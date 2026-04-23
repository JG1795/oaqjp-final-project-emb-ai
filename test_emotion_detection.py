import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionPredictor(unittest.TestCase):

    def test_joy(self):
        test_text = "I am glad this happened"
        result = emotion_detector(test_text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        test_text = "I am really mad about this"
        result = emotion_detector(test_text)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        test_text = "I feel disgusted just hearing about this"
        result = emotion_detector(test_text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        test_text = "I am so sad about this"
        result = emotion_detector(test_text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        test_text = "I am really afraid that this will happen"
        result = emotion_detector(test_text)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()