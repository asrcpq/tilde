from setuptools import setup, find_packages

setup(name='tilde',
      version='0.1',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'tilde=tilde.main:main'
          ]
      }, install_requires=['problog', 'scikit-learn', 'pyswip'])
