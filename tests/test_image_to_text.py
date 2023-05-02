import unittest
from image import Image


class ImageText(unittest.TestCase):

    def test_image_to_text(self):
        test_image = Image("Cheese Meme", "../images/FBb9ymGWUAEymnf.jpeg")
        self.assertEqual(20, len(test_image.get_image_text()))
        #test_image.print_image()
        test_image = Image("Steezus Christ", "../images/74cd5f7c132ba6c02cec6e3ea6d981b18c8e26e44f566325198d613040583e5e_3.jpeg")
        self.assertEqual(14, len(test_image.get_image_text()))
        #test_image.print_image()
        test_image = Image("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        # print(test_image.get_image_text())
        # self.assertEqual(226, len(test_image.get_image_text()))
        # test_image.print_image()
        print(test_image.get_text_summary())

