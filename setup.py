from setuptools import setup, find_packages
from src.logger.logger import __version__


# read requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='logging',
    version=__version__,
    packages=find_packages(),
    author='Klaus Moser',
    author_email='60796711+klaus-moser@users.noreply.github.com',
    description='Packet for a standardized logger.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/klaus-moser/logging',
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
