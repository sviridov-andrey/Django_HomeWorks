import json
from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        with open("data.json", 'r', encoding='cp1251') as file:
            data = json.load(file)

        category_list = []
        for item in data:
            category_list.append(Category(**item['fields']))

        try:
            Category.objects.all().delete()
        finally:
            Category.objects.bulk_create(category_list)
