# -*- coding: utf-8 -*-
#
# StackStorm documentation build configuration file, created by
# sphinx-quickstart on Tue Oct  7 21:52:49 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../st2'))

sys.path.append(BASE_DIR)
import info

# Include Python modules for all the st2components
st2_components_paths = glob.glob(ROOT_DIR + '/st2*')
for module_path in st2_components_paths:
    sys.path.append(module_path)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('./_themes'))

from st2common import __version__

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',

    # Add theme as extension so sitemap.xml is generated
    'sphinx_rtd_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# General information about the project.
project = info.project
copyright = info.copyright
author = info.author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# the __version__ is 0.8.1 or 0.9dev
# the version is short 0.8 version, to refer docs.
version = '.'.join(__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = __version__
# The complete list of current StackStorm versions.
release_versions = ['3.7', '3.6', '3.5', '3.4', '3.3', '3.2', '3.1', '3.0', '2.10', '2.9', '2.8', '2.7', '2.6', '2.5', '2.4', '2.3', '2.2', '2.1', '2.0', '1.6', '1.5', '1.4', '1.3', '1.2', '1.1', '0.13', '0.12', '0.11', '0.9', '0.8']

# Some loveliness that we have to do to make this work.  Otherwise it defaults to contents.rst
master_doc = info.master_doc


def previous_version(ver):
    if ver.endswith('dev'):
        return release_versions[0]
    major_minor = '.'.join(ver.split('.')[:2])
    if major_minor in release_versions:
        idx = release_versions.index(major_minor)
        if idx + 1 < len(release_versions):
            return release_versions[idx + 1]
    # Better than broken return some value. Control flow should not reach this point.
    return "unknown"

# The short versions of two previous releases, e.g. 0.8 and 0.7
version_minus_1 = previous_version(version)
version_minus_2 = previous_version(version_minus_1)

# extlink configurator sphinx.ext.extlinks
extlinks = {
    'github_st2': ('https://github.com/StackStorm/st2/tree/master/%s', None),
    'github_exchange':
        ('https://github.com/StackStorm-Exchange/%s', None),
    'web_exchange':
        ('https://exchange.stackstorm.org/#%s', None),
}

# Inserted at the bottom of all rst files.
# Use for variables substitutions

if tags.has('enterprise'):
    print("Building EWC docs")
    product_replace = "\n.. |st2| replace:: EWC\n.. |fullname| replace:: Extreme Workflow Composer"
else:
    print("Building StackStorm docs")
    product_replace = "\n.. |st2| replace:: StackStorm\n.. |fullname| replace:: StackStorm"

rst_epilog = """
%s
.. _exchange: https://exchange.stackstorm.org/
.. |ewc| replace:: Extreme Workflow Composer
.. |ipf| replace:: IP Fabric Automation Suite
""" % product_replace

# Show or hide TODOs. See http://sphinx-doc.org/ext/todo.html
todo_include_todos = True

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# dzimine: '**/._*' exclues files my Sublime creates on NFS mount.
exclude_patterns = [
    '**/._*',
    '**/__*', '__*',  # Naming convension for include files
    '_includes/*',  # includes files
    'todo.rst',
    'known_security_issues.rst',

]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, Sphinx will warn about all references where the target cannot be
# found. Default is False. You can activate this mode temporarily using the
# -n command-line switch.
nitpicky = True

# XXX: temp fix before we figure how to make autodocs work
nitpick_ignore = [
    ('py:class', 'st2actions.runners.pythonrunner.Action'),
    ('py:class', 'st2common.runners.base_action.Action'),
    ('py:class', 'KeyValuePair')]

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
if "READTHEDOCS" not in os.environ:
    html_theme_options = {
        'base_url': info.theme_base_url,
        'canonical_url': info.theme_base_url
    }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
html_theme_path = ["_themes", ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []
html_extra_path = ['_redirects']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = info.htmlhelp_basename

# Variables to be used by templates
if "READTHEDOCS" not in os.environ:
    html_context = {
        'github_user': info.github_user,
        'github_repo': info.github_repo,
        'github_version': info.github_version,
        'conf_py_path': '/docs/source/',
        'display_github': True,
        'source_suffix': source_suffix,
        'versions': [
            ('latest', '%slatest' % info.base_url),
            (version, '%s%s' % (info.base_url, version)),
            (version_minus_1, '%s%s' % (info.base_url, version_minus_1)),
            (version_minus_2, '%s%s' % (info.base_url, version_minus_2)),
        ],
        'current_version': version,
        'css_files': [
            '_static/theme_overrides.css',
            ],
    }


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = info.latex_documents

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code,     itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = info.man_pages

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = info.texinfo_documents

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/2': None}

autoclass_content = 'both'
