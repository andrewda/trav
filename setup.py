from setuptools import setup, find_packages


setup(
    name='trav',
    version='0.0.1',
    description='A package to access Travis CI environment variables',
    author='Andrew Dassonville',
    author_email='dassonville.andrew@gmail.com',
    url='https://github.com/andrewda/trav',
    keywords = ['frc', 'score', 'robotics'],
    license='MIT',
    packages=find_packages(exclude=('tests')),
)
