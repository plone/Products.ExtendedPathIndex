from setuptools import setup, find_packages
import os

version = '2.4'

setup(name='Products.ExtendedPathIndex',
      version=version,
      description="Zope catalog index for paths",
      long_description=open("README.txt").read() + "\n" + \
              open(os.path.join("docs", "HiSTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        ],
      keywords='Zope catalog index',
      author='Helge Tesdal',
      author_email='plone-developers@lists.sourceforge.net',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
