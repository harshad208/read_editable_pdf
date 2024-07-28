from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read the requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='read_editable_pdf',
    version='1.0.0',
    author='Harshad Yadav',
    author_email='harshadyadav20@gmail.com',
    description='A package to read editable PDFs and extract text with coordinates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourproject',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
