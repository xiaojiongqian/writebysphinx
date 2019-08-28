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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'writebysphinx'
copyright = '2019, Vik'
author = 'Vik'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.graphviz',
    #'rst2pdf.pdfbuilder',
    'sphinxcontrib.plantuml']

# index - master document
# write_by_sphinx - name of the generated pdf
# Write by Sphinx - title of the pdf
# Vik Qian - author name in the pdf
#pdf_documents = [('index', u'write_by_sphinx', u'Write by Sphinx', u'Vik Qian')]

# 设置 graphviz_dot 布局风格
# dot 默认布局方式，主要用于有向图
# neato 基于spring-model(又称force-based)算法   基于斥力+张力的布局
# twopi 径向布局
# circo 圆环布局
# osage
# fdp 用于无向图
# sfdp 用于无向图
graphviz_dot = 'dot'

# 设置 graphviz_dot_args 的参数，这里默认了默认字体
graphviz_dot_args = ['-Gfontname=Georgia', 
                     '-Nfontname=Georgia',
                     '-Efontname=Georgia']
# 输出格式，默认png，这里我用svg矢量图
graphviz_output_format = 'svg'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# 设置 plantuml.jar 路径
currentpath = os.getcwd() + '/'
plantuml = 'java -jar ' + currentpath + 'plantuml.jar'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
# html_theme_path = ['_themes']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }