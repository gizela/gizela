.. Gizela documentation master file, created by
   sphinx-quickstart on Thu Jul 11 21:36:44 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Gizela project
=========================

Geodetic data analyzer...

Package Documentation
---------------------
The documentation is writen in mess of epytext_ and restructured_ text.

.. _epytext: http://epydoc.sourceforge.net/
.. _restructured: http://docutils.sourceforge.net/rst.html

Code style variants 
-------------------
The package is hopefully writen in Python "new style"
http://www.python.org/doc/newstyle/

- Topics
    - Private and Public
        - __slots__ It looks a little bit tricky. Do we realy want to use them? http://docs.python.org/reference/datamodel.html#slots}
        - Underscore. Gizela use simple underscore as sign of private atribute or method.
    - method and atributes U{http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html}

    - super() method simplifies calling supercalss' constructor U{http://docs.python.org/library/functions.html#super}
    - Class and data atributes U{http://diveintopython.org/object_oriented_framework/class_attributes.html}
    - Properties and descriptors U{http://users.rcn.com/python/download/Descriptor.htm#properties}
    - Functions and Methods. It looks the method is regular function where its first argument is reserved for object instance. U{http://users.rcn.com/python/download/Descriptor.htm#functions-and-methods}
    - Static a class methods. Not used in Gizela project. U{http://users.rcn.com/python/download/Descriptor.htm#static-methods-and-class-methods}
    - x = property(_getx, _setx, _delx, "I'm the 'x' property.") Properties are sometimes called managed atributes.
            It is easier ??? way then using pure Python descriptors. http://users.rcn.com/python/download/Descriptor.htm}



.. """__license__ = 'GPL v 3' The license governing the use and distribution of gizela"""

API documentation
=================

.. toctree::
   :maxdepth: 1
   
   api
   
.. * :doc:`api`


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

