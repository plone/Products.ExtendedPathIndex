#
# Skeleton TestCase
#

from Testing import ZopeTestCase

ZopeTestCase.installProduct('ExtendedPathIndex')


class TestSomething(ZopeTestCase.ZopeTestCase):

    def afterSetUp(self):
        pass

    def testSomething(self):
        # Test something
        self.failUnless(1==1)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestSomething))
    return suite
