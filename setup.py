from setuptools import setup, find_packages
from app.logger import __version__


# read requirements.txt
with open('requirements.txt', "r") as f:
    requirements = f.read().splitlines()

# read description
with open('README.md', "r") as f:
    long_description = f.read()


setup(
    name='logging',
    version=__version__,
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    author='Klaus Moser',
    author_email='60796711+klaus-moser@users.noreply.github.com',
    description='Packet for a standardized logger.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/klaus-moser/logging',
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12'
)
