import folium
import requests
from pyfiglet import Figlet


def get_data(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()


# requirements
"""
folium==0.12.1.post1
pyfiglet==0.8.post1
requests==2.27.1
"""
