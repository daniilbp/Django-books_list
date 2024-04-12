from typing import Any
import random
from string import ascii_letters, digits

from django.core.management import BaseCommand

from .utils import info
from bookapp.models import Book, Profile

ALPHABET = ascii_letters + digits
columns = ['id', 'name', 'title', 'author', 'description', 'price']


class Command(BaseCommand):
    _class = Book
    name = 'BOOK'
    num_books: int = 10

    @info
    def handle(self, *args: Any, **options: Any) -> str | None:
        for i in range(self.num_books):
            Book.objects.get_or_create(
                name = f"Книга № {i + 1}",
                title = ''.join(random.choice(ALPHABET) for _ in range(10)),
                author = f"Автор - {''.join(random.choice(ALPHABET) for _ in range(5))}",
                description = ''.join(random.choice(ALPHABET) for _ in range(10)),
                price = int(f"{i + 1}{i}")
            )

        for col in columns:
            Profile.objects.get_or_create(
                column_name = col
            )
