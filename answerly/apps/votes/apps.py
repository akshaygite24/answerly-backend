from django.apps import AppConfig


class VotesConfig(AppConfig):
    name = 'apps.votes'


    def ready(self):
        import apps.votes.signals