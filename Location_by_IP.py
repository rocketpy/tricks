import folium
import requests
from pyfiglet import Figlet


def get_data(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        
        # for k, v in data.items():
        #    print(f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('Check internet connection!')


def main():
    preview_text = Figlet(font='slant')
    # print(preview_text.renderText('IP INFO'))
    ip = input('Please, enter IP address: ')
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()
    

# requirements
"""
folium==0.12.1.post1
pyfiglet==0.8.post1
requests==2.27.1
"""
