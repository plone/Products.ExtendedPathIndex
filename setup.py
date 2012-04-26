from setuptools import setup, find_packages

version = '3.0'

setup(name='Products.ExtendedPathIndex',
      version=version,
      description="Zope catalog index for paths",
      long_description=open("README.txt").read() + "\n" + \
                       open("CHANGES.txt").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='Zope catalog index',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/Products.ExtendedPathIndex',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'AccessControl',
          'transaction',
          'ZODB3',
          'Zope2 >= 2.13.0a3',
      ],
      )
