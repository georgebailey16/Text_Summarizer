from datetime import datetime
from image import Image


class ImageList:

    def __init__(self, list_name):
        self.name = list_name
        self.list = []

    def __str__(self):
        return self.name + " is an Image List containing " + str(len(self.list)) + " images."

    def _length(self):
        return len(self.list)

    def get_image_list(self):
        return self.list

    def add_image_to_list(self, image_name, image_file):
        """
        :param image: Image object
        """
        '''
        if image not in self.list:
            self.list.append(image)
        else:
            print("Image already contained in " + str(self.name))
        '''
        self.list.append(Image(image_name, image_file))

    def sort_by(self, sort_param):
        direction = input("Ascending or Descending?: ").lower()
        sort_param()
        if direction == "descending":
            self.list.reverse()

    def time_uploaded(self):
        self.list.sort(key=lambda x: datetime.strptime(x.upload_time, '%m/%d/%Y %I:%M %p'))

    def original_text_length(self):
        self.list.sort(key=lambda x: x.num_words)

    def name_of_image(self):
        self.list.sort(key=lambda x: x.image_name)