from setuptools import setup, find_packages


version = '0.1'

setup(
    name='ckanext-svvlayout',
    version='0.1',

    description='''Grafisk tilpasning for Statens vegvesen.''',
    long_description='''Contributors: 
    Trond Smaavik <trond.smaavik@vegvesen.no>
    and Jørgen Abrahamsen <jorgen.abrahamsen@gmail.com>
    ''',
    url='https://github.com/svv-its/ckanext-svvlayout',
    author='Hilde Austlid',
    author_email='hilde.austlid@vegvesen.no',
    license='',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='CKAN SVV CSS layout',
    namespace_packages=['ckanext'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    include_package_data=True,
    entry_points='''
        [ckan.plugins]
        svvlayout=ckanext.svvlayout.plugin:SvvLayoutPlugin
    ''',
)
