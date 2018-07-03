# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from ferrieres.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of ferrieres.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ferrieres.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ferrieres.urban.dataimport'))

    def test_uninstall(self):
        """Test if ferrieres.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['ferrieres.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('ferrieres.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IFerrieresUrbanDataimportLayer is registered."""
        from ferrieres.urban.dataimport.interfaces import IFerrieresUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IFerrieresUrbanDataimportLayer in utils.registered_layers())
