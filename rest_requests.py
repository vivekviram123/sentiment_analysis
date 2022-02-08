import requests

query = {'text':'i dont like this comment'}
response = requests.get('http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())

# r = requests.post('http://127.0.0.1:8000/sentiment_analysis/', data = {'key':'value'})