# mast.tests

Module containing unit, integration and regression tests for
MAST for IBM DataPower.

To run:


```bash
# Unit tests
$ ./mast -m mast.tests --unit
# Integration tests
$ ./mast -m mast.tests --integration
# Regression tests
$ ./mast -m mast.tests --regression
# Run all tests
$ ./mast -m mast.tests --All
# Run a combination of tests
$ ./mast -m mast.tests --unit --integration
```

By default, results will be sent to `stdout`. To output results to a
file, add a `-o, --out-file` to any of the above commands.

