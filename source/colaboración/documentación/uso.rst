Uso
===
He aquí algunas instrucciones generales para poder generar la documentación:

Como generar HTML
-----------------

.. code-block:: sh

    # generar html
    make html

    # visualizarlo
    firefox build/html/index.html

Si estás desarrollando y quieres que se recargue con cada cambio, usa:

.. code-block:: bash

    sphinx-autobuild source/ build/html/

.. hint::
    A veces, no funciona bien la recarga, sobre todo cuando modificas el menú. En esos casos, detén el servicio y corre:
    ``make clean`` antes de iniciarlo de nuevo.

Como generar un PDF
-------------------

.. code-block:: sh

    # generar pdf
    make latexpdf

    # visualizarlo
    evince build/latex/mxos.pdf

Como generar un ePub
--------------------

.. code-block:: sh

    # generar pdf
    make epub

    # localización
    build/epub/MxOS.epub

