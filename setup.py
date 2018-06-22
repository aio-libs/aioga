import io
import os
import re

from setuptools import setup


def get_version():
    regex = r"__version__\s=\s\'(?P<version>[\d\.]+?)\'"

    path = ('aioga', '__init__.py')

    return re.search(regex, read(*path)).group('version')


def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


setup(
    name='aioga',
    version=get_version(),
    author='wikibusiness',
    author_email='osf@wikibusiness.org',
    url='https://github.com/aio-libs/aioga',
    description='Google Analytics client for asyncio',
    long_description=read('README.rst'),
    install_requires=[
        'aiohttp>=3.0.0',
        'async-timeout',
        'yarl',
    ],
    python_requires='>=3.5.3',
    packages=['aioga'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=[
        'google analytics',
        'measurement protocol',
        'asyncio',
        'aiohttp',
    ],
)
