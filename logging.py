import logging


def main():
    logging.basicConfig(filename ='app.log', level = logging.ERROR)
    
    # Calls variables
    hostname = 'www...com'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
      
    # logging calls
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode = %r', filename, mode)
    logging.debug('Got here')
      
if __name__ == '__main__':
    main()
    
    
# Example 2
logging.basicConfig(filename = 'app.log', 
                    level = logging.WARNING, 
                    format = '%(levelname)s:%(asctime)s:%(message)s')

# Example 3
import logging
import logging.config
  
def main():
    # Configure the logging
    logging.config.fileConfig('logconfig.ini')
