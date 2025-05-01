Instalación
===========

Para instalar lo requerido para colaborar con el proyecto de documentación, debes hacer lo siguiente:


.. tab-set::

    .. tab-item:: Fedora

        Instalar los paquetes requeridos:

        .. code-block:: sh

            # como root o, además, puedes usar sudo
            dnf -y install \
                latexmk \
                python3-furo \
                python3-sphinx \
                python3-sphinx-design \
                texlive-babel-spanish \
                texlive-capt-of \
                texlive-cmap \
                texlive-ec \
                texlive-fncychap \
                texlive-framed \
                texlive-makeindex \
                texlive-metafont \
                texlive-needspace \
                texlive-parskip \
                texlive-tabulary \
                texlive-tex-gyre \
                texlive-upquote \
                texlive-wrapfig

    .. tab-item:: CentOS Stream 9

        Por lo pronto, no existen los paquetes:

        * python3-furo
        * sphinx-babel-spanish
        * python3-sphinx-design

        Fuera de eso, las dependencias pudiesen ser instaladas en la misma manera que Fedora pero sin incluir estos dos paquetes.

        .. attention::

            Es necesario instalar y/o activar `epel-release`, `crb`, `nfv` y `rt` antes de intentarlo.

        Para instalar lo que resta, es necesario:

        .. code-block:: sh

            # instalar componentes de dnf y epel
            dnf -y install dnf-plugins-core epel-release

            # activar los repositorios requeridos
            dnf config-manager --enable crb --enable epel --enable nfv --enable rt

            # verificar
            dnf repolist --all

        Luego, instalar los componentes requeridos:

        .. code-block:: sh

            # como root o, además, puedes usar sudo
            dnf -y install \
                latexmk \
                python3-sphinx \
                texlive-capt-of \
                texlive-cmap \
                texlive-ec \
                texlive-fncychap \
                texlive-framed \
                texlive-makeindex \
                texlive-metafont \
                texlive-needspace \
                texlive-oberdiek \
                texlive-parskip \
                texlive-tabulary \
                texlive-tex-gyre \
                texlive-upquote \
                texlive-wrapfig

        Para los componentes restantes, es posible instalarlos usando un "virtual environment" de python.
