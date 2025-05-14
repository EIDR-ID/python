import unittest
import coverage
import sys

COVERAGE_SOURCE = ['../scheme', '../services']

class ColorTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write("\033[92m")  # Green
        self.stream.writeln(f"✔ PASS: {test}")
        self.stream.write("\033[0m")   # Reset

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write("\033[91m")  # Red
        self.stream.writeln(f"✘ FAIL: {test}")
        self.stream.write("\033[0m")   # Reset

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write("\033[91m")  # Red
        self.stream.writeln(f"✘ ERROR: {test}")
        self.stream.write("\033[0m")   # Reset

class ColorTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return ColorTextTestResult(self.stream, self.descriptions, self.verbosity)

def main():
    cov = coverage.Coverage(source=COVERAGE_SOURCE)
    cov.start()

    loader = unittest.defaultTestLoader
    suite = loader.discover('.', pattern='test_*.py')

    runner = ColorTextTestRunner(verbosity=1)
    result = runner.run(suite)

    cov.stop()
    cov.save()

    print("\n=== Coverage per component ===")
    for name in COVERAGE_SOURCE:
        print(f"\n{name.capitalize()} coverage:")
        cov.report(include=[f'{name}/*'], show_missing=True)

    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    main()
