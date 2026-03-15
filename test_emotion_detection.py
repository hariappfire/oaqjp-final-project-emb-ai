import unittest
from unittest.mock import patch
from emotion_detection import emotion_detector # Assuming your file is named emotion_detection.py

class TestEmotionDetector(unittest.TestCase):


    def test_emotion_detector_joy(self):
        """Test a successful API response."""
   

        # Execute the function
        result = emotion_detector("I am glad this happened")
        data = result['emotionPredictions'][0]['emotion']

# Find the key with the maximum value
        dominant_emotion = max(data, key=data.get)
        dominant_value = data[dominant_emotion]
        # Assertions
        self.assertEqual("joy", dominant_emotion)
     
    def test_emotion_detector_anger(self):
        """Test a successful API response."""
   

        # Execute the function
        result = emotion_detector("I am really mad about this")
        data = result['emotionPredictions'][0]['emotion']

# Find the key with the maximum value
        dominant_emotion = max(data, key=data.get)
        dominant_value = data[dominant_emotion]
        # Assertions
        self.assertEqual("anger", dominant_emotion)
    
    def test_emotion_detector_disgust(self):
        """Test a successful API response."""
   

        # Execute the function
        result = emotion_detector("I feel disgusted just hearing about this")
        data = result['emotionPredictions'][0]['emotion']

# Find the key with the maximum value
        dominant_emotion = max(data, key=data.get)
        dominant_value = data[dominant_emotion]
        # Assertions
        self.assertEqual("disgust", dominant_emotion)
        # Assertions
    def test_emotion_detector_sadness(self):
        """Test a successful API response."""
   

        # Execute the function
        result = emotion_detector("I am so sad about this")
        data = result['emotionPredictions'][0]['emotion']

# Find the key with the maximum value
        dominant_emotion = max(data, key=data.get)
        dominant_value = data[dominant_emotion]
        # Assertions
        self.assertEqual("sadness", dominant_emotion)
        # Assertions

    def test_emotion_detector_fear(self):
        """Test a successful API response."""
   

        # Execute the function
        result = emotion_detector("I am really afraid that this will happen")
        data = result['emotionPredictions'][0]['emotion']

# Find the key with the maximum value
        dominant_emotion = max(data, key=data.get)
        dominant_value = data[dominant_emotion]
        # Assertions
        self.assertEqual("fear", dominant_emotion)
        # Assertions

     

if __name__ == '__main__':
    unittest.main()
