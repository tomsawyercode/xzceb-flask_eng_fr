import unittest
from translator import english_to_french, french_to_english


class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None) 
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Night'),'Nuit')
        self.assertNotEqual(english_to_french('Night'),'Night')
        
class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None), None) 
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Nuit'),'Night')
        self.assertNotEqual(french_to_english('Nuit'),'Nuit')        
  
unittest.main()



