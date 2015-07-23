# TODO.TXT-CLI-python test script
# Copyright (C) 2011-2012  Sigmavirus24
# Copyright (C) 2013       William Minchin
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# TLDR: This is licensed under the GPLv3. See LICENSE for more details.

import os
import shutil
import todo
import base
import sys
import unittest


class TestAddons(base.BaseTest):
    def setUp(self):
        super(TestAddons, self).setUp()
        todo.cli.CONFIG['TODO_DIR'] = todo.cli._path('./.todo-testing/')
        todo.cli.CONFIG['TODO_ACTIONS_DIR'] = todo.cli._path('./.todo-testing/actions')
        if not os.path.exists(todo.cli.CONFIG['TODO_DIR']):
            os.mkdir(todo.cli.CONFIG['TODO_DIR'])
        if not os.path.exists(todo.cli.CONFIG['TODO_ACTIONS_DIR']):
            os.mkdir(todo.cli.CONFIG['TODO_ACTIONS_DIR'])

    def tearDown(self):
        super(TestAddons, self).tearDown()
        for key in ('TODO_ACTIONS_DIR', 'TODO_DIR'):
            if os.path.exists(todo.cli.CONFIG[key]):
                shutil.rmtree(todo.cli.CONFIG[key], ignore_errors=True)

    def test_noaddons(self):
        bad_args = ['addp', 'foo']
        good_args = ['add', 'foo']
        self.assertEqual(todo.cli.execute_commands(bad_args), 1)
        self.assertEqual(todo.cli.execute_commands(good_args), 0)

    def test_py_addons(self):
        lines = ['def addp():\n', '\tpass', '\n\n',
            'commands = {"addp": (False, addp)}\n']
        filename = todo.cli.CONFIG['TODO_ACTIONS_DIR'] + '/addp.py'
        if not os.path.exists(filename):
            with open(filename, 'w+') as fd:
                fd.writelines(lines)

        todo.cli.CONFIG['ACTIONS'] = 'addp'
        commands = todo.cli.commands.copy()
        todo.cli.load_actions()

        args = ['addp', '']
        self.assertEqual(todo.cli.execute_commands(args), 0)
        os.unlink(filename)
        if os.path.exists(filename + 'c'):
            os.unlink(filename + 'c')
        todo.cli.CONFIG['ACTIONS'] = ''
        todo.cli.commands = commands.copy()
        self.assertEqual(todo.cli.execute_commands(args), 1)

    @unittest.skipIf(sys.platform.startswith("win"), "sh not (typically) available on Windows")
    def test_sh_addons(self):
        lines = ['#!/bin/bash\n\n', 'A=$((1+1))']
        filename = todo.cli.CONFIG['TODO_ACTIONS_DIR'] + '/addnums'
        if not os.path.exists(filename):
            with open(filename, 'w+') as fd:
                fd.writelines(lines)
        os.chmod(filename, 0o700)

        args = ['addnums']
        self.assertEqual(todo.cli.execute_commands(args), 0)
        os.unlink(filename)
        self.assertEqual(todo.cli.execute_commands(args), 1)
