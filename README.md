# echo-server

This is a python socket server that echos back any http request made to it.

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
* Add screenshot and instructions to README
* Figure out how to make it a module so I can do `python -m echo`
  * Notes:
    * Works by default.
    * Would like to figure out how to add it to the python package index
* Add to dockerhub
* Write responses to log file
