import requests
import json


def image_to_json(image_file):
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    with open(image_file, 'rb') as image_file_descriptor:
        files = {'image': image_file_descriptor}
        r = requests.post(api_url, files=files, headers={'X-Api-Key': 'qzxHLFBxoKXQDcfA8RowVQ==bhFZlshUidUT3Vbf'})

    return r.json()


def image_to_text(image_file):
    text_list = []
    image_json_text = image_to_json(image_file)
    for word in image_json_text:
        text_list.append(word['text'])

    return text_list

