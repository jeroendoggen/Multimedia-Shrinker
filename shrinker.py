"""
    WualaCleaner: tool to clean up "fotos-familie" archive
    WualaCleaner.py is copyright 2013,2014 Jeroen Doggen.
"""

import os
import sys
import shutil


SCRIPTPATH = os.getcwd()
INPUTFOLDER = SCRIPTPATH + "/input_original"
OUTPUTFOLDER = SCRIPTPATH + "/output_lowres"


def run():
    """Run the main program"""
    create_folders()
    for (everyfile)
        get_type()
        define_work()
        convert()
        report()

def report():
    """Calculate the progress, file size, ..."""

def create_folders():
    """Duplicate the input folder structure in the output folder"""

def get_type(filename):
    """Detect the file type (image/video,...)"""
    pass

def convert(filename, filetype):
    """Convert the file to a 'lowres' version"""
    pass

def define_work(filename)
    """Analyse the file and decide what to do"""
    pass

def get_size(start_path='.'):
    """ Calculate folder size """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for inputfile in filenames:
            filepointer = os.path.join(dirpath, inputfile)
            total_size += os.path.getsize(filepointer)
    return float(total_size)

if __name__ == "__main__":
    sys.exit(run())
