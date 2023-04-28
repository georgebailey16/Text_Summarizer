import image_to_text
import requests
import json
from image import Image


def main():
    gettysburg = Image("Gettysburg Address", 'images/Gettysburg_Address_(poster).jpeg')

    print(gettysburg.get_image_text())


main()
