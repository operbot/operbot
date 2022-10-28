# This file is placed in the Public Domain.
# -*- coding: utf-8 -*-


import doctest
import sys
import os


curdir = os.getcwd()


sys.path.insert(0, curdir)
sys.path.insert(0, curdir + os.sep + '..' )
sys.path.insert(0, curdir + os.sep + '..'  + os.sep + "..")


__version__ = "104"


needs_sphinx='1.7'

nitpick_ignore = [
                ('py:class', 'builtins.BaseException'),
               ]


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages'
]


project = "OPERBOT"
version = '%s' % __version__
release = '%s' % __version__


html_short_title ="operator bot"
html_title = "OPERBOT"
html_style = 'operbot.css'
html_static_path = ["_static"]
html_css_files = ["operbot.css",]
html_theme = "alabaster"
html_theme_options = {
    'github_user': 'operbot',
    'github_repo': 'operbot',
    'github_button': True,
    'github_banner': False,
    'logo': 'opersmile.png',
    'link': '#000',
    'link_hover': '#000',
    'nosidebar': True,
    'show_powered_by': False,
    'show_relbar_top': False,
}
#html_theme_path = []
html_favicon = "opersmile.png"
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = True
html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html',
    ]
}
html_use_index = True
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
html_use_opensearch = 'http://operbot.rtfd.io/'
html_file_suffix = '.html'
htmlhelp_basename = 'pydoc'
templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
language = ''
today = ''
today_fmt = ''
#exclude_patterns = ['_build', "_sources", "_templates"]
exclude_patterns = ['_build', '_templates', '_source', 'Thumbs.db', '.DS_Store']
default_role = ''
add_function_parentheses = False
add_module_names = False
show_authors = True
pygments_style = 'colorful'
modindex_common_prefix = [""]
keep_warnings = True
rst_prolog = '''.. image:: operline.png
    :width: 100%
    :height: 2.3cm
    :target: index.html

.. raw:: html

    <center><b>

:ref:`about <about>` - :ref:`manual <manual>` - :ref:`programmer <programmer>` - :ref:`source <source>` - `pypi <http://pypi.org/project/operbot>`_ - `github <http://github.com/operbot/operbot>`_ - `sponsor <http://operbot.rtfd.io>`_ - `index <genindex-all.html>`_

.. raw:: html

   </b>
   </center>

'''
autosummary_generate = True
autodoc_default_flags = ['members',
                         'undoc-members',
                         'private-members',
                         "imported-members"]
autodoc_member_order = 'bysource'
autodoc_docstring_signature = False
autoclass_content = "class"
doctest_global_setup = ""
doctest_global_cleanup = ""
doctest_test_doctest_blocks = "default"
trim_doctest_flags = True
doctest_flags = doctest.REPORT_UDIFF
intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', 'objects.inv'),
                       'sphinx': ('http://sphinx.pocoo.org/', None),
                      }
intersphinx_cache_limit = 1
