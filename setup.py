from setuptools import find_packages, setup


setup(
    name='kagiso_wagtail_slack',
    version='0.0.1',
    author='Kagiso Media',
    author_email='development@kagiso.io',
    description='Kagiso Wagtail Slack',
    url='https://github.com/Kagiso-Future-Media/kagiso_wagtail_slack',
    packages=find_packages(),
    install_requires=[
        'wagtail>=1.3.1',
    ]
)
