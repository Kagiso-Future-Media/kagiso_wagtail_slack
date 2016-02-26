from setuptools import find_packages, setup


setup(
    name='kagiso_wagtail_sitemap',
    version='0.0.1',
    author='Kagiso Media',
    author_email='development@kagiso.io',
    description='Kagiso Search',
    url='https://github.com/Kagiso-Future-Media/kagiso_wagtail_sitemap',
    packages=find_packages(),
    install_requires=[
        'wagtail>=1.3.1',
    ]
)
