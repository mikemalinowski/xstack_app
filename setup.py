import os
import setuptools

if os.path.exists('README.md'):
    with open('README.md', 'r') as fh:
        long_description = fh.read()

else:
    long_description = 'A python package exposing the class composition design pattern'

setuptools.setup(
    name='xstack_app',
    version='1.0.1',
    author='Mike Malinowski',
    author_email='mike.external@outlook.com',
    description='xstack_app is a Qt based app to visualise the xstack library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/xstack_app',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "xstack",
        "qt.py",
        "scribble",
        "qtility",
    ],
    keywords="xstack",
)
