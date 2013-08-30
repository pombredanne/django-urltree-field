# -*- coding: utf-8 -*-
import urlparse
from urltree.logger import logger
from urltree.models import URLNode


def get_host(url):
    parsedUrl = urlparse.urlparse(url)
    hostUrl = parsedUrl.netloc
    logger.debug('hostUrl: %s ' % hostUrl)
    return hostUrl
    
def save_links_to_nodes(unchecked_links, urltree):
    for crawled_link in unchecked_links:
        node = URLNode.objects.get_or_create(urltree=urltree, 
            url=crawled_link.rstrip('/')+'/')[0]
        node.checked = True
        node.save()
    set_parents_for_nodes(urltree)

def set_parents_for_nodes(urltree):
    """ parent-find-algorithm on basis of url """
    for node in URLNode.objects.filter(urltree=urltree, checked=True, parent=None):
        candidate = node.url
        logger.debug('orphan-node: %s')
        while (True):
            candidate = candidate[0:candidate.rstrip('/').rfind('/')+1] # possible caveat
            logger.debug('ParentCandidate: ' + candidate)
            if candidate.lower() == 'http://':
                break
            try:
                parent = URLNode.objects.get(url=candidate, urltree=urltree)
            except URLNode.DoesNotExist:
                continue
            logger.info("found parent: %s for %s" % (parent, node.url))
            node.parent=parent
            node.save()
            break
