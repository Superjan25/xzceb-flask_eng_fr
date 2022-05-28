import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french('Hello'), 'Hola')
        self.assertEqual(english_to_french(''),'No text entered')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hola')
        self.assertEqual(french_to_english(''),'Pas de text entré')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()