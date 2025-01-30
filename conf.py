# Configuration file for Sphinx documentation builder.
#
# This file contains a selection of the most common options for setting up a website using a Sphinx template. 
# See the full documentation here:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "Benchling resources"
copyright = "2024, DTU Biosustain, Informatics Platform, Research Data Management Team"
#author = "Ester Milesi"


# -- General configuration ---------------------------------------------------

# Enable MyST-NB, which allows Sphinx to render Markdown files with notebook (Jupyter) support.
# Enable "sphinx_new_tab_link", which automatically makes links open in a new tab.
extensions = [
    "myst_nb", 
    # "sphinx_design", # https://sphinx-design.readthedocs.io/en/sbt-theme/
    # "sphinx_copybutton", # https://sphinx-copybutton.readthedocs.io/
    "sphinx_new_tab_link",
    "sphinx_design", #This extension enables the hiding of answers in the FAQ page (allow us to use {dropdown})
    # "sphinxcontrib.video", # This extension allows video embedding without YouTube https://sphinxcontrib-video.readthedocs.io/en/latest/index.html (not working)
    
]

templates_path = ["_templates"]
# Website pages can only be built from percent notebooks and markdowns files.
# We need to exclude some files/patterns included in the repository.

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
    "**/.ipynb_checkpoints/*",
    "jupyter_execute",
    "conf.py",
    ".venv",
]


# -- Jupiter Notebook related settings -----------------------------------------------

# add notebooks (myst-nb extension)
#  https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "auto"

myst_enable_extensions = ["dollarmath", "amsmath"]

# Plolty support through require javascript library
# https://myst-nb.readthedocs.io/en/latest/render/interactive.html#plotly
html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"
]

# https://myst-nb.readthedocs.io/en/latest/configuration.html
# Execution
nb_execution_raise_on_error = True
# Rendering
nb_merge_streams = True

# https://myst-nb.readthedocs.io/en/latest/authoring/custom-formats.html#write-custom-formats
nb_custom_formats = {
    ".py": ["jupytext.reads", {"fmt": "py:percent"}]
}


# -- Options for HTML output -------------------------------------------------

# 2. Select a tempalate
# ! you might need additional dependencies in requirements.txt
# browse available themes: https://sphinx-themes.org/


# The theme to use for HTML and HTML Help pages.  
# See the documentation for a list of existing themes:
# https://github.com/executablebooks/MyST-NB/blob/master/docs/conf.py

#OLD THEME "sphinx_book_theme"

#THEME (AND LOGO) 

#_static directory is typically where Sphinx expects custom static assets like images
#html_theme = 'press'
html_theme = 'piccolo_theme'
# html_logo = "_static/logo-wide.svg" #check where is _static
# html_favicon = "_static/logo-square.svg"

html_theme_options = {
    "show_theme_credit": False
}

html_title = 'Benchling resources' 

# THEME options
# html_theme_options = {
#     "github_url": "https://github.com/biosustain",
#     "repository_url": "https://github.com/biosustain/benchling-resources",
#     # "repository_branch": "main",
#     # "home_page_in_toc": True,
#     # # "path_to_docs": "docs",
#     # "show_navbar_depth": 1,
#     # # "use_edit_page_button": True,
#     # # "use_repository_button": True,
#     # "use_download_button": True,
#     # #"launch_buttons": {
#     # #    "colab_url": "https://colab.research.google.com"
#     # #    #     "binderhub_url": "https://mybinder.org",
#     # #   #     "notebook_interface": "jupyterlab",
#     # #},
#     # "navigation_with_keys": False,
# }
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css'] # Fixes ability to center text on the screen


