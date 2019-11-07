import ast
import os
import re
from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))
_version_re = re.compile(r'__version__\s+=\s+(?P<version>.*)')

with open(os.path.join(current_dir, 'deps.py'), 'r') as f:
    version = _version_re.search(f.read()).group('version')
    version = str(ast.literal_eval(version))


setup(
    name='deps',
    license='MIT',
    version=version,
    description='Dependency injection based on attrs',
    long_description=open('README.rst').read(),
    author='Daniel Kuruc',
    author_email='daniel@kuruc.dev',
    url='https://github.com/danie1k/deps',
    py_modules=[
        'deps',
    ],
    zip_safe=False,
    python_requires='>=3.6',
    tests_require=['pytest'],
    install_requires=[
        'attrs < 19.4',
        'Inject < 3.6',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
