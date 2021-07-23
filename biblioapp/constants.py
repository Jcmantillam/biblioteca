from datetime import date

SERVICE_CHOICES = (
        ('G', 'Google'),
        ('O', 'Oreilly'),
    )

last_day_of_year = date(date.today().year, 12, 31)

local_save_book = 'http://localhost:8000/api/v1/save_book/?book_id'

local_api_service = 'http://localhost:8000/api/v1/search_book_local/?search='

google_api_service = 'https://www.googleapis.com/books/v1/volumes?q='
get_google_book = 'https://www.googleapis.com/books/v1/volumes/'

oreilly_api_service = 'https://learning.oreilly.com/api/v2/search/?query='
get_oreilly_book = 'https://learning.oreilly.com/api/v1/book/'
