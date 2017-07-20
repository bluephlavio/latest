Getting Started
---------------

Run `latest` script from the command line

.. code-block:: bash

    $ latest template data


where 

    * `template` is the path to a template file and 
    * `data` is the path to a yaml formatted data file.


An example template file can be something like

.. include:: ../../test/res/example.tmpl
   :literal:

while a yaml formatted data file can be something like

.. include:: ../../test/res/example.yaml
   :literal:

The expected output is

.. include:: ../../test/res/example.tex
   :literal:

