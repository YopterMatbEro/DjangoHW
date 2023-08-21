import json

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Путь к файлу JSON')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r', encoding='utf-8') as f:
            books = json.load(f)

        for book in books:
            # created=False - запись присутствует /True - отсутствует
            book_obj, created = Book.objects.get_or_create(
                id=book['pk'],
                name=book['fields']['name'],
                author=book['fields']['author'],
                pub_date=book['fields']['pub_date']
            )

            if not created:
                # Обновляем существующую запись
                book_obj.id = book['pk']
                book_obj.name = book['fields']['name']
                book_obj.author = book['fields']['author']
                book_obj.pub_date = book['fields']['pub_date']
                book_obj.save()
