py.test test_sample.py --collect-only  # collects information test suite

py.test test_sample.py -v  # outputs verbose messages

py.test -q test_sample.py  # omit filename output

python -m pytest -q test_sample.py  # calling pytest through python

py.test --markers  # show available markers


# In order to create a reusable marker.
"""
# content of pytest.ini
[pytest]
markers =
    webtest: mark a test as a webtest.
"""

py.test -k "TestClass and not test_one"  # only run tests with names that match the "string expression"

py.test test_server.py::TestClass::test_method  # cnly run tests that match the node ID

py.test -x  # stop after first failure

py.test --maxfail=2  # stop after two failures

py.test --showlocals  # show local variables in tracebacks
py.test -l  # (shortcut)

py.test --tb=long  # the default informative traceback formatting
py.test --tb=native  # the Python standard library formatting
py.test --tb=short  # a shorter traceback format
py.test --tb=line  # only one line per failure
py.test --tb=no  # no tracebak output

py.test -x --pdb # drop to PDB on first failure, then end test session

py.test --durations=10  # list of the slowest 10 test durations.

py.test --maxfail=2 -rf  # exit after 2 failures, report fail info.

py.test -n 4  # send tests to multiple CPUs

py.test -m slowest  # run tests with decorator @pytest.mark.slowest or slowest = pytest.mark.slowest; @slowest

py.test --traceconfig  # find out which py.test plugins are active in your environment.

py.test --instafail  # if pytest-instafail is installed, show errors and failures instantly instead of waiting until the end of test suite.

# Test using parametrize
"""
    import pytest


    @pytest.mark.parametrize(
        ('n', 'expected'), [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            pytest.mark.xfail((1, 0)),
            pytest.mark.xfail(reason="some bug")((1, 0)),
            pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
        ]
    )
    def test_increment(n, expected):
        assert n + 1 == expected
"""
