import os
from setuptools import setup, find_packages
from lfs_order_numbers import __version__

version = __version__
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()

setup(
    name="lfs-order-numbers",
    version=version,
    description="",
    long_description=README,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords="django e-commerce online-shop",
    author="Kai Diefenbach",
    author_email="kai.diefenbach@iqpp.de",
    url="http://www.getlfs.com",
    license="BSD",
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    zip_safe=False,
    dependency_links=["http://pypi.iqpp.de/"],
    install_requires=[
        "setuptools",
    ],
)
