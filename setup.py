from setuptools import setup, find_namespace_packages

setup(name='wingedsheep-carcassonne',
      version='1.0.3',
      description='Carcassonne implementation',
      author='Vincent Bons',
      url='https://github.com/wingedsheep/carcassonne',
      download_url='https://github.com/wingedsheep/carcassonne',
      license='MIT',
      install_requires=['numpy>=1.21.1',
                        'pillow>=8.3.1'],
      packages=find_namespace_packages(),
      package_data={"": ["*.png", "*.jpg"]})
