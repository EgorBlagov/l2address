from os import path

from setuptools import setup

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '1.0.1'

setup(
    name='l2address',
    packages=['l2address'],
    version=version,
    license='MIT',
    description='MAC address manipulation library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Egor Blagov',
    author_email='e.m.blagov@gmail.com',
    url='https://github.com/EgorBlagov/l2address',
    download_url='https://github.com/EgorBlagov/l2address/archive/v{}.tar.gz'.format(
        version),
    keywords=['Networking', 'Telecommunication', 'MAC', 'L2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
