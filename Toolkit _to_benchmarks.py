#  pyperf - Python module to run and analyze benchmarks

# PyPi: https://pypi.org/project/pyperf/
# Github: https://github.com/psf/pyperf

# pip install pyperf

# Usage

# To run a benchmark use the pyperf timeit command (result written into bench.json):
# $ python3 -m pyperf timeit '[1,2]*1000' -o bench.json

"""
Or write a benchmark script bench.py:

#!/usr/bin/env python3
import pyperf

runner = pyperf.Runner()
runner.timeit(name="sort a sorted list",
              stmt="sorted(s, key=f)",
              setup="f = lambda x: x; s = list(range(1000))")
              
# To run the script and dump the results into a file named bench.json:

# $ python3 bench.py -o bench.json
              
"""

# To analyze benchmark results use the pyperf stats command:
# $ python3 -m pyperf stats telco.json
 
