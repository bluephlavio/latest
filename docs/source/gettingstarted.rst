Getting Started
===============


Basic Syntax
------------

Code Islands
::::::::::::

The simplest thing that you can do with :mod:`latest` is to insert python expressions or **code islands** inside a document. For a code island to be evaluated a data context (python dictionary) had to be set up.

By default code islands are bracketed between :code:`{%` and :code:`%}`. You can change these in the configuration file (see *code_entry* and *code_exit* options in *lang* section).

A plain text with code islands in between is called **expression**.

For example the expression

.. code::

   If a = {% a %} and b = {% b %}, then a + b = {% a+b %}

with a data context :code:`{a: '1', b: '2'}` evaluates to

.. code::

   If a = 1 and b = 2, then a + b = 3

Namespaces
::::::::::

Namespaces are a powerful concept in :mod:`latest`. A namespace is a branch of a data context (python dictionary). It can be a single data context or a list of data contexts.

A namespace can be useful to simplify variable names within python code with deep data contexts.

More interestingly, namespaces allow to creates loops without standard loop syntax.

Blocks
::::::

A more advanced concept is that of **blocks**. A block is defined by a namespace and an expression. The namespace define the branch of the data context in which to look for variable names in python code islands. If the namespace selects a list of dictionaries the block is evaluated for each one of them and the results are joined by a special sequence of characters defined in a configuration file. This is effectively a :code:`for` loop implementation without the standard :code:`for` loop syntax.


Creating a template
-------------------

A template file can be of any type but latest searches in it for **code islands** and **blocks**.


Creating a data file
--------------------

Data formats supported by :mod:`latest` are

* json
* yaml (require optional :mod:`pyyaml`)


The latest cli
--------------

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

