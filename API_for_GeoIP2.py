# MaxMind GeoIP2 API

# https://pypi.org/project/geoip2/
# https://github.com/maxmind/GeoIP2-python
# https://www.maxmind.com/en/home

# pip install geoip2


# Web Service Example
import geoip2.webservice

# This creates a Client object that can be reused across requests.
# Replace "42" with your account ID and "license_key" with your license
# key. Set the "host" keyword argument to "geolite.info" to use the
# GeoLite2 web service instead of the GeoIP2 web service.
with geoip2.webservice.Client(42, 'license_key') as client:
    # Replace "city" with the method corresponding to the web service
    # that you are using, i.e., "country", "city", or "insights". Please
    # note that Insights is not supported by the GeoLite2 web service.
    response = client.city('203.0.113.0')
    response.country.iso_code
    response.country.name
    response.country.names['zh-CN']
    response.subdivisions.most_specific.name
    response.subdivisions.most_specific.iso_code
    response.city.name
    response.postal.code
    response.location.latitude
    response.location.longitude
    response.traits.network
