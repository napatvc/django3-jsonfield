#!/usr/bin/env python
import os
import sys
import warnings
import django

BASE_PATH = os.path.dirname(__file__)


def main():
    """
    Standalone django model test with a 'memory-only-django-installation'.
    You can play with a django model without a complete django app installation.
    http://www.djangosnippets.org/snippets/1044/
    """
    warnings.filterwarnings("always", category=DeprecationWarning)
    warnings.filterwarnings("always", category=PendingDeprecationWarning)

    os.environ["DJANGO_SETTINGS_MODULE"] = "jsonfield.tests.settings"
    os.environ.setdefault('DB_ENGINE', 'sqlite')
    os.environ.setdefault('DB_NAME', 'test')
    from django.conf import global_settings
    from django.test.utils import get_runner
    test_runner = get_runner(global_settings)
    test_runner = test_runner()

    if getattr(django, 'setup', None):
        django.setup()

    failures = test_runner.run_tests(['jsonfield'])

    sys.exit(failures)


if __name__ == '__main__':
    main()
