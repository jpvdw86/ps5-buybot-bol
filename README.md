# Bol.com order bot

This bot check if the product is available and if, its open the (chrome) browser and add it to cart

##Install
You need to have python3 and virtualenv and chrome with chromedriver installed <br>
Chrome driver can be downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads

brew install cairo pkg-config gobject-introspection 

Mac
``python3 -m pip install --user virtualenv``

Windows
``py -m pip install --user virtualenv``

Create and activate a virtaulenviroment <br>
Mac
``python3 -m venv venv``
``source venv/bin/activate``

Windows
``python3 -m venv venv``
``.\venv\Scripts\activate``

Run
``pip3 install -r requirements.txt``

Stop virtualenv <br>
close terminal or run ``deactivate``



##Usage
`` 
python main.py --email=<your email> --password=<your password> --productId=<product id> --timeout=120 --directorder
``

####The direct order option is optional.
if you direct want to open the default payment method

####The timeout is default 120 (seconds). 
this is the amount of seconds that the scrip check if product is available


#### Example product IDS

Playstation 5 = 9300000004162282<br>
Chromecast = 9200000049577657

You can find the product ID in the url
