from distutils.core import setup
import py2exe, sys

def finish():
    sys.argv.append("py2exe")
    setup(Windows=["C:\Python27\Mangafox\MangaFoxScript.pyw"])
