from django.core.management.base import BaseCommand
from channel.bot import bot

class Command(BaseCommand):
    help = 'Run the Discord bot'

    def handle(self, *args, **kwargs):
        bot.run()
