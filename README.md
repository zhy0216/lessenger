# lessenger

It is a small code project practice.


## Environment
* python 3.6.5
* Mac 10.13.5

## Run Application
* `virtualenv venv -p python3`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `export DARK_SKY_API_KEY=<YOUR KEY HERE>`
* `export GMAP_API_KEY=<YOUR KEY HERE>`
* `python web.py`

## Run Test
* `py.test tests/*`

make sure all the test cases can pass before you run the application.

## Reference:

* [https://github.com/channelcat/sanic](https://github.com/channelcat/sanic)
* [https://github.com/ashleysommer/sanic-cors](https://github.com/ashleysommer/sanic-cors)
* [https://github.com/aio-libs/aiohttp](https://github.com/aio-libs/aiohttp)