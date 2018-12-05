from os.path import abspath, dirname, join, normpath
from setuptools import setup

setup(
    name='maclookup-cli',
    version='0.1.8',
    license='MIT',
    packages=['maclookupcli', 'maclookupcli.errors'],
    package_dir={
        'maclookupcli': 'maclookupcli',
        'maclookupcli.errors': 'maclookupcli/errors',
    },
    include_package_data=True,
    install_requires=[
        'click',
        'maclookup',
    ],
    entry_points='''
        [console_scripts]
        maclookup=maclookupcli.command:cli
    ''',
    description='Console tool to make a MAC vendor lookups',
    long_description=open(normpath(join(dirname(abspath(__file__)), "DESCRIPTION.rst"))).read(),
    author='CodeLine OY',
    author_email='support@macaddress.io',
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    url='https://github.com/CodeLineFi/maclookup-cli',
)
