import appdirs
import os

# Per contract with Sphinx-Gallery, this method must be available at top level
from pyvista.utilities.sphinx_gallery import _get_sg_image_scraper

from ansys.mapdl.core._version import __version__
from ansys.mapdl.core.archive import (Archive, write_cmblock, write_nblock,
                                      save_as_archive)
from ansys.mapdl.core.cell_quality import quality
from ansys.mapdl.core.common import read_binary
from ansys.mapdl.core.convert import convert_script
from ansys.mapdl.core.launcher import launch_mapdl, change_default_ansys_path
from ansys.mapdl.core.misc import Report, _configure_pyvista, _check_has_ansys
from ansys.mapdl.core.examples.downloads import *
from ansys.mapdl.core.launcher import get_ansys_path

_HAS_ANSYS = _check_has_ansys()

# Setup data directory
try:
    USER_DATA_PATH = appdirs.user_data_dir('ansys_mapdl_core')
    if not os.path.exists(USER_DATA_PATH):  # pragma: no cover
        os.makedirs(USER_DATA_PATH)

    EXAMPLES_PATH = os.path.join(USER_DATA_PATH, 'examples')
    if not os.path.exists(EXAMPLES_PATH):  # pragma: no cover
        os.makedirs(EXAMPLES_PATH)

except:  # pragma: no cover
    pass

# set pyvista defaults
_configure_pyvista()
