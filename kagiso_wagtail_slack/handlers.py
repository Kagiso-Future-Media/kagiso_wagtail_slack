import json
import logging

from bs4 import BeautifulSoup
from django.conf import settings
from raven.contrib.django.raven_compat.models import client as sentry
import requests
from requests.exceptions import RequestException
from wagtail.wagtailcore.signals import page_published


logger = logging.getLogger('django')


def send_to_slack(sender, **kwargs):
    instance = kwargs['instance']
    webhook_url = settings.SLACK_PAGE_PUBLISHED_WEBHOOK
    payload = {
        'text': '{0} was published.'.format(instance.title),
        'attachments': [
            {
                'title': instance.title,
                'title_link': instance.url,
                'text': BeautifulSoup(instance.summary, 'html5lib').getText()
            }
        ]
    }

    if instance.getattr('cover_image', None):
        payload['attachments'][0]['image_url'] = instance.cover_image.get_rendition('fill-100x100').url  # noqa
    timeout_seconds = 3

    try:
        r = requests.post(
            webhook_url,
            data=json.dumps(payload),
            timeout=timeout_seconds
        )
        logger.info('%s published to Slack, status %s', instance.title, r.status_code)  # noqa
    except RequestException as e:
        logger.error(e)
        sentry.captureException()


page_published.connect(send_to_slack)
