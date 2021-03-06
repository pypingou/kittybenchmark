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

.. _R: http://r-project.org
- kittystore (Bundled in)
- SQLAlchemy 
- pymongo for mongodb
- `R`_

We now have a modified version of kittystore which contains more queries
for PostgreSQL. Modified queries which will not be part of upstream's
version (for example, using union or 'or' statement).
Use the version bundled in, or you will have to adjust tests.py


Usage:
------

Clone this repository:
 git clone https://github.com/pypingou/kittybenchmark.git

Adjust the tests.py file:
 At the top of the file, adjust the lines 12 (URL) and 14 (MG_STORE),
 replace the dummy information with the real information needed to
 connect to the databases.

Run the script:
 python tests.py

Generate the visualisation:
 R < visualisation.R

License
-------

.. _GPL v2.0: http://www.gnu.org/licenses/gpl-2.0.html

``KittyBenchmark`` is licensed under the `GPL v2.0`_

