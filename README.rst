Readme
======

``latest`` is a LaTeX-oriented template engine.

Basic Usage
-----------

Run `latest` script from the command line

.. code-block:: bash

    latest template data

where 
    * `template` is the path to a template file and 
    * `data` is the path to a yaml formatted data file.

An example template file can be something like::

    \documentclass{article}
    
    \title{<<<$title$>>>}
    \author{<<<$author$>>>}
    \date{<<<Biella (IT), $date$>>>}
    
    \begin{document}
    <<<content::x = $x$ so that x^2 = $x**2$>>>.
    \end{document}

while a yaml formatted data file can be something like::

    title: Testing latest
    author: Flavio Grandin
    date: Today
    content:
      x: 3

The expected output is::

    \documentclass{article}
    
    \title{Testing latest}
    \author{Flavio Grandin}
    \date{Biella, Today}
    
    \begin{document}
    x = 3 so that x^2 = 9.
    \end{document}


