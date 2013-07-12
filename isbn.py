# -*- coding: utf-8 -*-
__author__ = 'Poc'
import re,json,sys,httplib,requests
_isbn_lst='4710947917212'
_URL_PREFIX='http://search.books.com.tw/exep/prod_search.php?cat=all&key='

def fetch_data(isbn):
    req_url=_URL_PREFIX+_isbn_lst

    pass

def main():
    print("isbn test")
    pass

if __name__ == '__main__':
    main()
