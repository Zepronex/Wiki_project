from django.apps import AppConfig

class WikiAppConfig(AppConfig):  # Renamed from WikiConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wiki_app'  # Must match the app directory name