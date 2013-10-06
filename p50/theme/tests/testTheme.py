import time
import unittest2 as unittest
from zExceptions import BadRequest

from zope.component import getSiteManager
from zope.component import getUtility

from plone.app.theming.utils import getAvailableThemes

from Products.CMFCore.utils import getToolByName

from base import PROJECTNAME
from base import INTEGRATION_TESTING

class TestThemeInstalled(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = INTEGRATION_TESTING
    
    def setUp(self):
        self.portal = self.layer['portal']
    
    def testBrowserLayerRegistered(self):
        sm = getSiteManager(self.portal)
        themes = getAvailableThemes()
        assert len(themes) > 0, "No theme installed"
        theme = themes[0]
        assert theme.__name__ == 'p50.theme'
        assert theme.absolutePrefix == '/++theme++p50.theme'
