"""
    WualaCleaner: tool to clean up "fotos-familie" archive
    WualaCleaner.py is copyright 2013,2014 Jeroen Doggen.
"""

import os
import sys
import shutil

# TODO: check for un-changed folders and ignore these: (re-use code from 'LaTeX Handouts Builder)

class MultimediaShrinker:
    """ Contains all the code for the tool """

    def __init__(self):
        self.thefile = ""
        self.filetype = ""
        self.scriptpath = os.getcwd()
        self.inputfolder = self.scriptpath + "/input_original"
        self.outputfolder = self.scriptpath + "/output_lowres2"
        self.infos = []
        self.itemcounter = 0

    def run(self):
        """Run the main program"""
        self.getInfo(self.inputfolder)
        self.create_folders()
        """for every file"""
        self.get_type(self.thefile)
        self.define_work(self.thefile, self.filetype)
        self.convert(self.thefile, self.filetype)
        self.report(self.thefile, self.filetype)

    def getInfo(self, currentDir):
        for item in os.walk(self.inputfolder, "*"):
            self.infos.append(item)
            self.itemcounter = self.itemcounter + 1
        for item in (self.infos):
            print(item)
        #print(self.infos)
        print(self.itemcounter)

    def report(self, filename, filetype):
        """Calculate the progress, file size, ..."""
        pass

    def create_folders(self):
        """Duplicate the input folder structure in the output folder"""
        pass
        #shutil.copytree(self.inputfolder, self.outputfolder)
        #shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)

    def get_type(self, filename):
        """Detect the file type (image/video,...)"""
        pass

    def define_work(self, filename, filetype):
        """Analyse the file and decide what to do"""
        pass

    def convert(self, filename, filetype):
        """Convert the file to a 'lowres' version"""
        pass

    def get_size(self, start_path='.'):
        """ Calculate folder size """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for inputfile in filenames:
                filepointer = os.path.join(dirpath, inputfile)
                total_size += os.path.getsize(filepointer)
        return float(total_size)

if __name__ == "__main__":
    Shrinker = MultimediaShrinker()
    sys.exit(Shrinker.run())
