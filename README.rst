wm_todo
=======

Note: Depreciated
-----------------

**Please note that this project is no longer maintained, as I hit the limits of what it could do, and have moved to** `topydo <https://github.com/bram85/topydo>`_, **which is a more powerful implementation of similiar functionalitiy.**

--- End Note ---


.. image:: https://secure.travis-ci.org/MinchinWeb/Todo.txt-python.png?branch=development
    :alt: Build Status
    :target: http://travis-ci.org/MinchinWeb/Todo.txt-python

A port of the `popular todo.txt-cli project
<https://github.com/ginatrapani/todo.txt-cli>`_ to Python.

Information About This Branch
-----------------------------

This is my main development branch.

Dependencies
------------

This only requires GitPython_ if you want to have todo.py also manage a git
repository which tracks the related files. Running the script once will give
you the URL to download it. Please note that GitPython is written for ``git
--version`` 1.7.2+.

If you're on Windows Coloram_ is required and provides support for colours
in the command line output.

.. _GitPython: https://github.com/gitpython-developers/GitPython
.. _Colorama: https://pypi.python.org/pypi/colorama

Installation
------------

From the repo
`````````````
Todo.py is designed to installed as is typical of Python packages. Download and
unzip/untar the repo, move to the base directory of the repo on your computer,
as at the command prompt, run

``python setup.py install``

This will install the program system-wide (as per your Python settings).


If you want to install the copy locally (i.e. to a personal directory) (Linux
and MacOS only) you can
simply download one of the packages_ and run the ``install.sh`` script.

.. _packages: https://github.com/MinchinWeb/Todo.txt-python/releases

Be sure to run ``./install.sh -h`` first. You can decide where you would like
the script installed (the default is ``$HOME/bin/``) and where you would like an
alias for the script, e.g., ``t`` or ``tpy``, written (the default is
``$HOME/.bashrc``).

Using pypi
``````````

(Note, this edition has not yet been uploaded to PyPi...)
If you would prefer a system-wide installation, you can use install ``wm_todo``
from PyPi like so:

::

    $ pip install wm_todo

Be aware that making a system-wide installation will not automattically create
an alias for your use. You will have to edit either your ``.bashrc`` or
``.bash_profile`` (or respective shell configuration filse) to include something
along the lines of:

::

    alias t='$HOME/bin/todo.py'

Usage
-----

The basic command is ``todo``.

* To add an item: ``todo add [item +project @context]``
* To complete an item" ``todo do (item number)``
* To delete an item: ``todo del (item number)``
* To add a priority (A thru Z) to an item: ``todo pri (A-Z) (item number)``
* To remove the priority from an item: ``todo depri (item number)``
* To list all items ``todo ls``

There are many other commands available.
	
Hacking
-------

Enjoy, contribute, and feel free to clone. I'm doing this blind [1]_ as best as
possible for fun.

Important Information
---------------------

- License: GPLv3_
- Build Status: TravisCI_

.. _GPLv3: https://raw.github.com/MinchinWeb/Todo.txt-python/development/LICENSE
.. _TravisCI: http://travis-ci.org/MinchinWeb/Todo.txt-python

--------

.. [1] By blind, I mean without looking at the source of the original todo.txt-cli
    project. I'm working solely from my experiences with the script and
    experimenting with the functionality while adding things I should probably write
    as patches and send upstream... I'll wait to finish my version of the project
    first though.
