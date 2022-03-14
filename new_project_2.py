#  python-geoip

# pip install python-geoip

# for free MaxMind Geolite2 database you can in addition
# pip install python-geoip-geolite2

# Docs: https://pythonhosted.org/python-geoip/

# Usage
from geoip import geolite2

match = geolite2.lookup('17.0.0.1')
print(match.country)
# match.continent
# match.timezone
# match.subdivisions


