from setuptools import setup
from os import path

import latest

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='latest',
    version=latest.__version__,
    description='A LaTeX-oriented template engine.',
    long_description=long_description,
    author='Flavio Grandin',
    author_email='flavio.grandin@gmail.com',
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    install_requires=[
        'pyyaml',
    ],
    include_package_data=True,
    license='MIT',
    url='https://github.com/bluePhlavio/latest',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        ],
    keywords='latex template engine',
    packages=['latest'],
    entry_points={
        'console_scripts': ['latest=latest.__main__:main'],
    },
)


