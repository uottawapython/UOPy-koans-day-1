#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The path to enl ightenment starts with the following:

import unittest

from koans.about_asserts import AboutAsserts
from koans.about_variables import AboutVariables
from koans.about_operators import AboutOperators
from koans.about_strings import AboutStrings
from koans.about_none import AboutNone
#from koans.about_lists import AboutLists
#from koans.about_list_assignments import AboutListAssignments
#from koans.about_control_statements import AboutControlStatements

def koans():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    loader.sortTestMethodsUsing = None
    suite.addTests(loader.loadTestsFromTestCase(AboutAsserts))
    suite.addTests(loader.loadTestsFromTestCase(AboutVariables))
    suite.addTests(loader.loadTestsFromTestCase(AboutOperators))
    suite.addTests(loader.loadTestsFromTestCase(AboutStrings))
    suite.addTests(loader.loadTestsFromTestCase(AboutNone))
    #suite.addTests(loader.loadTestsFromTestCase(AboutLists))
    #suite.addTests(loader.loadTestsFromTestCase(AboutListAssignments))
    #suite.addTests(loader.loadTestsFromTestCase(AboutControlStatements))

    return suite
