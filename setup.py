from setuptools import setup, find_packages

version = '4.0.0'

setup(
    name='Products.ExtendedPathIndex',
    version=version,
    description="Zope catalog index for paths",
    long_description=(
        open("README.rst").read() +
        "\n" +
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: Core",
        "Framework :: Plone :: 6.0",
        "Framework :: Zope",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords='Zope catalog index',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://github.com/plone/Products.ExtendedPathIndex',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'six',
        'Zope',
    ],
)
