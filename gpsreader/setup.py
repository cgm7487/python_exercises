from setuptools import setup, find_packages

REQUIREMENTS = ['pyserial']

setup(name='gpsreader',
      author = "cgm",
      author_email = "cgm7487@gmail.com",
      version = '1.0',
      packages=find_packages(),
      install_requires=REQUIREMENTS
      )
