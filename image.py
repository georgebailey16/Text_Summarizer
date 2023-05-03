from image_to_text import image_to_text
from datetime import datetime
from PIL import Image as PILImage
from text_summarizer import summarize


class Image:
    def __init__(self, image_name, image_file):
        self.image_file = image_file
        self.image_name = image_name
        self.image_text = image_to_text(image_file)
        self.num_words = len(self.image_text)
        self.text_summary = summarize(self.image_file)
        self.upload_time = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return "Image " + str(self.image_name) + " has " + str(self.num_words) + " words."

    def get_image_text(self):
        """
        :return: self.image_text
        """
        return self.image_text

    def get_num_words(self):
        """
        :return: self.num_words
         """
        return self.num_words

    def get_text_summary(self):
        """
        :return: self.text_summary
        """
        return self.text_summary

    def print_image(self):
        """
        :post: uses PIL Image Library to open the image in a new window
        """
        with PILImage.open(self.image_file) as im:
            im.show()
