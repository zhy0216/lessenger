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
* `py.test tests --loop uvloop`

make sure all the test cases can pass before you run the application.
If it did not pass, probably you forgot to setup `DARK_SKY_API_KEY` and `GMAP_API_KEY`.

## Reference:

* [sanic](https://github.com/channelcat/sanic)
* [sanic-cors](https://github.com/ashleysommer/sanic-cors)
* [aiohttp](https://github.com/aio-libs/aiohttp)
* [python regular expressions](https://docs.python.org/3/library/re.html)