import io                                                                       
import urllib2  
import scrapy                                                              
import pytesseract     
from PIL import Image  
     

class CaptchaSpider(scrapy.Spider):
    name = 'captcha'                                                            

    def start_requests(self):                                                   
        yield scrapy.Request('https://...', cookies={'PHPSESSID': 'xyz'})                      

  
