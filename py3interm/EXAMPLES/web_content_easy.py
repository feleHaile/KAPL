#!/usr/bin/env python

import sys
import requests

BASE_URL = 'http://lcboapi.com/products'

def main(args):

    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)
    
    response = requests.get(BASE_URL, params={ 'q': args[0] } )

    if response.status_code == requests.codes.OK:
        # print(response.content)
        raw_data = response.json()
        if raw_data['result']:
            for result in raw_data['result']:
                print("PRODUCT NUMBER:", result['product_no'])
                print("NAME:", result['name'])
                print("PACKAGE:", result['package'])
                print("PRICE: ${0:5.2f}/liter".format(result['price_per_liter_in_cents']/100))
                print(result['serving_suggestion'])
                print()
        else:
            print("Sorry, no items matched your query.")
    else:
        print("Sorry, HTTP response", response.status_code)
        
if __name__ == '__main__':
    main(sys.argv[1:])
