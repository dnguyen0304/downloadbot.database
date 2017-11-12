#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'downloadbot_cache'

    description = 'An event handler that writes to cache.'

    install_requires = [
        # This package is needed by the application layer to implement
        # event sources.
        'downloadbot_common==0.1.0',
        # This package is needed by the application layer to implement
        # repositories that synchronize with caches.
        'redis==2.10.6']
    dependency_links = [
        'git+https://github.com/dnguyen0304/downloadbot_common.git@v0.1.0#egg=downloadbot_common-0.1.0']

    setuptools.setup(name=package_name,
                     version='0.1.0',
                     description=description,
                     url='https://github.com/dnguyen0304/downloadbot_cache.git',
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     classifiers=['Programming Language :: Python :: 3.5'],
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     install_requires=install_requires,
                     dependency_links=dependency_links,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
