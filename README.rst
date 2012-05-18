KittyBenchmark
=========

:Author: Pierre-Yves Chibon <pingou@pingoured.fr>


Scripts used to run a benchmark using kittystore against the backends:

- postgresql (8.4.9-1.el6_1.1.x86_64)
- mongodb (1.8.2-2.el6.x86_64)


Get this project:
-----------------
Source:  https://github.com/pypingou/kittybenchmark


Dependencies:
-------------
- kittystore
- SQLAlchemy 
- pymongo for mongodb


Usage:
------

Clone this repository
 git clone https://github.com/pypingou/kittybenchmark.git

Have the dependencies installed or make a symbolic link to the
kittystore module.
 ln -s ../kittystore/kittystore .

Adjust the tests.py file.

 At the top of the file, adjust the lines 12 (URL) and 14 (MG_STORE),
 replace the dummy information with the real information needed to
 connect to the databases.


License
-------

.. _GPL v2.0: http://www.gnu.org/licenses/gpl-2.0.html

``KittyBenchmark`` is licensed under the `GPL v2.0`_

