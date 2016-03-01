# kagiso_wagtail_slack
Notify Slack via a web hook when a page has been published

## Installation
`pip install kagiso_wagtail_slack`

Add your Slack webhook as `SLACK_PAGE_PUBLISHED_WEBHOOK` in your settings.py

Add `kagiso_wagtail_slack.apps.KagisoWagtailSlackConfig` to your `INSTALLED_APPS` in your `settings.py`.

