import requests

api_url = 'https://api.api-ninjas.com/v1/imagetotext'
image_file_descriptor = open('images/74cd5f7c132ba6c02cec6e3ea6d981b18c8e26e44f566325198d613040583e5e_3.jpeg', 'rb')
files = {'image': image_file_descriptor}
r = requests.post(api_url, files=files, headers={'X-Api-Key': 'qzxHLFBxoKXQDcfA8RowVQ==bhFZlshUidUT3Vbf'})
print(r.json())