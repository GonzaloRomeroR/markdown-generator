from setuptools import setup, find_packages

setup(name='markdownWriter',
      version='0.1',
      url='https://github.com/',
      license='MIT',
      author='Gonzalo Romero',
      author_email='gonzaromero2007@gmail.com',
      description='Markdown Writer',
      #packages=find_packages(exclude=['tests']),
      packages=find_packages('markdownWriter'),                   #Packages to import
      long_description=open('README.md').read(),
      package_data={
        '': ['*.txt'],
      },
      setup_requires=[''],
      zip_safe=False
      )
