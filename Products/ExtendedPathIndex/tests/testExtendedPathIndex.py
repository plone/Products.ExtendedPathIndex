# Copyright (c) 2004 Zope Corporation and Plone Solutions
# ZPL 2.1 license

import unittest

class Dummy:
    def __init__(self, path):
        self.path = path
    def getPhysicalPath(self):
        return self.path.split('/')


class TestBase(object):
    def _makeOne(self):
        from Products.ExtendedPathIndex.ExtendedPathIndex import ExtendedPathIndex
        return ExtendedPathIndex('path')
    
    def _populateIndex(self):
        for k, v in self._values.items():
            self._index.index_object( k, v )


class TestPathIndex(TestBase, unittest.TestCase):
    """ Test ExtendedPathIndex objects """
    def setUp(self):
        self._index = self._makeOne()
        self._values = {
            1 : Dummy("/aa/aa/aa/1.html"),
            2 : Dummy("/aa/aa/bb/2.html"),
            3 : Dummy("/aa/aa/cc/3.html"),
            4 : Dummy("/aa/bb/aa/4.html"),
            5 : Dummy("/aa/bb/bb/5.html"),
            6 : Dummy("/aa/bb/cc/6.html"),
            7 : Dummy("/aa/cc/aa/7.html"),
            8 : Dummy("/aa/cc/bb/8.html"),
            9 : Dummy("/aa/cc/cc/9.html"),
            10: Dummy("/bb/aa/aa/10.html"),
            11: Dummy("/bb/aa/bb/11.html"),
            12: Dummy("/bb/aa/cc/12.html"),
            13: Dummy("/bb/bb/aa/13.html"),
            14: Dummy("/bb/bb/bb/14.html"),
            15: Dummy("/bb/bb/cc/15.html"),
            16: Dummy("/bb/cc/aa/16.html"),
            17: Dummy("/bb/cc/bb/17.html"),
            18: Dummy("/bb/cc/cc/18.html")
        }

    def testEmpty(self):
        self.assertEqual(self._index.numObjects() ,0)
        self.assertEqual(self._index.getEntryForObject(1234), None)
        self._index.unindex_object( 1234 ) # nothrow
        self.assertEqual(self._index._apply_index(dict(suxpath="xxx")), None)

    def testUnIndex(self):
        self._populateIndex()
        self.assertEqual(self._index.numObjects(), 18)

        for k in self._values.keys():
            self._index.unindex_object(k)

        self.assertEqual(self._index.numObjects(), 0)
        self.assertEqual(len(self._index._index), 0)
        self.assertEqual(len(self._index._unindex), 0)

    def testReindex(self):
        self._populateIndex()
        self.assertEqual(self._index.numObjects(), 18)

        o = Dummy('/foo/bar')
        self._index.index_object(19, o)
        self.assertEqual(self._index.numObjects(), 19)
        self._index.index_object(19, o)
        self.assertEqual(self._index.numObjects(), 19)

    def testUnIndexError(self):
        self._populateIndex()
        # this should not raise an error
        self._index.unindex_object(-1)

        # nor should this
        self._index._unindex[1] = "/broken/thing"
        self._index.unindex_object(1)

    def testRoot(self):
        self._populateIndex()
        
        queries = (
            dict(path=dict(query='/', level=0)),
            dict(path=(('/', 0),)),
        )
        for q in queries:
            res = self._index._apply_index(q)
            self.assertEqual(list(res[0].keys()), range(1,19))

    def testSimpleTests(self):
        self._populateIndex()
        tests = [
            # component, level, expected results
            ("aa", 0, [1,2,3,4,5,6,7,8,9]),
            ("aa", 1, [1,2,3,10,11,12] ),
            ("bb", 0, [10,11,12,13,14,15,16,17,18]),
            ("bb", 1, [4,5,6,13,14,15]),
            ("bb/cc", 0, [16,17,18]),
            ("bb/cc", 1, [6,15]),
            ("bb/aa", 0, [10,11,12]),
            ("bb/aa", 1, [4,13]),
            ("aa/cc", -1, [3,7,8,9,12]),
            ("bb/bb", -1, [5,13,14,15]),
            ("18.html", 3, [18]),
            ("18.html", -1, [18]),
            ("cc/18.html", -1, [18]),
            ("cc/18.html", 2, [18]),
        ]

        # Test with the level passed in as separate parameter
        for comp, level, results in tests:
            for path in [comp, "/"+comp, "/"+comp+"/"]:
                res = self._index._apply_index(dict(path=
                    dict(query=path, level=level)))
                lst = list(res[0].keys())
                self.assertEqual(lst, results)

        # Test with the level passed in as part of the path parameter
        for comp, level, results in tests:
            for path in [comp, "/"+comp, "/"+comp+"/"]:
                res = self._index._apply_index(dict(path=
                    dict(query=((path, level),))))
                lst = list(res[0].keys())
                self.assertEqual(lst, results)

    def testComplexOrTests(self):
        self._populateIndex()
        tests = [
            # Path query (as list or (path, level) tuple), level, expected
            (['aa','bb'], 1, [1,2,3,4,5,6,10,11,12,13,14,15]),
            (['aa','bb','xx'], 1, [1,2,3,4,5,6,10,11,12,13,14,15]),
            ([('cc',1), ('cc',2)], 0, [3,6,7,8,9,12,15,16,17,18]),
        ]

        for lst, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=lst, level=level, operator='or')))
            lst = list(res[0].keys())
            self.assertEqual(lst, results)

    def testComplexANDTests(self):
        self._populateIndex()
        tests = [
            # Path query (as list or (path, level) tuple), level, expected
            (['aa','bb'], 1, []),
            ([('aa',0), ('bb',1)], 0, [4,5,6]),
            ([('aa',0), ('cc',2)], 0, [3,6,9]),
        ]

        for lst, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=lst, level=level, operator='and')))
            lst = list(res[0].keys())
            self.assertEqual(lst, results)


class TestExtendedPathIndex(TestBase, unittest.TestCase):
    """ Test ExtendedPathIndex objects """
    def setUp(self):
        self._index = self._makeOne()
        self._values = {
            1 : Dummy("/1.html"),
            2 : Dummy("/aa/2.html"),
            3 : Dummy("/aa/aa/3.html"),
            4 : Dummy("/aa/aa/aa/4.html"),
            5 : Dummy("/aa/bb/5.html"),
            6 : Dummy("/aa/bb/aa/6.html"),
            7 : Dummy("/aa/bb/bb/7.html"),
            8 : Dummy("/aa"),
            9 : Dummy("/aa/bb"),
            10: Dummy("/bb/10.html"),
            11: Dummy("/bb/bb/11.html"),
            12: Dummy("/bb/bb/bb/12.html"),
            13: Dummy("/bb/aa/13.html"),
            14: Dummy("/bb/aa/aa/14.html"),
            15: Dummy("/bb/bb/aa/15.html"),
            16: Dummy("/bb"),
            17: Dummy("/bb/bb"),
            18: Dummy("/bb/aa")
        }

    def testIndexIntegrity(self):
        self._populateIndex()
        index = self._index._index
        # Check that terminators have been added for all indexed items
        self.assertEqual(list(index[None][0].keys()), [1,8,16])
        self.assertEqual(list(index[None][1].keys()), [2,9,10,17,18])
        self.assertEqual(list(index[None][2].keys()), [3,5,11,13])
        self.assertEqual(list(index[None][3].keys()), [4,6,7,12,14,15])

    def testUnIndexError(self):
        self._populateIndex()
        # this should not raise an error
        self._index.unindex_object(-1)

        # nor should this
        self._index._unindex[1] = "/broken/thing"
        self._index.unindex_object(1)

    def testDepthLimit(self):
        self._populateIndex()
        tests = [
            # depth, expected result
            (1, [1,8,16]),
            (2, [1,2,8,9,10,16,17,18]),
            (3, [1,2,3,5,8,9,10,11,13,16,17,18]),
            ]

        for depth, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query='/', depth=depth)))
            lst = list(res[0].keys())
            self.assertEqual(lst, results)

    def testDefaultNavtree(self):
        self._populateIndex()
        tests = [
            # path, level, expected results
            ('/',         0, [1,8,16]),
            ('/aa',       0, [1,2,8,9,16]),
            ('/aa',       1, [2,3,9,10,13,17,18]),
            ('/aa/aa',    0, [1,2,3,8,9,16]),
            ('/aa/aa/aa', 0, [1,2,3,4,8,9,16]),
            ('/aa/bb',    0, [1,2,5,8,9,16]),
            ('/bb',       0, [1,8,10,16,17,18]),
            ('/bb/aa',    0, [1,8,10,13,16,17,18]),
            ('/bb/bb',    0, [1,8,10,11,16,17,18]),
            ]
        for path, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, level=level, depth=1, navtree=True)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results)

    def testShallowNavtree(self):
        self._populateIndex()
        # With depth 0 we only get the parents
        tests = [
            # path, level, expected results
            ('/',         0, []),
            ('/aa',       0, [8]),
            ('/aa',       1, [18]),
            ('/aa/aa',    0, [8]),
            ('/aa/aa/aa', 0, [8]),
            ('/aa/bb',    0, [8,9]),
            ('/bb',       0, [16]),
            ('/bb/aa',    0, [16,18]),
            ('/bb/bb',    0, [16,17]),
            ('/bb/bb/aa', 0, [16,17]),
            ]
        for path, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, level=level, depth=0, navtree=True)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results)

    def testNonexistingPaths(self):
        self._populateIndex()
        # With depth 0 we only get the parents
        # When getting non existing paths, 
        # we should get as many parents as possible when building navtree
        tests = [
            # path, level, expected results
            ('/',        0, []),
            ('/aa',      0, [8]), # Exists
            ('/aa/x',    0, [8]), # Doesn't exist
            ('/aa',      1, [18]),
            ('/aa/x',    1, [18]),
            ('/aa/aa',   0, [8]),
            ('/aa/aa/x', 0, [8]),
            ('/aa/bb',   0, [8,9]),
            ('/aa/bb/x', 0, [8,9]),
            ]
        for path, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, level=level, depth=0, navtree=True)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results)

    def testEmptyFolderDepthOne(self):
        # Shouldn't return folder when we want children of empty folder
        self._values = {
            1: Dummy("/portal/emptyfolder"),
            2: Dummy("/portal/folder"),
            3: Dummy("/portal/folder/document"),
            4: Dummy("/portal/folder/subfolder"),
            5: Dummy("/portal/folder/subfolder/newsitem")
        }
        self._populateIndex()
        tests = [
            # path, expected results
            ('/portal/folder',                    [3,4]),
            ('/portal/emptyfolder',               []),
            ('/portal/folder/document',           []),
            ('/portal/folder/subfolder',          [5]),
            ('/portal/folder/subfolder/newsitem', []),
            ]
        for path, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, depth=1)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results)

    def testSiteMap(self):
        self._values = {
            1: Dummy("/portal/emptyfolder"),
            2: Dummy("/portal/folder"),
            3: Dummy("/portal/folder/document"),
            4: Dummy("/portal/folder/subfolder"),
            5: Dummy("/portal/folder/subfolder/newsitem")
        }
        self._populateIndex()
        tests = [
            # Path, depth, expected results
            ('/', 1, []),
            ('/', 2, [1,2]),
            ('/', 3, [1,2,3,4]),
            ('/', 4, [1,2,3,4,5]),
            ('/', 5, [1,2,3,4,5]),
            ('/', 6, [1,2,3,4,5]),
            ]
        for path, depth, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, depth=depth)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results)


    def testBreadCrumbsWithStart(self):
        self._populateIndex()
        # Adding a navtree_start > 0 to a breadcrumb search should generate
        # breadcrumbs back to that level above the root.
        tests = [
            # path, level, navtree_start, expected results
            ('/',                 0, 1, []),
            ('/aa',               0, 1, []),
            ('/aa/aa',            0, 1, [8]),
            ('/aa/aa/aa',         0, 1, [8]),
            ('/aa/bb',            0, 1, [8,9]),
            ('/bb',               0, 1, []),
            ('/bb/aa',            0, 1, [16,18]),
            ('/bb/aa',            0, 2, []),
            ('/bb/bb',            0, 1, [16,17]),
            ('/bb/bb',            0, 2, []),
            ('/bb/bb/bb/12.html', 0, 1, [12,16,17]),
            ('/bb/bb/bb/12.html', 0, 2, [12,17]),
            ('/bb/bb/bb/12.html', 0, 3, [12]),
            ('aa',                1, 1, [18]),
            ('aa',                1, 2, []),
            ]
        for path, level, navtree_start, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, level=level, navtree_start=navtree_start,
                     depth=0, navtree=True)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results,
                        '%s != %s Failed on %s start %s'%(
                                               lst,results,path,navtree_start))

    def testNegativeDepthQuery(self):
        self._populateIndex()
        tests = [
            # path, level, expected results
            ('/',      0, range(1,19)),
            ('/aa',    0, [2,3,4,5,6,7,8,9]),
            ('/aa/aa', 0, [3,4]),
            ('/aa/bb', 0, [5,6,7,9]),
            ('/bb',    0, [10,11,12,13,14,15,16,17,18]),
            ('/bb/aa', 0, [13,14,18]),
            ('/bb/bb', 0, [11,12,15,17]),
            ('aa',     1, [3,4,13,14,18]),
        ]

        for path, level, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, level=level)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results,
                        '%s != %s Failed on %s level %s'%(
                                        lst,results,path,level))

    def testPhysicalPathOptimization(self):
        self._populateIndex()
        # Fake a physical path for the index
        self._index.getPhysicalPath = lambda: ('','aa')
        # Test a variety of arguments
        tests = [
            # path, depth, navtree, expected results
            ('/',              1, False, [1,8,16]), # Sitemap
            ('/',              0, True,  []), # Non-Existant
            ('/',              0, True,  []), # Breadcrumb tests
            ('/aa',            0, True,  [8]),
            ('/aa/aa',         0, True,  [8]),
            ('/',              1, True,  [1,8,16]), # Navtree tests
            ('/aa',            1, True,  [1,2,8,9,16]),
            ('/aa/aa',         1, True,  [1,2,3,8,9,16]),
            ('/',              0, False, []), # Depth Zero tests
            ('/aa',            0, False, [8]),
            ('/aa/aa',         0, False, []),
            ('/',             -1, False, range(1,19)), # Depth -1
            ('/aa',           -1, False, range(1,19)), # Should assume that
                                                       # all paths are relevant
            ((('aa/aa', 1),), -1, False, [4,14]) # A (path, level) tuple, 
                                                       # relative search
        ]

        for path, depth, navtree, results in tests:
            res = self._index._apply_index(dict(path=
                dict(query=path, depth=depth, navtree=navtree)))
            lst = list(res[0].keys())
            self.assertEqual(lst,results,
                        '%s != %s Failed on %s depth %s navtree %s'%(
                                        lst,results,path,depth,navtree))


def test_suite():
    import unittest, sys
    return unittest.findTestCases(sys.modules[__name__])
