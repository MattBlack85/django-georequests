#!/usr/bin/env python

import sys


def run_tests():
    import django
    from django.conf import global_settings
    from django.conf import settings


    settings.configure(
        INSTALLED_APPS=[
            'geo_middleware',
            'reversegeoip',
            'geodashboard'
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
    )

    if hasattr(django, 'setup'):
        django.setup()

    from django.test.simple import DjangoTestSuiteRunner

    test_runner = DjangoTestSuiteRunner(verbosity=2)
    return test_runner.run_tests(['geo_middleware',
                                  'reversegeoip',
                                  'geodashboard'])

def main():
    failures = run_tests()
    sys.exit(failures)

if __name__ == '__main__':
    main()
