# Mr. Python
[![Build Status](https://travis-ci.org/petermelias/mrpython.png?branch=master)](https://travis-ci.org/petermelias/mrpython) [![Coverage Status](https://coveralls.io/repos/petermelias/mrpython/badge.png?branch=master)](https://coveralls.io/r/petermelias/mrpython?branch=master) [![Downloads](https://pypip.in/d/mrpython/badge.png)](https://pypi.python.org/pypi/mrpython/) [![Downloads](https://pypip.in/v/mrpython/badge.png)](https://pypi.python.org/pypi/mrpython/)

A collection of functions, decorators and data that don't seem to fit into any of my (or anybody else's) libraries.

## Functions
* ``` autolog(message, level=logging.DEBUG) ```
* ``` enum(**enums) ```
* ``` ip2long(ip) ```
* ``` long2ip(long) ```
* ``` to_dict(o, limit=None) ```
* ``` walker(node, limit=None) ```

## Data
* STATES (dict)
* ORDERED_STATES (OrderedDict)

## Interfaces
* TInterface (only for use with walker)


### Instructions for using walker

1. Inherit your walkable nodes from ``` mrpython.TInterface ```
2. Pass one of the nodes to ``` walker(node) ``` - or - include a limiting tuple if you like ``` walker(node, limit=('name', 'address')) ```
3. Store the resulting dictionary :)