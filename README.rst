Introduction
============

This is an Zope Catalog index to query treeish structures in the ZODB by path.
It supports depth limiting, and has the ability to build a structure usable for navtrees and sitemaps.
The actual navtree implementations are not (and should not) be in this package.
This is the index implementation only.

Assumptions
===========

EPI makes an assumption about the catalog and index being in the same container as all the content.
This makes a lot of sense in a Plone setting, but might not work as expected in other scenarios.

A query like ``/plonesite/folder, level=0`` is transformed internally to ``/folder, level=1``.
This avoids touching the rather large plonesite set which contains reference to all content in your site.

Features
========

- Can construct a site map with a single catalog query

- Can construct a navigation tree with a single catalog query

Configuration
=============

In a GenericSetup profile, provide th following snippet to create an index::

  <index
      meta_type="ExtendedPathIndex"
      name="my_path">
    <extra
        name="indexed_attrs"
        value="my_path"
    />
  </index>

For multi valued paths, provide an extra
(switches off an breaking optimization not needed for this cases)::

  <index
      meta_type="ExtendedPathIndex"
      name="my_path">
    <extra
        name="indexed_attrs"
        value="my_path"
    />
    <extra
        name="multi_valued"
        value="True"
    />
  </index>

An example for an index with multiple values per path element:
Imagine to index multilingual content.
Every item is translated and all translated items share a common unique identifier
(this is how plone.app.multilingual works).
Now create an indexer returning this unique identifier instead of the items ID as a path element.
With this it is possible to query all elements of all languages in a folder in one go
(for an advanced usage of this pattern look at ``plone.app.multilingualindexes``).

Usage
=====

``catalog(path='some/path')``
  search for all objects below some/path (recursive, equivalent to depth = -1)

``catalog(path=dict(query='some/path', depth=0))``
  search for the object with the given path.
  For multi valued paths, multiple objects are returned.

``catalog(path=dict(query='some/path', depth=2))``
  search for all objects below some/path but only down to a depth of 2

``catalog(path=dict(query='some/path', navtree=True))``
  search for all objects below some/path for rendering a navigation tree.
  This includes all objects below some/path up to a depth of 1 and all parent objects.

``catalog(path=dict(query='some/path', navtree=True, depth=0))``
  search for all objects below some/path for rendering a breadcrumb trail.
  This includes only the parent objects themselves.

``catalog(path=dict(query='some/path', navtree=True, navtree_start=1))``
  search for all objects below some/path for rendering a partial navigation tree.
  This includes all objects below the path but stops 1 level above the root.
  The given path is included,
  even if it is at a shorter path in the portal than the level parameter would allow.

``catalog(path=dict(query='some/path', navtree=True, depth=0, navtree_start=1))``
  search for all objects below some/path for rendering a partial breadcrumb trail.
  This includes all parents below the path but stops 1 level above the root.
  The given path is included, even if it is at a lower level in the portal than the start parameter would allow.

``catalog(path=dict(query='some/path', level=2))``
  search for all objects whose path contains some/path at level 2.
  This includes paths like /foo/bar/some/path and /spam/eggs/some/path,
  plus all children of those paths.

``catalog(path=dict(query='some/path', level=-1, depth=0))``
  search for all objects whose path contains some/path at *any* level.
  This includes paths like /spam/some/path as well as /foo/bar/baz/some/path,
  but only those exact matches are included in the result because depth is set to 0.

``catalog(path=dict(query=(('foo/bar', 2), ('bar/baz'), 1), depth=0))``
  search for multiple paths,
  each at different levels
  (foo/bar at level 2, and bar/baz at level 1),
  and return exact matches only.

Credits
=======

- Zope Corporation for the initial PathIndex code

- Helge Tesdal and Martijn Pieters from Jarn_ for the ExtendedPathIndex implementation

- Alec Mitchell for the navtree and listing optimizations

.. _Jarn: http://jarn.com


License
=======

This software is released under the GPLv2 license.

