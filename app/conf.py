# -- Environment settings -----------------------------------------------------
import os

plantuml_path = os.environ['PLANTUML_PATH']
noto_font_path = os.environ['NOTO_FONT_PATH']
static_dir = os.environ['STATIC_DIR']
template_dir = os.environ['TEMPLATE_DIR']
# -- Extention configuration ---------------------------------------------------
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
  # markdown parser
  'myst_parser',
]
# -- Project information -----------------------------------------------------
project = u'Project Name'
copyright = u'hermit255'
author = u'hermit255'
version = u'1.0'
release = u'1.0.0'
# -- Theme settings -----------------------------------------------------
extensions.append("uedoc_theme")
#html_theme = 'alabaster'
html_theme = "uedoc_theme"
html_favicon = "https://cdn.icon-icons.com/icons2/112/PNG/512/python_18894.png"
html_copy_source = False

# -- Epub settings ---------------------------------------------------
epub_title = project
epub_author = copyright
epub_basename = project
epub_language = u'ja'
epub_publisher = copyright
epub_identifier = u'http://example.com'
epub_scheme = 'URL'
epub_tocdepth = 2

# -- General configuration ---------------------------------------------------
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html'],
}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = [static_dir]
templates_path = [template_dir]

html_last_updated_fmt = '%Y-%m-%d %H:%M'

language = 'ja'
master_doc = 'index'
source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'restructuredtext',
  '.md': 'markdown',
}
htmlhelp_basename = 'doc'

# -- Global terms list -----------------------------------------------------
rst_prolog= u"""
.. include:: /docs/_replace.txt
"""
# -- Custom settings -----------------------------------------------------
def setup(app):
  app.add_css_file('css/code-block.css')
  app.add_css_file('css/custom.css')
  app.add_config_value('dev', True, 'html')

# -- Diagram configuration ---------------------------------------------------
blockdiag_fontpath = noto_font_path
seqdiag_fontpath = noto_font_path
actdiag_fontpath = noto_font_path
nwdiag_fontpath = noto_font_path

blockdiag_html_image_format ='SVG'
seqdiag_html_image_format = 'SVG'
actdiag_html_image_format = 'SVG'
nwdiag_html_image_format = 'SVG'

blockdiag_antialias = True
seqdiag_antialias = True
actdiag_antialias = True
nwdiag_antialias = True

# -- PlantUml configuration ---------------------------------------------------
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinxcontrib.plantuml')
graphviz_dot_args = ['-Gfontname=sans-serif', '-Efontname=sans-serif', '-Nfontname=sans-serif']
graphviz_output_format = 'svg'
plantuml = 'java -jar %s' % plantuml_path
plantuml_output_format = 'svg'

# -- HoverXref configuration ---------------------------------------------------
extensions.append('hoverxref.extension')
hoverxref_role_types = {
  'hoverxref': 'modal',
  'ref': 'modal',  # for hoverxref_auto_ref config
  'confval': 'tooltip',  # for custom object
  'mod': 'tooltip',  # for Python Sphinx Domain
  'class': 'tooltip',  # for Python Sphinx Domain
}