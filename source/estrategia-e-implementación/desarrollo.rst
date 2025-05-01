.. _development_strategy_mxos:

########################
Estrategia de Desarrollo
########################

La estrategia de desarrollo de MxOS adopta un enfoque pragmático y eficiente, diseñado para ofrecer un sistema operativo robusto,
seguro y relevante para México con rapidez y sostenibilidad. Inicialmente, **MxOS se basará directamente en CentOS Stream**, aunque
la visión a largo plazo contempla alcanzar una mayor autosuficiencia.

Base: CentOS Stream
===================
La decisión de utilizar **CentOS Stream** como la base fundamental de MxOS nos permite:

* **Aprovechar una Base Enterprise:** Heredamos la estabilidad, seguridad y rendimiento de nivel empresarial del ecosistema RHEL
  (Red Hat Enterprise Linux), del cual CentOS Stream es el flujo de desarrollo principal.

* **Reutilizar Infraestructura y Herramientas:** Adoptamos las herramientas de construcción (`rpm`, `mock`, `koji`), gestión de
  paquetes (`dnf`) e instalación (Anaconda) probadas y estandarizadas del ecosistema Fedora/CentOS/RHEL.

* **Apalancar Documentación Existente:** Nos beneficiamos de la extensa documentación disponible para CentOS Stream y RHEL,
  reduciendo significativamente el esfuerzo de documentación base.

* **Beneficiarnos del Aprendizaje Acumulado:** Capitalizamos las décadas de experiencia, lecciones learnedas y ciclos de prueba y
  error que han conformado CentOS Stream, evitando obstáculos comunes en el desarrollo de distribuciones.

* **Compatibilidad:** Obtenemos una amplia compatibilidad de hardware y software gracias a la extensa base de usuarios y pruebas del
  ecosistema RHEL.

Este punto de partida nos permite acelerar el desarrollo inicial y concentrarnos en el valor añadido específico para México.

Enfoque del Desarrollo de MxOS (Adaptación y Complemento)
=========================================================
Al partir de CentOS Stream, nuestro esfuerzo de desarrollo **se concentra en adaptar y complementar** esta sólida base para
satisfacer las necesidades específicas de México. Las tareas principales del equipo y la comunidad MxOS serán:

* **Reutilización Máxima:** Utilizar los paquetes binarios y fuentes de CentOS Stream siempre que sea posible, minimizando la
  necesidad de recompilar o modificar el núcleo base.

* **Identidad MxOS:** Aplicar la marca, temas visuales (artwork), fondos de pantalla y otros elementos gráficos propios de MxOS para
  darle una identidad distintiva.

* **Selección y Curación de Paquetes:** Definir los conjuntos de paquetes que se instalarán por defecto para diferentes perfiles de
  uso (ej. escritorio estándar, servidor básico, estación de trabajo para desarrollo), posiblemente eliminando software no relevante
  y añadiendo otros.

* **Adición de Software Esencial Faltante:** Empaquetar y mantener en **repositorios propios de MxOS** aquellas aplicaciones y
  herramientas clave que no formen parte de CentOS Stream pero sean consideradas esenciales para los usuarios mexicanos (ej. suites
  ofimáticas, herramientas de usuario final, aplicaciones de servidor complementarias).

* **Configuración y Localización Optimizadas:** Establecer configuraciones predeterminadas adaptadas a México (idioma es-MX, teclado
  latinoamericano, zona horaria, etc.) y asegurar una localización completa.

* **Exploración de Variantes Inmutables:** Investigar y potencialmente desarrollar **ediciones inmutables** de MxOS (similares a
  Fedora Silverblue/Kinoite) utilizando tecnologías como **OSTree** y `rpm-ostree`. Estas ediciones ofrecerían mayor robustez,
  actualizaciones atómicas y un paradigma de gestión moderno para casos de uso específicos (escritorios, edge, contenedores).

* **Aseguramiento de la Calidad (QA):** Probar la distribución MxOS completa, enfocándose en la correcta integración de los
  componentes añadidos, las configuraciones personalizadas, las variantes (incluyendo las inmutables si se desarrollan) y la
  compatibilidad general, complementando las pruebas de CentOS Stream.

Herramientas y Procesos
=======================
Aprovecharemos las herramientas estándar del ecosistema:

* **Empaquetado:** `rpm` y `spec files`.

* **Gestión de Paquetes:** `dnf` (y `rpm-ostree` para variantes inmutables).

* **Construcción:** Sistemas como `mock` y potencialmente `Koji` para los repositorios MxOS.

* **Instalador:** Personalización del instalador Anaconda.

* **Desarrollo Abierto:** Repositorios públicos (GitLab/GitHub) para los paquetes y configuraciones específicas de MxOS, y un bug
  tracker público.

Colaboración (Upstream y Local)
===============================
* **CentOS Stream:** Interactuaremos con la comunidad CentOS Stream reportando bugs encontrados en la base que afecten a MxOS.

* **Comunidad MxOS:** Fomentaremos las contribuciones locales para empaquetar software adicional, mejorar la localización, realizar
  pruebas y desarrollar documentación específica de MxOS.

Ciclo de Vida y Actualizaciones
===============================
Inicialmente, el ciclo de vida de MxOS estará **estrechamente ligado al de CentOS Stream**. Las actualizaciones de seguridad y
paquetes provenientes de CentOS Stream se integrarán de forma continua o periódica en MxOS. Esto implica un modelo de
**actualización más continuo**.

Evolución a Largo Plazo: Hacia la Autosuficiencia
=================================================
Si bien comenzar basándonos en CentOS Stream es un enfoque pragmático y eficiente, la **visión a largo plazo** para MxOS, alineada
con el objetivo final de soberanía tecnológica, es alcanzar la **autosuficiencia técnica**.

Esto significa aspirar a tener la capacidad de **gestionar el ciclo de vida completo de todos los paquetes** del sistema operativo
de forma independiente, aunque sigamos colaborando y utilizando fuentes del ecosistema FOSS global. Lograr esta independencia
requerirá un **crecimiento muy significativo en recursos, infraestructura y talento técnico especializado** dentro del proyecto MxOS
y su ecosistema.

Es un objetivo ambicioso que guiará la evolución del proyecto a medida que madure y consolide sus capacidades y recursos.

---

Esta estrategia revisada establece un camino claro: empezar de forma eficiente apalancando CentOS Stream, enfocar los esfuerzos
iniciales en la adaptación y el valor añadido para México (incluyendo la exploración de variantes inmutables), y mantener la vista
en el objetivo a largo plazo de una mayor independencia técnica, siempre dentro de un marco de desarrollo abierto y colaborativo.
