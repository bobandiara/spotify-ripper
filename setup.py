#!/usr/bin/python3
# coding=utf-8

from setuptools import setup, find_packages
import os


def create_default_dir():
    default_dir = os.path.normpath(os.path.realpath((os.path.join(os.path.expanduser("~"), ".spotify-ripper"))))
    if not os.path.exists(default_dir):
        print("Creating default settings directory: " + default_dir)
        os.makedirs(default_dir.encode("utf-8"))

def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(
    name='spotify-ripper',
    version='2.18',
    packages=find_packages(exclude=["tests"]),
    #scripts=['spotify_ripper/main.py'],
    include_package_data=True,
    zip_safe=False,

    # Executable
    entry_points={
        'console_scripts': [
            'spotify-ripper = spotify_ripper.main:main',
        ],
    },

    # Additional data
    package_data={
        '': ['README.md', 'LICENSE']
    },

    # Requirements
    install_requires=[
        'pyspotify>=2.0.5',
        'colorama>=0.3.3',
        'mutagen>=1.30',
        'requests>=2.13.0',
        'schedule>=0.3.1',
        'spotipy>=2.4.4'
    ],

    # Metadata
    author='Simone Caronni',
    author_email='negativo17@gmail.com',
    description='A small ripper for Spotify that rips Spotify URIs to media files',
    license='MIT',
    keywords="spotify ripper mp3 ogg vorbis flac opus acc mp4 m4a",
    url='https://github.com/scaronni/spotify-ripper',
    download_url='https://github.com/scaronni/spotify-ripper/tarball/2.15',
    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ],
)

create_default_dir()
