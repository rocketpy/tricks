"""
pip install ftputil


#  docs
https://ftputil.sschwarzer.net/trac/wiki/RussianDocumentation

#  ftp-servers list
https://t.me/aiWeipeighah7vufoHa0ieToipooYe
"""


#  need create directory(folder) 'Downloads'  !!!
import ftputil
import warnings


warnings.filterwarnings("ignore")

host = 'host '
username = 'some_name'
password = ''

try:
    ftp_host = ftputil.FTPHost(host, username, password)
    ftp_host.use_list_a_option = False

    with ftp_host:
            list = ftp_host.listdir(ftp_host.curdir)
            for fname in list:
                if ftp_host.path.isdir(fname):
                    print(fname + 'dir name')
                    try:
                        ftp_host.upload('test.txt', '/' + fname + '/test.txt')
                        print("File in dir  " + fname)
                    except:
                        print("Dir not exist !")
                else:
                    print(fname + 'some_file')
                    if('.zip' in fname):  # HERE we can use any (.zip , .txt and others )
                        print('File is loading ' + fname)
                        ftp_host.download(fname, 'downloads/' + fname)
                        print('File  ' + fname + ' is loaded ')
except:
    print('No response from server !')
