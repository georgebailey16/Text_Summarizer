import requests


def image_to_json(image_file):
    """
    :param image_file: An image file
    :return: A JSON of the text contained in image_file
    """
    api_url = 'https://api.api-ninjas.com/v1/imagetotext'
    with open(image_file, 'rb') as image_file_descriptor:
        files = {'image': image_file_descriptor}
        r = requests.post(api_url, files=files, headers={'X-Api-Key': 'qzxHLFBxoKXQDcfA8RowVQ==bhFZlshUidUT3Vbf'})

    return r.json()


def image_to_text(image_file):
    """
    :param image_file: a JSON file of an image file
    :return: a list of the words contained in image_file, seperated from the JSON file
    """
    text_list = []
    image_json_text = image_to_json(image_file)
    for word in image_json_text:
        text_list.append(word['text'])

    return text_list

