"""setup.py controls the build, testing, and distribution of the egg"""

from setuptools import setup, find_packages
import re
import os.path
from glob import glob



def get_version():
    """Reads the version from the package"""
    return "0.2"

def get_requirements():
    """Reads the installation requirements from requirements.pip"""
    with open("requirements.txt") as handle:
        return [line.rstrip() for line in handle if not line.startswith("#")]


setup(
    name='linux_binary',
    version=get_version(),
    description="Description.",
    long_description="""\
""",
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='',
    packages=find_packages(),
    # packages=["src", ],
    # package_dir={'': '.', },
    author='Hugh Brown',
    author_email='hughdbrown@yahoo.com',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    scripts=glob('scripts/*'),
    install_requires=get_requirements(),
)
