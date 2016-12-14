from setuptools import setup, find_packages

setup(
    name='shacknami',
    version='0.0.1',
    packages=find_packages(),
    scripts=[],

    install_requires=[
        'pyvit>=0.1.0'
    ],

    test_suite='test',

    author='syntroniks',
    author_email='syntroniks@gmail.com',
    url='http://github.com/ulabs-sgiroux/shacknami',
    license='GPLv3',
    description='Shacknami vehicle interface experiments',
    long_description=open('README.rst').read(),
    classifiers=['Development Status :: 0 - Pre-Alpha',
                 ('License :: OSI Approved :: ' +
                  'GNU General Public License v3 (GPLv3)'),
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Software Development :: Embedded Systems']
)
