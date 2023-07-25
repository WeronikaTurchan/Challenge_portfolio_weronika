import unittest

from unittest.loader import makeSuite


from test_cases.add_player import TestAddAPlayer
from test_cases.change_language import TestChangeLanguage
from test_cases.framework import Test
from test_cases.login_correct import TestLoginPage
from test_cases.login_invalid_data import TestLoginPageInvalidData
from test_cases.show_list_of_players import TestShowPlayers


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestLoginPageInvalidData))
   test_suite.addTest(makeSuite(TestChangeLanguage))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestShowPlayers))
   test_suite.addTest(makeSuite(Test))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())