import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # print(phone)
            # TODO: Добавьте сохранение модели
            # created=False - запись присутствует /True - отсутствует
            phone_obj, created = Phone.objects.get_or_create(
                id=phone['id'],
                defaults={
                    'name': phone['name'],
                    'image': phone['image'],
                    'price': phone['price'],
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'],
                }
            )

            if not created:
                # Обновляем существующую запись
                phone_obj.name = phone['name']
                phone_obj.image = phone['image']
                phone_obj.price = phone['price']
                phone_obj.release_date = phone['release_date']
                phone_obj.lte_exists = phone['lte_exists']
                phone_obj.save()
