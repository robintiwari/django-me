from setuptools import setup, find_packages

import djangome


setup(name='djangome',
      packages = find_packages(),
      version=djangome.__version__,
      description=djangome.__doc__,
      author=djangome.__author__,
      url='https://github.com/nixdaemon/django-me',
      license=djangome.__license__,
      include_package_data=True,
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: Jython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Django Mongoengine Integration',
      ],
      keywords = ['django', 'mongoengine',],
      )
