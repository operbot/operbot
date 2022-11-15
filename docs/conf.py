# OPERBOT - write your own commands
# -*- coding: utf-8 -*-


"write your own commands"


__name__ = "operbot"
__version__ = "105"


import doctest
import os
import sys
import unittest


curdir = os.getcwd()


sys.path.insert(0, os.path.join(curdir))
sys.path.insert(0, os.path.join(curdir, ".."))
sys.path.insert(0, os.path.join(curdir, "..", ".."))


# -- Options for GENERIC output ---------------------------------------------


project = __name__
master_doc = 'index'
version = '%s' % __version__
release = '%s' % __version__
language = ''
today = ''
today_fmt = '%B %d, %Y'
needs_sphinx='1.7'
exclude_patterns = ['_build', '_templates', '_source', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
modindex_common_prefix = [""]
keep_warnings = False
templates_path=['_templates']
add_function_parentheses = False
add_module_names = False
show_authors = False
pygments_style = 'colorful'
extensions=[
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages'
]


# -- Options for HTML output -------------------------------------------------


html_title = "write your own commands"
html_style = 'operator.css'
html_static_path = ["_static"]
html_css_files = ["operbot.css",]
html_short_title = "OPERBOT %s" % __version__
html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html',
    ]
}
html_theme = "alabaster"
html_theme_options = {
    'github_user': 'operbot',
    'github_repo': __name__,
    'github_button': False,
    'github_banner': False,
    'logo': 'opersmile.png',
    'link': '#000',
    'link_hover': '#000',
    'nosidebar': True,
    'show_powered_by': False,
    'show_relbar_top': False,
    'sidebar_width': 0,
}
html_favicon = "opersmile.png"
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = False
html_use_index = True
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
html_use_opensearch = 'http://%s.rtfd.io/' % __name__
html_file_suffix = '.html'
htmlhelp_basename = 'testdoc'

intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', 'objects.inv'),
                       'sphinx': ('http://sphinx.pocoo.org/', None),
                      }
intersphinx_cache_limit=1


rst_prolog = '''.. image:: operline.png
    :width: 100%
    :height: 2.3cm
    :target: index.html

.. raw:: html

    <center><b>

`about <about.html>`_ - :ref:`programmer <programmer>` - :ref:`source <source>` - `pypi <http://pypi.org/project/operbot>`_ - `github <http://github.com/operbot/operbot>`_ - `index <genindex-all.html>`_ 

.. raw:: html

   </b>
   </center>

'''

autosummary_generate=True
autodoc_default_flags=['members', 'undoc-members', 'private-members', "imported-members"]
autodoc_member_order='groupwise'
autodoc_docstring_signature=True
autoclass_content="class"
doctest_global_setup=""
doctest_global_cleanup=""
doctest_test_doctest_blocks="default"
trim_doctest_flags=True
doctest_flags=doctest.REPORT_UDIFF
nitpick_ignore=[
                ('py:class', 'builtins.BaseException'),
               ]
