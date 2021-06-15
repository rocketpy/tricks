# TypeTastic - Python utility to make creating screencasts easier, and doing live demo's less stressful.

# PyPi: https://pypi.org/project/typetastic/

# pip install typetastic

# TypeTastic uses a Robot to type commands for you. In the simplest form you can pass the commands in as an array.
import typetastic


robot = typetastic.Robot()
robot.load(['ls', 'echo "Hello World\!"'])
robot.run()

