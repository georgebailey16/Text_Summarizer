from datetime import datetime


class ImageList:

    def __init__(self, list_name):
        self.name = list_name
        self.list = []

    def _length(self):
        num_of_images = len(self.list)
        return num_of_images

    def add_image_to_list(self, image):
        """
        :param image: Image object
        """
        if image not in self.list:
            self.list.append(image)
        else:
            print("Image already contained in " + str(self.name))

    def sort_by(self, sort_param):
        direction = input("Ascending or Descending?: ").lower()
        sort_param()
        if direction == "descending":
            self.list.reverse()

    def time(self):
        self.list.sort(key=lambda x: datetime.strptime(x.upload_time, '%m/%d/%Y %I:%M %p'))

    def text_length(self):
        self.list.sort(key=lambda x: x.num_words)

    def name(self):
        self.list.sort(key=lambda x: x.image_name)