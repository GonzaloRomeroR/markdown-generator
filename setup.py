from setuptools import setup, find_packages

setup(name='markdownWriter',
      version='0.1',
      url='https://github.com/',
      license='MIT',
      author='Gonzalo Romero',
      author_email='gonzaromero2007@gmail.com',
      description='Markdown Writer',
      packages=find_packages(exclude=['tests']),
      #packages=find_packages('markdownWriter'),
      long_description=open('README.md').read(),
      zip_safe=False
      )
