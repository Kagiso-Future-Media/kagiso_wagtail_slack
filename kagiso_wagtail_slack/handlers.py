import json

from bs4 import BeautifulSoup
import requests
from wagtail.wagtailcore.signals import page_published


def send_to_slack(sender, **kwargs):
    instance = kwargs['instance']
    webhook_url = 'https://hooks.slack.com/services/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'  # noqa
    payload = {
        'text': '{0} was published by {1}'.format(
            instance.title,
            instance.owner.username
        ),
        'attachments': [
            {
                'title': instance.title,
                'title_link': instance.url,
                'text': BeautifulSoup(instance.summary, 'html5lib').getText()
            }
        ]
    }

    if instance.cover_image:
        payload['attachments'][0]['image_url'] = instance.cover_image.get_rendition('fill-100x100').url
    r = requests.post(webhook_url, data=json.dumps(payload))
    print(r.status_code)


page_published.connect(send_to_slack)
