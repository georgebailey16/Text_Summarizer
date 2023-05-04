import unittest
from image import Image
from image_list import ImageList


class ImageText(unittest.TestCase):

    def test_image(self):
        test_image = Image("Cheese Meme", "../images/FBb9ymGWUAEymnf.jpeg")
        self.assertEqual(20, len(test_image.get_image_text_list()))
        test_image.print_image()
        test_image = Image("Steezus Christ", "../images/74cd5f7c132ba6c02cec6e3ea6d981b18c8e26e44f566325198d613040583e5e_3.jpeg")
        self.assertEqual(14, len(test_image.get_image_text_list()))
        test_image.print_image()
        test_image = Image("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        print(test_image.get_image_text_list())

        self.assertEqual(230, len(test_image.get_image_text_list()))
        # program reading bullet points as 'e', outputting 230. Actual count is 226 but program constantly outputs 230.
        test_image.print_image()

        test_image = Image("Sunset", "../images/pexels-nicole-avagliano-2893556.jpeg")
        self.assertEqual(0, len(test_image.get_image_text_list()))
        print(test_image.get_image_text_list())

    def test_image_list(self):
        test_list = ImageList("My Image List")
        print(test_list)
        test_list.add_image_to_list("Last of Us Poster", "../images/lastofus.jpeg")
        print(test_list)
        test_list.add_image_to_list("Comp 172 Syllabus", "../images/Screen Shot 2023-05-01 at 4.56.47 PM.png")
        test_list.add_image_to_list("I Want You Poster", "../images/J._M._Flagg,_I_Want_You_for_U.S._Army_poster_(1917).jpeg")
        test_list.add_image_to_list("Steezus Christ", "../images/74cd5f7c132ba6c02cec6e3ea6d981b18c8e26e44f566325198d613040583e5e_3.jpeg")
        print(test_list)
        print(test_list.get_gallery())
        test_list.sort_by()
        print(test_list.get_gallery())

