import io                                                                       
import urllib2  
import scrapy                                                              
import pytesseract     
from PIL import Image  
     

class CaptchaSpider(scrapy.Spider):
    name = 'captcha'                                                            


    def start_requests(self):                                                   
        yield scrapy.Request('https://...', cookies={'PHPSESSID': 'xyz'})                      

     
    def parse(self, response):                                                  
        img_url = response.urljoin(response.xpath('...').extract_first())
        url_opener = urllib2.build_opener()                                     
        url_opener.addheaders.append(('Cookie', 'PHPSESSID=xyz'))               
        img_bytes = url_opener.open(img_url).read()                             
        img = Image.open(io.BytesIO(img_bytes))                                 
        captcha = pytesseract.image_to_string(img)                              
        print('Captcha solved:', captcha)                                

        return scrapy.FormRequest.from_response(response, formdata={'captcha': captcha},                             
                                                callback=self.after_captcha)                                        


    def after_captcha(self, response):                                          
        print('Result:', response.body)     
  
