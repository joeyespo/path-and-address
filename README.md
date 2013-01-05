Path-and-Address
================

Functions for command-line server tools used by humans.


Description
-----------

Path-and-address resolves ambiguities for command-line interface applications
with the following pattern:

```bash
$ your_app [<path>] [<address>]
```

The library applies [the principal of least surprise][pols] to command-line
interfaces.

Some examples:

```bash
$ your_app .
 * Serving . on http://localhost:5000/

$ your_app 80
 * Serving . on http://localhost:80/

$ your_app ./80
 * Serving ./80 on http://localhost:5000/

$ your_app path/to/file
 * Serving path/to/file on http://localhost:5000/

$ your_app 0.0.0.0
 * Serving 0.0.0.0 on http://localhost:5000/

$ your_app . 0.0.0.0
 * Serving . on http://0.0.0.0:5000/

$ your_app 0.0.0.0:8080
 * Serving . on http://0.0.0.0:8080/
```


Usage
-----

Implement a CLI front-end in Python that exposes the above `[path] [address]`
pattern. Then call `resolve(path, address)`.

Example, using `sys.argv` directly:

```python
import sys
from path_and_pattern import resolve

path, address = resolve(*argv[1:])
```

More examples can be found in the "examples" directory.


Installation
------------

To install, simply:

```bash
$ pip install path-and-address
```

Or put it in your project's `requirements.txt`.


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository
3. Write tests to show that the bug was fixed or that the feature works
   as expected
3. Send a pull request


[pols]: http://en.wikipedia.org/wiki/Principle_of_least_astonishment
