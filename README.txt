Introduction
============

This is an index that supports depth limiting, and the ability to build a
structure usable for navtrees and sitemaps. The actual navtree implementations
are not (and should not) be in this Product, this is the index implementation
only.

Assumptions
===========

EPI makes an assumption about the catalog and index being in the
same container as all the content. This makes a lot of sense in a
Plone setting, but might not work as expected in other scenarios.

A query like ``/plonesite/folder, level=0`` is transformed internally to
``/folder, level=1``. This avoids touching the rather large plonesite set
which contains reference to all content in your site.

Features
========

- Can construct a site map with a single catalog query

- Can construct a navigation tree with a single catalog query

Usage
=====

``catalog(path='some/path')``
  search for all objects below some/path (recursive, equivalent to depth = -1)

``catalog(path={'query' : 'some/path', 'depth' : 0})``
  search for the object with the given path.

``catalog(path={'query' : 'some/path', 'depth' : 2 )``
  search for all objects below some/path but only down to a depth of 2

``catalog(path={'query' : 'some/path', 'navtree' : 1 )``
  search for all objects below some/path for rendering a navigation tree. This
  includes all objects below some/path up to a depth of 1 and all parent
  objects.

``catalog(path={'query' : 'some/path', 'navtree' : 1, 'depth': 0 })``
  search for all objects below some/path for rendering a breadcrumb trail.
  This includes only the parent objects themselves.

``catalog(path={'query' : 'some/path', 'navtree':1, 'navtree_start':1})``
  search for all objects below some/path for rendering a partial
  navigation tree. This includes all objects below the path but stops
  1 level above the root.  The given path is included, even if it is at a
  lower level in the portal than the start parameter would allow.

``catalog(path={'query' : 'some/path', 'navtree':1, 'depth':0, 'navtree_start':1})``
  search for all objects below some/path for rendering a partial
  breadcrumb trail. This includes all parents below the path but stops
  1 level above the root.  The given path is included, even if it is at a
  lower level in the portal than the start parameter would allow.
 
Credits
=======

- Zope Corporation for the initial PathIndex code

- Helge Tesdal from Jarn_ for the ExtendedPathIndex implementation

- Alec Mitchell for the navtree and listing optimizations

.. _Jarn: http://jarn.com


License
=======

This software is released under the ZPL license.

