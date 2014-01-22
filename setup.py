#!/usr/bin/env python

import sys
import os
from os.path import join, dirname
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.argv[-1] in ("submit", "publish"):
    os.system("python setup.py sdist upload")
    sys.exit()

packages = []
requires = []

conditional_dependencies = {
    "colorama>=0.2.5": "win32" in sys.platform,
}

base_dir = os.path.dirname(os.path.abspath(__file__))
def get_version(filename="todo/__init__.py"):
    with open(os.path.join(base_dir, filename)) as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)

setup(
    name = "wmtodo",
    version = get_version(),
    description = "Python version of Gina Trapani's popular bash script to manage your todo list.",
    long_description = "\n\n".join([open(join(dirname(__file__), "README.rst")).read(), open(join(dirname(__file__),"HISTORY.rst")).read()]),
    author = "graffatcolmingov",
    author_email = "graffatcolmingov@gmail.com",
    url = "https://github.com/MinchinWeb/Todo.txt-python",
	packages = find_packages(),
    #package_data={'': ['LICENSE']},
	#data_files=[('', ['README.rst', 'LICENSE', 'HISTORY.rst',])],
	include_package_data = True,
	    extras_require = {
        "git": "GitPython>=0.3.2.RC1"
    },
    install_requires = [
        ] + [p for p, cond in conditional_dependencies.items() if cond],
    classifiers = (
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        ),
    #scripts=["todo/todo.py"],
    entry_points = {
        'console_scripts': [
            'todo = todo.cli:run',
        ],
    },
)
