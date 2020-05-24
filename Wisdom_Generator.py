from bs4 import BeautifulSoup
import requests


def get_wisdom(count=1, stopwords=None):

    if stopwords is None:
        stopwords = ['physics', 'womb', 'god', 'boson']

    url = "http://wisdomofchopra.com/iframe.php#"
    quotes = []

    while len(quotes) < count:
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        quote = soup.find('h2')
        quote = quote.text.strip().replace('"', '')
        for word in stopwords:
            if word in quote.lower():
                break
        quotes.append(quote)

    return quotes


if __name__ == "__main__":

    quotes = get_wisdom(20)
    for q in quotes:
        print(q)