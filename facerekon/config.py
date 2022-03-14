from os import mkdir
from os.path import exists, join
from pathlib import Path


__title__ = "FaceRekon"
__description__ = "Face recognition-based Photo naming API"
__version__ = "1.0.0"

CUR_ABSPATH = Path(__file__).parent.absolute()
STATIC = join(CUR_ABSPATH, 'static')
IMAGES_UNNAMED = join(CUR_ABSPATH, 'images-unnamed')
IMAGES_NAMED = join(CUR_ABSPATH, 'images-named')

if not exists(IMAGES_NAMED):
    mkdir(IMAGES_NAMED)
if not exists(IMAGES_UNNAMED):
    mkdir(IMAGES_UNNAMED)
