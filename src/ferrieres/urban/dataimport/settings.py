# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.csv.settings import CSVImporterSettings


class FerrieresImporterSettingsForm(ImporterSettingsForm):
    """ """

class FerrieresImporterSettings(ImporterSettings):
    """ """
    form = FerrieresImporterSettingsForm


class FerrieresImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = FerrieresImporterSettings


class FerrieresImporterFromImportSettings(CSVImporterSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(FerrieresImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
