Getting Started
---------------

Run `latest` script from the command line

.. code-block:: bash

    $ latest template data


where 

    * **template** is the path to a template file
    * **data** is the path to a *json* or *yaml* formatted data file.


---------------------------------------------------------------------


An example template file can be something like

.. include:: ../../test/res/template.tmpl
   :literal:

while the data file can be something like (*yaml*)

.. include:: ../../test/res/data.yaml
   :literal:

The expected output is

.. include:: ../../test/res/expected.tex
   :literal:

