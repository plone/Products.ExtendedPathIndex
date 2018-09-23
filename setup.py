from setuptools import setup, find_packages

version = '3.3.1'

setup(
    name='Products.ExtendedPathIndex',
    version=version,
    description="Zope catalog index for paths",
    long_description=(open("README.rst").read() + "\n" + \
                      open("CHANGES.rst").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
      ],
    keywords='Zope catalog index',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.ExtendedPathIndex',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.ZCatalog',
        'six',
        'ZODB3',
        'Zope2 >= 2.13.0a3',
        'zope.interface',
    ],
    )
