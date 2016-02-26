# kagiso_wagtail_sitemap
Postgres fulltext search for Wagtail

## Installation
`pip install kagiso_wagtail_sitemap`

Add `kagiso_wagtail_sitemap` to your `INSTALLED_APPS` in your `settings.py`.

`python manage.py migrate`

Add the following to `urls.py`:
```py
from kagiso_wagtail_sitemap.views import search as search_view

url(r'^search/', search_view, name='search'),
```
Make sure that there is a search template at
`kagiso_wagtail_sitemap/search_results.html` in your templates folder
(see a sample below).
