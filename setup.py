from setuptools import setup, find_packages

setup(
    name='clean_panda',
    version='0.1.0',
    description='A package for handling various data preprocessing tasks',
    author='asimtarik & emirs',
    author_email='support@cleanpanda.com',
    url='https://github.com/EmirhanSyl/CinemaConsult',  # Replace with your GitHub repository URL
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)