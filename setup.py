"""The setup module for django_saml2_auth.
See:
https://github.com/fangli/django_saml2_auth
"""

from codecs import open
from setuptools import (setup, find_packages)
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django_saml2_auth_lw',
    description='Django SAML2 Authentication Made Easy. Easily integrate with SAML2 SSO identity providers like Okta',
    long_description=long_description,
    long_description_content_type='text/markdown',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    url='https://github.com/Lotterywest/django-saml2-auth-lw',

    author='Fang Li, Lotterywest GoRillas Team',
    author_email='surivlee+djsaml2auth@gmail.com, Gorillas@lotterywest.wa.gov.au',

    license='Apache 2.0',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    keywords='Django SAML2 Authentication Made Easy, integrate with SAML2 SSO such as Okta easily',

    packages=find_packages(),

    install_requires=['pysaml2>=4.5.0',
                      'drf-jwt'],
    include_package_data=True,
)
