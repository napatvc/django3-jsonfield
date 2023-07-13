#!/usr/bin/env python

# Copyright (c) Microsoft Corporation.
# Licensed under the BSD license.

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")
os.environ.setdefault('DB_ENGINE', 'sqlite3')
os.environ.setdefault('DB_NAME', 'test')

if __name__ == "__main__":

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
