import unittest
from image import Image


class TextSummarizer(unittest.TestCase):

    def test_summarize(self):
        test_image = Image("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        print(test_image.get_text_summary())
        print(test_image.get_text_summary())
        test_image_no_words = Image("Pic With No Words", '../images/pexels-nicole-avagliano-2893556.jpeg')
        print(test_image_no_words)
        print(test_image_no_words.get_text_summary())