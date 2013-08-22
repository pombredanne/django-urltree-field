django-urltree-field
====================

Creates a tree of URL-Nodes by crawling a website, which can be accessed in models by UrlTreeField.


Installation
------------

#. pip install -e git@github.com:ralfzen/django-urltree-field.git

#. Add ``urltree`` to your INSTALLED_APPS._

#. Deploy the necessary static files. If you are using Django 1.3 and ``contrib.staticfiles`` the 
   necessary static files should be picked up automatically. In all other cases you have to copy or
   symlink the static files.

#. Browse to ``/urltree/build/<domain>/``. If no domain is given the current Site of django's builtin sites-module will be taken.


Configuration
-------------

In your models.py::

    from urltree.fields import UrlTreeField
  
    class MyModel(models.Model):
      link = UrlTreeField(blank=True)


That's it.
