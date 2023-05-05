class ImageList:

    def __init__(self, list_name):
        self.name = list_name
        self.gallery = {}

    def __str__(self):
        return self.name + " is an Image List containing " + str(len(self.gallery)) + " images."

    def _length(self):
        return len(self.gallery)

    def get_list_name(self):
        return self.name

    def get_gallery(self):
        return self.gallery

    def add_image_to_list(self, image):
        """
        :param image: is an Image object
        """
        if image.get_image_name() not in self.gallery:
            self.gallery[image.get_image_name()] = image
        else:
            print("Image already contained in " + str(self.name))

    def sort_by(self):
        my_keys = list(self.gallery.keys())
        my_keys.sort()
        self.gallery = {i: self.gallery[i] for i in my_keys}
