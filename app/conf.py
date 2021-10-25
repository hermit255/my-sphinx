# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

def setup(app):
    app.add_css_file('css/code-block.css')
    app.add_css_file('css/custom.css')

import os
plantuml_dir = os.environ['PLANTUML_DIR']
font_dir = os.environ['FONT_DIR']
static_dir = os.environ['STATIC_DIR']
template_dir = os.environ['TEMPLATE_DIR']

# -- Project information -----------------------------------------------------

project = u'Project Name'
copyright = u'hermit255'
author = u'hermit255'

# The short X.Y version
version = u'1.0'
# The full version, including alpha/beta/rc tags
release = u'1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.blockdiag',
]
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinxcontrib.plantuml')

blockdiag_fontpath = '%s/NotoSansCJKjp-Regular.ttf' % font_dir
seqdiag_fontpath = '%s/NotoSansCJKjp-Regular.ttf' % font_dir
actdiag_fontpath = '%s/NotoSansCJKjp-Regular.ttf' % font_dir
nwdiag_fontpath = '%s/NotoSansCJKjp-Regular.ttf' % font_dir

blockdiag_html_image_format = 'SVG'
seqdiag_html_image_format = 'SVG'
actdiag_html_image_format = 'SVG'
nwdiag_html_image_format = 'SVG'

blockdiag_antialias = True
seqdiag_antialias = True
actdiag_antialias = True
nwdiag_antialias = True

graphviz_dot_args = ['-Gfontname=sans-serif', '-Efontname=sans-serif', '-Nfontname=sans-serif']
graphviz_output_format = 'svg'


plantuml = 'java -jar %s/plantuml.jar' % plantuml_dir
plantuml_output_format = 'svg'

# The master toctree document.
master_doc = 'index'
language = 'ja'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [static_dir]
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html'],
}
html_last_updated_fmt = '%Y-%m-%d %H:%M'
htmlhelp_basename = 'doc'
# Add any paths that contain templates here, relative to this directory.
templates_path = [template_dir]
source_suffix = '.rst'

# terms list
rst_prolog= u"""
.. include:: /docs/_replace.txt
"""

# theme
extensions.append("uedoc_theme")
html_theme = "uedoc_theme"
html_favicon = "https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png"
html_copy_source = False