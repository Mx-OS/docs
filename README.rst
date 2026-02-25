==================================================
Documentación de Organización de la Fundacion MxOS
==================================================

Documentación organizacional del proyecto de **Fundacion MxOS**, una iniciativa estratégica para desarrollar y mantener un sistema
operativo mexicano basado en GNU/Linux y los principios del Software Libre y de Código Abierto (FOSS).

Construida con `Sphinx <https://www.sphinx-doc.org/>`_ y el tema `Furo <https://pradyunsg.me/furo/>`_.

Publicada en: https://docs.mx-os.mx/es-MX/organizacion/

Requisitos
----------
* Python 3
* sphinx
* sphinx-design
* furo

Instalación de dependencias::

   pip install sphinx sphinx-design furo

Uso
---
Construir la documentación en HTML::

   make html

Servir localmente en http://localhost:8001::

   make serve

Limpiar artefactos de construcción::

   make clean

Licencia
--------
Este trabajo está licenciado bajo la `GNU Free Documentation License v1.3 o posterior (GFDLv1.3+)
<https://www.gnu.org/licenses/fdl-1.3.html>`_.
