import requests

a = requests.get('https://docs.google.com/document/d/1p6EyqG8QVPL8uKBlLjMv9a5rczhRnyaB5j8tWHmuRlg/edit')

message = a.text[a.text.find('<meta property="og:description" content="')+41:a.text.find('"><meta name="google" content="notranslate">')]

# print(message)