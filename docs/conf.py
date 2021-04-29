import builtins
import configparser
import importlib
from pathlib import Path
import pkg_resources
import sys

# Make it possible for our code to tell that it is running under Sphinx.
# See https://stackoverflow.com/a/65147676/167694
builtins.__sphinx_build__ = True


sys.path.insert(0, str(Path(__file__).parents[1]))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'celery.contrib.sphinx',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']
source_parsers = {}

# The master toctree document.
master_doc = 'index'
