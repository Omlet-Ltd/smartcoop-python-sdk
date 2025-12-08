from setuptools import setup, find_packages

setup(
    name='smartcoop_python_sdk',
    version='1.1.6',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Omlet',
    author_email='info@omlet.com',
    description='A Python SDK for the SmartCoop API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Omlet-Ltd/smartcoop-python-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
