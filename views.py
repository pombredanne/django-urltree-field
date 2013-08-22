# -*- coding: utf-8 -*-
import sys
import urllib2
import urlparse
import string
from BeautifulSoup import BeautifulSoup
from time import gmtime, strftime
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from annoying.decorators import ajax_request
from django.conf import settings as django_settings
from urltree.models import URLTree, URLNode
from urltree import settings
from urltree.logger import logger
from urltree.helpers import normalize_url, save_links_to_nodes
from django.template.defaultfilters import force_escape as escape


MAX_TIMEOUTS = 10
MAX_TIMEOUT_TIME = 5

# unfortunately you need to run 2 development-servers because 2 parallel or do a subprocess-crawl ...

def build_tree(request, domain=None):
    """ makes tree from ´´links´´ (=list)
    No resume, but rebuild.
    """
    if domain == None:
        domain = Site.objects.get_current().domain

    # create tree
    urltree, created = URLTree.objects.get_or_create(domain=domain)
    
    if not created: # clear tree
        urltree.nodes.all().delete()

    context = {
        'starttime': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()),
        'settings_var': settings,
        'query': request.GET.copy(),
        'domain': domain,
    }
    return render(request, 'urltree/urltree_build.html', context)


@ajax_request
def get_logging(request):
    if not request.method == 'GET':
        return logger.warning('no GET Request')
    with open(django_settings.SITE_ROOT + "/urltree-logfile", 'r+') as f:
        content = f.readlines()
        f.seek(0) # pointer to beginning again
        f.truncate() # for erasing
    return {'value': content}

    
@ajax_request
def process_nodes(request, domain):
    """ prints to screen with simple ajax-polling """
    # timeouts
    timeouts = 0
    logger.debug('timeouts: %s' % timeouts)
    
    # urltree
    try: 
        urltree = URLTree.objects.get(domain=domain)    # one tree per domain
    except URLTree.DoesNotExist:
        logger.error('Missing URLTree. try build before.')
        return {'value': 'Missing URLTree. try /urltree/build before or go to admin.',}
    
    # root
    root_url = 'http://%s' % domain
    root_url = root_url.rstrip('/')+'/'
    rootNode = URLNode.objects.get_or_create(urltree=urltree, url=root_url)[0]
    logger.debug("rootNode: %s" % rootNode)
    
    # links
    unchecked_links = list(URLNode.objects.filter(urltree=urltree, checked=False).values_list('url', flat=True))
    checked_links = URLNode.objects.filter(urltree=urltree, checked=True).values_list('url', flat=True)

    #crawl
    for link in unchecked_links:
        crawled_links = []
        logger.info('processing: %s' % link)
        try:
            url = urllib2.urlopen(link, timeout=MAX_TIMEOUT_TIME)
        except urllib2.URLError, e:
            timeouts += 1
            logger.warning("%s: %s" % (str(timeouts), escape(str(e))))
            if timeouts > MAX_TIMEOUTS:
                logger.error("BREAK because of too many errors: try later to check the other links")
                break
            continue

        # check for media (no download - only for existence)
        urlinfo = url.info()
        if urlinfo.type != 'text/html':
            logger.info("media: %s" % link)
            continue
        
        # parse for links
        src = url.read()
        bs = BeautifulSoup(src)
        for a_elem in bs.findAll('a', {'href':True}):
            absUrl = urlparse.urljoin(link, a_elem['href'])
            parsedUrl = urlparse.urlparse(absUrl)
            logger.debug('href: %s | absURL: %s | parsedUrl: %s' % (a_elem['href'], absUrl, parsedUrl))
            
            hostUrl = normalize_url(absUrl)
            
            absUrl = urlparse.urlunparse((parsedUrl.scheme, hostUrl, parsedUrl.path,
                        parsedUrl.params, parsedUrl.query, parsedUrl.fragment))
                        
            logger.debug('absURL: %s | parsedUrl: %s' % (absUrl, parsedUrl))
            
            if (parsedUrl.scheme == 'http') and ( # http for crawling
                parsedUrl.netloc == domain) or ( # URL must be internal
                parsedUrl.netloc.endswith('.' + domain)): # or subdomain
                if absUrl not in crawled_links and (
                absUrl not in unchecked_links) and (
                absUrl not in checked_links):
                    unchecked_links.append(absUrl) # if link is new append for crawling
    
    save_links_to_nodes(unchecked_links, urltree)

    logger.info('%s links checked %s' % (len(unchecked_links), strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())))
    return {}

    
def show_tree(request):
    urltrees = URLTree.objects.all()
    if urltrees.count() == 0:
        return redirect('urltree-build')
    context = {
        'urltrees': urltrees,
        'settings_var': settings,
        'query': request.GET.copy(),
        'current_site': Site.objects.get_current(),
    }
    
    return render(request, 'urltree/urltree.html', context)
