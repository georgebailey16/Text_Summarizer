import image_to_text
import requests
import json
from image import Image
from text_summarizer import summarize
from image_list import ImageList

def main():
    gettysburg = Image("Gettysburg Address", 'images/Gettysburg_Address_(poster).jpeg')
    cheese_meme = Image("Cheese Meme", "images/FBb9ymGWUAEymnf.jpeg")
    images = ImageList("test list")
    images.add_image_to_list(cheese_meme)
    images.add_image_to_list(gettysburg)

main()
