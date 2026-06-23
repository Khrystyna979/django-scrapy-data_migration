from models import Author, Quote
import json

authors_file = 'authors.json'
quotes_file = 'quotes.json'

def load_data():
    with open(authors_file, 'r', encoding='utf-8') as af:
        data = json.load(af)
        for item in data:
            author = Author(**item) # unpack the dictionary into an object
            author.save()

    with open(quotes_file, 'r', encoding='utf-8') as qf:
        data = json.load(qf)
        for item in data:
            author_fullname = item.get('author')
            author = Author.objects(fullname=author_fullname).first() # searching for the author in the database

            if author:
                quote = Quote(
                        tags=item.get('tags'),
                        quote=item.get('quote'),
                        author=author
                    )
                quote.save()

if __name__ == '__main__':
    load_data()