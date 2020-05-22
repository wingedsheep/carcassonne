from setuptools import setup, find_namespace_packages

setup(name='wingedsheep-carcassonne',
      version='1.0.0',
      description='Carcassonne implementation',
      author='Vincent Bons',
      url='https://github.com/wingedsheep/carcassonne',
      download_url='https://github.com/wingedsheep/carcassonne',
      license='MIT',
      install_requires=['numpy>=1.18.1',
                        'pillow>=7.1.2'],
      packages=find_namespace_packages(),
      package_data={"": ["*.png", "*.jpg"]})
