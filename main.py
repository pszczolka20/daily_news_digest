import requests
from send_email import send_email
from datetime import date

# Returns the current local date
today = date.today()

topic = "tesla"
api_key = "f5565672f45941549e0815284bb43c9b"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from={today}&sortBy=publishedAt&apiKey=" \
      "f5565672f45941549e0815284bb43c9b&language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description

body = "Subject: Today's news" + "\n"
for article in content['articles'][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + \
               article['description'] + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(body)

