# -*- coding: utf-8 -*-
__author__ = 'Poc'

import re,json,sys,requests,codecs
from BeautifulSoup import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

_isbn_lst='4710947917212'
_URL_PREFIX='http://search.books.com.tw/exep/prod_search.php?cat=all&key='

def parse_html(data):
    soup =BeautifulSoup(data)
    soup_price =soup.find('span', {'class' :'price'})
    # print(dir(soup_price))
    print((soup_price.find('strong').findAll('b')))
    print(soup_price.findChildren('<b>'))
    print(soup.find('HEAD'))

    pass

def fetch_data(isbn):
    html_file = 'save_isbn.html'
    req_url=_URL_PREFIX+_isbn_lst
    # results = requests.get(req_url,
    #                        headers={'User-Agent': 'Mozilla/5.0'})
    #
    # print(results.text.encode('iso-8859-1'))
    # print(results.text.encode('utf-8'))


    # parse_html(results.text.encode('iso-8859-1'))
    # f = codecs.open(html_file,'w', 'utf-8')
    # f.write(results.text.encode('iso-8859-1'))
    # f.close()
    parse_html( open(html_file,'r').read() )
    pass

def main():
    print("isbn test")
    fetch_data(_isbn_lst)
    pass

if __name__ == '__main__':
    main()
