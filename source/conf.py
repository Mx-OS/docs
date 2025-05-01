# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MxOS'
copyright = '2025, Rénich Bon Ćirić'
author = 'Rénich Bon Ćirić'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
html_baseurl = 'https://mx-os.mx/'
html_favicon = '_static/logo.svg'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Furo customizations
html_title = "MxOS"
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Metrophobic"
    },
    "dark_css_variables": {
        "color-background-primary": "#111",
        "color-background-secondary": "#111115"
    }
}

# landing
html_additional_pages = {"index": "landing.html"}
