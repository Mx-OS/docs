.. _estrategia_de_desarrollo:

.. _development_strategy_mxos:

########################
Estrategia de Desarrollo
########################

La estrategia de desarrollo de la Fundación MxOS se articula en torno a dos ejes complementarios: la **creación y mantenimiento del
sistema operativo MxOS** como una plataforma robusta y adaptada para México, y la **promoción de la investigación y el desarrollo
(I+D) tecnológico más amplio** para impulsar la soberanía nacional.

Desarrollo del Sistema Operativo MxOS
=====================================
El desarrollo del sistema operativo MxOS se guiará por los siguientes principios y enfoques:

Base en CentOS Stream para Compatibilidad y Estabilidad
-------------------------------------------------------
Reconociendo la amplia adopción de sistemas basados en RHEL (Red Hat Enterprise Linux) y CentOS en el sector empresarial y
gubernamental de México, **MxOS (el sistema operativo) se basará fundamentalmente en CentOS Stream**. Esta decisión estratégica nos
permite:

* **Maximizar la Compatibilidad:** Asegurar una transición más fluida y una mejor interoperabilidad para organizaciones que ya
  utilizan soluciones del ecosistema RHEL/CentOS.

* **Aprovechar una Base Enterprise:** Heredar la estabilidad, seguridad y rendimiento probados de este ecosistema.

* **Reutilizar Herramientas y Documentación:** Adoptar herramientas de construcción, gestión de paquetes e instalación
  estandarizadas, y apalancar la extensa documentación existente.

* **Beneficiarnos del Aprendizaje Acumulado:** Capitalizar la experiencia y el conocimiento de la comunidad CentOS Stream y RHEL.

Enfoque de Adaptación y Complemento para MxOS
---------------------------------------------
Al partir de CentOS Stream, el esfuerzo principal para el SO MxOS se concentra en **adaptar y complementar** esta base:

* **Reutilización Máxima:** Priorizar el uso de paquetes de CentOS Stream para mantener la compatibilidad y eficiencia.

* **Identidad MxOS:** Aplicar la marca y elementos visuales propios.

* **Curación de Paquetes:** Definir perfiles de instalación y añadir software esencial para el usuario mexicano que no esté en la
  base (ej. suites ofimáticas, herramientas de productividad, aplicaciones de servidor complementarias). Estos se gestionarán en
  repositorios propios de MxOS.

* **Configuración y Localización Optimizadas:** Adaptación al contexto mexicano (idioma, teclado, configuraciones regionales).

* **Exploración de Variantes Inmutables:** Investigar y potencialmente desarrollar ediciones inmutables de MxOS con tecnologías como
  OSTree y `rpm-ostree` para mayor robustez y gestión moderna.

* **Aseguramiento de la Calidad (QA):** Pruebas exhaustivas de la distribución MxOS completa, enfocándose en los componentes
  añadidos y personalizados.

Investigación y Desarrollo Tecnológico Ampliado de la Fundación
===============================================================
Más allá del desarrollo específico del SO MxOS, la Fundación buscará posicionarse como un **centro para la investigación y el
desarrollo de tecnologías abiertas** relevantes para la soberanía de México. Esto incluye:

* **Áreas de Interés Estratégico:**

   * Ciberseguridad aplicada a infraestructuras nacionales.

   * Desarrollo de software para sectores clave mexicanos (ej. gobierno electrónico, educación, salud, PYMEs) utilizando FOSS.

   * Inteligencia Artificial y Ciencia de Datos con herramientas abiertas y enfoque ético.

   * Potencial exploración en hardware abierto y su integración con software soberano.

   * Redes y comunicaciones seguras.

* **Metodología:**

    * Fomentar proyectos de investigación aplicada y desarrollo experimental.

    * Colaborar estrechamente con universidades, centros de investigación públicos y privados, y otras OSC.

    * Publicar resultados, herramientas y conocimientos generados bajo licencias abiertas.

* **Sinergia con MxOS:**

    * El SO MxOS puede servir como plataforma de pruebas y despliegue para las innovaciones desarrolladas.

    * Las investigaciones pueden retroalimentar y mejorar la seguridad, funcionalidad y adaptabilidad de MxOS.

Herramientas y Procesos Comunes
===============================
Tanto para el desarrollo del SO MxOS como para otros proyectos de I+D, se aprovecharán:

* **Herramientas Estándar del Ecosistema FOSS:** Como `rpm`, `spec files`, `dnf`, `mock`, `Koji` (para construcción y empaquetado).

* **Instalador:** Personalización de Anaconda para MxOS.

* **Desarrollo Abierto:** Repositorios públicos (GitLab/GitHub), bug trackers y canales de comunicación abiertos para todos los
  proyectos de la Fundación.

Colaboración (Upstream y Local)
===============================
* **Proyectos Upstream (incluyendo CentOS Stream):** Reportar errores y, cuando sea posible, contribuir mejoras a los proyectos base
  que utiliza MxOS y otros desarrollos.

* **Comunidad Local:** Fomentar contribuciones de la comunidad mexicana en todos los niveles: desarrollo de código para MxOS y otros
  proyectos, empggg
