import unittest
from image import Image
from image_list import ImageList
from text_summarizer import summarize


class TextSummarizer(unittest.TestCase):

    def test_summarize(self):
        test_image = Image("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        print(test_image.get_text_summary())
