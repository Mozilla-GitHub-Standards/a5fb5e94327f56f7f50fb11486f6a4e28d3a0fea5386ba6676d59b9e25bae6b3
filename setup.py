""" Setup file.
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README')) as f:
    README = f.read()


setup(name='signing',
    version=0.1,
    description="Application receipt certifier and verifier",
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
    keywords="web services",
    author='Ryan Tilder',
    author_email="service-dev@mozilla.com",
    url="http://mozilla.org",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['cornice', 'PasteScript'],
    entry_points = """\
    [paste.app_factory]
    main = signing:main
    [console_scripts]
    check_keys = signing.scripts:check_keys
    certifier = signing.scripts:certifier
    """,
    paster_plugins=['pyramid'],
)
