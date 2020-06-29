from setuptools import setup

def readme():
    with open('README.md', encoding='utf8') as f:
        return f.read()

setup(name='owotext',
      version='1.0.3',
      description='A Python library for converting text strings into OwO',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/DerpyChap/owotext',
      author='DerpyChap',
      author_email='holla@derpychap.co.uk',
      license='MIT',
      packages=['owotext'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'owo = owotext.owo:main'
          ]
      })
