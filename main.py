import requests

api_key = "f5565672f45941549e0815284bb43c9b"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-08-05&sortBy=publishedAt&apiKey=" \
      "f5565672f45941549e0815284bb43c9b"

#Make a request
request = requests.get(url)

#Get a dicttionary with data
content = request.json()

#Access the article titles and description
for article in content['articles']:
      print(article['title'])
      print(article['description'])

