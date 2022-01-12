from Issue_Localizer import Localizer
import unittest

class TestLocalizer(unittest.TestCase):
    def testSearch(self):
        self.assertEqual(Localizer(editor="code")._search("..\\", "essai"),"", "Failed")

    def testSearch(self):
        self.assertEqual(Localizer(editor="code")._search2("..\\", "essai"), "", "Failed")
    

if __name__=="__main__":
    unittest.main()
    