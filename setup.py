#!/usr/bin/env python
from distutils.core import setup


setup(
    name='wagtail_embed_videos',
    version='0.0.5',
    description='Embed Videos for Wagtail CMS.',
    long_description=README,
    author='Diogo Marques',
    author_email='doriva.marques.29@gmail.com',
    maintainer='Diogo Marques',
    maintainer_email='doriva.marques.29@gmail.com',
    url='https://github.com/infoportugal/wagtail-embedvideos',
    packages=['wagtail_embed_videos', 'wagtail_embed_videos.views'],
    package_data={'wagtail_embed_videos': ['static/wagtail_embed_videos/js/*.js']},
    requires=['django(>=1.7)', 'wagtail(>=1.0)', 'django-embed-video(>=1.0)'],
    install_requires=['wagtail', 'django-embed-video'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Framework :: Wagtail CMS',
        'License :: OSI Approved :: BSD License'],
    license='New BSD',

)
