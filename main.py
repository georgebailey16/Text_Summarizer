import image_to_text
import requests
import json
from image import Image
from text_summarizer import summarize


def main():
    gettysburg = Image("Gettysburg Address", 'images/Gettysburg_Address_(poster).jpeg')
    print(gettysburg.get_image_text())

    cheese_meme = Image("Cheese Meme", "images/FBb9ymGWUAEymnf.jpeg")
    print(cheese_meme.get_image_text())


main()
