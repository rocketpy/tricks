# build - A simple, correct Python build frontend.

# https://github.com/pypa/build
# https://build.pypa.io/en/stable/

"""
Installation - build can be installed via pip or an equivalent via:

$ pip install build

Usage

$ python -m build

python -m build

A simple, correct Python build frontend.
By default, a source distribution (sdist) is built from {srcdir} and a binary distribution (wheel) is built from the sdist.
This is recommended as it will ensure the sdist can be used to build wheels.
Pass -s/–sdist and/or -w/–wheel to build a specific distribution.
If you do this, the default behavior will be disabled,
and all artifacts will be built from {srcdir} (even if you combine -w/–wheel with -s/–sdist, the wheel will be built from {srcdir}).

python -m build [-h] [--version] [--verbose] [--sdist] [--wheel] [--outdir PATH]
                [--skip-dependency-check] [--no-isolation | --installer {pip,uv}]
                [--config-setting KEY[=VALUE]]
                [srcdir]

python -m positional arguments
srcdir - source directory (defaults to current directory)

python -m options
-h, --help - show this help message and exit

--version, -V - show program’s version number and exit

--verbose, -v - increase verbosity (default: 0)

--sdist, -s - build a source distribution (disables the default behavior)

--wheel, -w - build a wheel (disables the default behavior)

--outdir PATH, -o PATH - output directory (defaults to {srcdir}/dist)

--skip-dependency-check, -x - do not check that build dependencies are installed

--no-isolation, -n - disable building the project in an isolated virtual environment.
Build dependencies must be installed separately when this option is used

--installer INSTALLER - Python package installer to use (defaults to pip)

--config-setting KEY[=VALUE], -C KEY[=VALUE] - settings to pass to the backend. Multiple settings can be provided.
Settings beginning with a hyphen will erroneously be interpreted as options to build if separated by a space character;
use --config-setting=--my-setting -C--my-other-setting (default: None)
"""
