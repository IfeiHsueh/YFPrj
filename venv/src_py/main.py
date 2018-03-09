"""

"""
import sys
import getopt
from RSimage import RSimage
from MovingWindow import MovingWindow
from image_factory_ih import ImageFactory


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def execute():
    img = RSimage('../data/09AUG11PILOT.tif', 1)
    mw = MovingWindow('rectangle', 3, 0, img)
    ifac = ImageFactory(img, mw)
    ifac.execute_mwindow()

def main(argv=None):
    if argv is None:
        argv = sys.argv

    execute()

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


print('Hello')

if __name__ == '__main__':
    sys.exit(main())