from text_summarizer import summarize

test_text = ["This is sentence one and it is about a rubber ball.", "This is sentence two and the rubber ball is "
                                                                    "bouncing.", "The rubber ball exploded."]
test_text2 = "This is a long string about a red rubber ball that bounced and rolled and sprung"
print(summarize(test_text))
import unittest
from image import Image
from image_list import ImageList
from text_summarizer import summarize


class TextSummarizer(unittest.TestCase):

    def test_summarize(self):
        test_image = Image("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        print(test_image.get_text_summary())
