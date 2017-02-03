from setuptools import find_packages, setup


setup(
    name='kagiso_wagtail_slack',
    version='2.0.0',
    author='Kagiso Media',
    author_email='development@kagiso.io',
    description='Kagiso Wagtail Slack',
    url='https://github.com/Kagiso-Future-Media/kagiso_wagtail_slack',
    packages=find_packages(),
    install_requires=[
        'wagtail>=1.8.0',
    ]
)
