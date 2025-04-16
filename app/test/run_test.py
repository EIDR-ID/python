import unittest
import coverage

# will be very useful for CLI and doing the Scheme ingestion for diff versions
# folders to include in coverage report
COVERAGE_SOURCE = ['../scheme', '../services']


def main():
    cov = coverage.Coverage(source=COVERAGE_SOURCE)
    cov.start()

    loader = unittest.defaultTestLoader

    # When creating new tests, make sure to start with test_ or add new suite and pattern
    suite = loader.discover('.', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    cov.stop()
    cov.save()

    print("\n=== Coverage per component ===")
    for name in COVERAGE_SOURCE:
        print(f"\n{name.capitalize()} coverage:")
        cov.report(include=[f'{name}/*'], show_missing=True)

    if not result.wasSuccessful():
        exit(1)


if __name__ == '__main__':
    main()
