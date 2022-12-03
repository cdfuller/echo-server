# echo-server

This is a python socket server that echos back any http request made to it.

## Example
Make a custom request:
```
$ curl --header "Favorite-Color: Purple" \
      --data "param1=value1&param2=value2"\
      http://localhost:3246/hello-mars
```

Prints:
```
$ python echo.py
Echoing from http://localhost:3246
127.0.0.1 - Thu Mar 15 23:43:27 2018 - POST /hello-mars HTTP/1.1
```

Returns
```
POST /hello-mars HTTP/1.1
Host: localhost:3246
User-Agent: curl/7.54.0
Accept: */*
Favorite-Color: Purple
Content-Length: 27
Content-Type: application/x-www-form-urlencoded

param1=value1&param2=value2
```

## Requirements

Python 3.4+

No other dependencies


## Running

Default port is 3246 (echo on a dialpad)

Python:
```
./echo.py
```

**Or:**

Docker:
```
docker build -t echo-server .
docker run -itp 3246:3246 echo-server
```

**Or:**
Dockerhub:
```
docker run -itp 3246:3246 cdfuller/echo-server
```

### Options
```
  -b BIND, --bind BIND  host to bind to
  -p PORT, --port PORT  port to listen on
  -v, --verbose         print all requests to terminal
```


## References
* [Let’s Build A Web Server. Part 1](https://ruslanspivak.com/lsbaws-part1/), [Part. 2](https://ruslanspivak.com/lsbaws-part2/), [Part 3](https://ruslanspivak.com/lsbaws-part3/)
* [HTTP/1.1 RFC2616](https://tools.ietf.org/html/rfc2616)
* [A Practical Guide to Writing Clients and Servers](http://www.jmarshall.com/easy/http/)

## TODO
* Figure out how to make it a module so I can do `python -m echo`
  * Notes:
    * Works by default.
    * Would like to figure out how to add it to the python package index
* Write responses to log file
* How to add options when using docker to run
