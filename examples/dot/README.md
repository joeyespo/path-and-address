Dot
===

A [path-and-address][repo] example that uses [docopt][] for its
command-line argument processing.


Usage
-----

To try it, simply clone the repo, install the requirements, and run the script:

```bash
$ git clone git@github.com:joeyespo/path-and-address.git
$ cd path-and-address/examples/dot
$ pip install -r requirements.txt
```

And try some arguments:

```bash
$ dot.py .
 * Serving . on http://localhost:5000/

$ dot.py 80
 * Serving . on http://localhost:80/
```

[repo]: https://github.com/joeyespo/path-and-address
[docopt]: http://docopt.org
[localhost]: http://localhost:5000/
