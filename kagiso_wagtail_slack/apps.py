from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'kagiso_wagtail_slack'
    verbose_name = 'Kagiso Wagtail Slack'

    def ready(self):
        from . import handlers  # noqa
