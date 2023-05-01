import unittest
from image import Image


class ImageText(unittest.TestCase):

    def test_image_to_text(self):
        test_image = Image("Cheese Meme", "images/FBb9ymGWUAEymnf.jpeg")
        self.assertEqual(20, len(test_image.get_image_text()))

