from django.apps import AppConfig


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

# l4-6, make sure PostConfig and post is the same in settings.py
# otherwise you will get an error