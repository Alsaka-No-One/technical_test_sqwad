from urllib.parse import unquote

import urllib.request
import ssl

def is_shopify_shop(shop_url):
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        unquote(shop_url)
        fp = urllib.request.urlopen(shop_url)
        readBytes = fp.read()

        mystr = readBytes.decode("utf-8")
        fp.close()

        if "Shopify" in mystr or "shopify" in mystr:
            return True
    except Exception as e:
        print("an error occured: ", e)
    return False