Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

4.0.1 (2020-09-28)
------------------

Bug fixes:


- unpin zc.buildout
- pin versions to Zope 4 (otherwise Python 2.7 version cannot be built anymore)
- update tox.ini to align with setup classifiers
- add `Products.ZCatalog` to setup.py's `install_requires`, as it is no longer part of Zope core (#17)


4.0.0 (2020-05-06)
------------------

Breaking changes:


- Drop compatibility for ZCatalog < 4 [jensens] (#15)


Bug fixes:


- Fix IRO of EPI. [jensens] (#15)


3.4.2 (2019-05-01)
------------------

Bug fixes:


- Avoid a deprecation warning.
  [gforcada] (#10)


3.4.1 (2018-12-14)
------------------

Bug fixes:


- Rerelease without changes to update the changelog properly. (#7)


3.4.0 (2018-12-14)
------------------

New features:


- Support allow multi value results for "virtual" paths. [jensens] (#7)


3.3.1 (2018-09-23)
------------------

Bug fixes:

- Fix dependencies defined in setup.py.
  [gforcada]


3.3.0 (2018-01-17)
------------------

New features:

- Add compatibility with Python 3.


3.2.0 (2017-08-27)
------------------

New features:

- Add forward compatibility with ZCatalog 4's IQueryIndex interface.


3.1.1 (2016-07-29)
------------------

Bug Fixes:

- Use zope.interface decorator.
  [gforcada]


3.1 (2013-01-01)
----------------

* The behavior is inconsistent, because as long as the input path length is
  shorter or equal to the longest indexed path, there is no requirement that
  the entire path is indexed already.
  [bosim]

3.0.1 - 2012-06-30
------------------

* Fixed depth limited searches, when the path index wasn't the first index
  in the query plan. Thx to Peter Mathis for reporting the problem.
  [hannosch]

3.0 - 2012-04-26
----------------

* Fixed TypeError on insert when parent_path is not in the index_parents.
  [maurits]

* Better protection against corrupted internal data in ``_index_parents``.
  [hannosch]

* Slightly optimize reindexing an object by passing in information from the
  index to the unindex method and avoiding another unindex scan.
  [hannosch]

* Avoid an extra unindex scan for determining length changes in index_object.
  [hannosch]

* Declared support for new ILimitedResultIndex interface and require at least
  Zope 2.13.0a3.
  [hannosch]

* Merge in optimizations from ``experimental.catalogqueryplan``.
  [hannosch]

* PEP8 cleanup and minor optimizations in un/index code.
  [hannosch]

* Specify distribution dependencies.
  [hannosch]

2.9 - 2010-07-18
----------------

* Update license to GPL version 2 only.
  [hannosch]

2.8 - 2010-05-01
----------------

* No longer depend directly on test internals of PathIndex.
  [hannosch]

2.7 - 2009-11-13
----------------

* Added AccessControl import to tests to avoid cyclic import issue in
  Zope 2.12.
  [davisagli]

2.6 - 2009-05-18
----------------

* Clarified license to be only GPL.
  [hannosch]

* Declare package dependencies and fixed deprecation warnings for use
  of Globals.
  [hannosch]

2.5 - December 19, 2008
-----------------------

* Cleaned out tests: removing ZTC cruft, turning them into proper unit tests
  and removing tests that tested other non-index components.
  [mj]

* Fixed level handling for queries where a (path, level) tuple is passed in
  instead of using the general level parameter.
  [mj]

* Refactored and documented the index codebase. Several bugs were discovered
  and solved in the process. Missing functionality was also added, all search
  options should now work across all scenarios.
  [mj]

2.4.1 - September 28, 2008
--------------------------

- Fix typo in setup.py which broke installation of the egg
  [ree]



2.4 - September 11, 2006
------------------------

- Relaxed a check for path only allowing strings so far. Now we except all
  basestrings. This closes http://dev.plone.org/plone/ticket/5617.
  [hannosch]

- Converted log infrastructure to use Python's logging module instead zLOG.
  [hannosch]

2.3 - December 18, 2005
-----------------------

- Added some extra debug information when an improper path is cataloged.
  [sidnei]

2.2 - October 7, 2005
---------------------

- Add seperate index structures on the parent path and the full path of all
  objects.  This significantly improves scaling for navtrees, breadcrumbs,
  and listings.
  [alecm]

- Assume that EPI is used inside same container as content and use relative
  search instead of absolute - basically transforming / plonesite search
  to / search with startlevel set to 1 instead of 0.
  [tesdal]

2.1 - May 20, 2005
------------------

- Implement 'indexed_attrs' support for ExtendedPathIndex.

- Prevent navigation tree queries from stopping prematurely if the
  queried-for path does not actually exist in the index, but its parents do.

1.0
---

- Path index capable of generating a navigation tree structure from
  cataloged data.
