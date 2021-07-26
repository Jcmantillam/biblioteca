import datetime
import json
import requests
from rest_framework.authtoken.models import Token
from .constants import SERVICE_CHOICES
from .models import Editor, Category, Author, Book
from .constants import local_api_service, google_api_service, get_google_book, get_oreilly_book, oreilly_api_service, local_save_book


def API_request(search, option, auth=None):
    if option == "local":
        url = local_api_service + search

        headers = {
            'Authorization': 'Token  {}'.format(auth)
        }
        r = requests.request("GET", url, headers=headers, data={})
        data = r.json()

        if data: 
            data[0]['service'] = option
        return data
    elif option == SERVICE_CHOICES[0][0]:
        service = google_api_service + search + '&maxResults=1'
        r = requests.get(service)
        data = r.json()
        data['service'] = option
        key =  'id'
        method = local_save_book + '_g='
        data['items'] = add_save_method(data['items'], method, key)
        return data
    
    elif option == SERVICE_CHOICES[1][0]:
        service = oreilly_api_service + search
        r = requests.get(service)
        data = r.json()
        data['service'] = option
        key = 'archive_id'
        method = local_save_book + '_o='
        data['results'] = add_save_method(data['results'], method, key)
        return data


def get_book_by_id(id, service):
    if service == SERVICE_CHOICES[0][0]:
        service = get_google_book + id
        print(service)
    elif service == SERVICE_CHOICES[1][0]:
        service = get_oreilly_book + id
    r = requests.get(service)
    data = r.json()
    return data


def add_save_method(books, method, key):
    items = []
    for book in books:
        book['save_link'] = method + book[key]
        items.append(book)
    return items


def save_book(data, option):
    if option == SERVICE_CHOICES[0][0]:
        title = data["volumeInfo"]["title"]

        try:
            subtitle = data["volumeInfo"]["subtitle"]
        except:
            subtitle = title

        try:
            description = data["volumeInfo"]["description"]
        except:
            description = "Not found"

        try:
            image = data["volumeInfo"]["imageLinks"]["thumbnail"]
        except:
            image = None

        date_str = data["volumeInfo"]["publishedDate"]
        editor_name = data["volumeInfo"]["publisher"]
        authors_name = data["volumeInfo"]["authors"]
        try:
            categories_name = data["volumeInfo"]["categories"]
        except:
            categories_name = ["No registrado"]

    elif option == SERVICE_CHOICES[1][0]:
        title = data["title"]
        subtitle = data["title"]
        description = data["description"]
        image = data["cover"]
        date_str = data["issued"]
        editor_name = data["publishers"][0]["name"]
        authors_name = [author['name'] for author in data["authors"]]
        categories_name = [topic['name'] for topic in data["topics"]]

    book_querty = Book.objects.filter(title=title)
    if book_querty:
        raise Exception("Title already exists")
    
    
    editor_querty = Editor.objects.filter(name=editor_name)
    if editor_querty:
        editor = editor_querty.first()
    else:
        editor = Editor.objects.create(name=editor_name)

    authors = []
    for author_name in authors_name:
        author = Author.objects.filter(name=author_name)

        if author:
            authors.append(author.first())
        else:
            author = Author.objects.create(name=author_name)
            authors.append(author)
    
    categories = []
    for category_name in categories_name:
        category = Category.objects.filter(name=category_name)
        
        if category:
            categories.append(category.first())
        else:
            category = Category.objects.create(name=category_name)
            categories.append(category)

    book = Book.objects.create(
        title=title,
        subtitle=subtitle,
        release_date=convert_str_to_date(date_str),
        image=image,
        editor=editor,
        description=description
    )
    book.authors.set(authors)
    book.categories.set(categories)

    return book


def convert_str_to_date(date_str):
    if len(date_str.split('-')) == 1:
        date_str = date_str + '-01-01'
    elif len(date_str.split('-')) == 2:
        date_str = date_str + '-01'
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    print('Date:', date_obj.date())
    return date_str
