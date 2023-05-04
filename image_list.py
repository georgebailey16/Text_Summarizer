from datetime import datetime
from image import Image


class ImageList:

    def __init__(self, list_name):
        self.name = list_name
        self.gallery = {}

    def __str__(self):
        return self.name + " is an Image List containing " + str(len(self.gallery)) + " images."

    def _length(self):
        return len(self.gallery)

    def get_gallery(self):
        return self.gallery

    def add_image_to_list(self, image_name, image_file):
        """
        :param image_file: is a file of an image
        """
        '''
        if image not in self.list:
            self.list.append(image)
        else:
            print("Image already contained in " + str(self.name))
        '''
        self.gallery[image_name] = Image(image_name, image_file)

    def sort_by(self):
        direction = input("Ascending or Descending?: ").lower()
        my_keys = list(self.gallery.keys())
        my_keys.sort()
        if direction == "descending":
            my_keys.reverse()
        self.gallery = {i: self.gallery[i] for i in my_keys}
