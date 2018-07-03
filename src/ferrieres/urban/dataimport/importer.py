# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.csv.importer import CsvDataImporter
from ferrieres.urban.dataimport.interfaces import IFerrieresDataImporter


class FerrieresDataImporter(CsvDataImporter):
    """ """

    implements(IFerrieresDataImporter)
