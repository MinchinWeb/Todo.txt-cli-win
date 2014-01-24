History
=======

0.4 Beta
-------
- convert from script to a system command (i.e. from ``todo.py`` to ``todo.exe``
  on Windows), courtesy of @minchinweb
- added ``top`` subcommand, that only displays the top 21 todo items (a
  screenful), courtesy of @minchinweb
- priorities now run A-Z (were A-X)
- hanging indent on long todo items, courtesy of @minchinweb
- Properly handle paths on windows with colons & backslashes courtesy @mstave 
  (commit message shows his name as unknown unfortunately: 
  3a8b7673cd85e8ec6d29c6832b5bcb2afdbb44c1)

0.3
---

- Add add-on functionality!

  - Add unittests for this functionality
  - Support todo.sh_'s add-ons_

    - Add unittests for this as well

- Add colorama support for users using the script in ``cmd.exe`` on 
  Windows
- Add tests for ``get_config()``
- Add @usage decorator for actions

  - Add unittests for the @usage decorator

- Add sample_addons directory with Matt Stave's suggestions
- PEP257 (Docstring) compliance
- Help documentation automatically generated
- Fix rare occurrence where script wipes out todo.txt file

.. _todo.sh: https://github.com/ginatrapani/todo.txt-cli
.. _add-ons:
    https://github.com/ginatrapani/todo.txt-cli/wiki/Todo.sh-Add-on-Directory
