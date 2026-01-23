"""
Comando Django para aguardar até que o banco de dados esteja disponível.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comando Django para aguardar o banco de dados."""

    def handle(self, *args, **options):
        """Ponto de entrada para comando."""
        self.stdout.write('Aguardando banco de dados...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Banco de dados indisponível, aguardando 1 segundo...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Banco de dados disponível!'))

