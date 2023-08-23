
import os
import platform
import subprocess

class ExplorerPointer:
    def __init__(self, directory_path):
        self.original_dir = directory_path
        self.current_dir = self.original_dir

    def gotoNextPath(self, path):
        self.current_dir = self.getNextPath(path)

    def resetToOriginalPath(self):
        self.current_dir = self.original_dir

    def fetchAllDirectories(self):
        return os.listdir(self.current_dir)

    def isDirectory(self, path):
        return os.path.isdir(self.getNextPath(path))

    def getNextPath(self, path):
        return os.path.join(self.current_dir, path)

    def openCurrentDirectory(self):
        if platform.system() == 'Windows':
            os.startfile(self.current_dir)
        elif platform.system() == 'Darwin':  # Darwin is the correct term for MacOS
            subprocess.call(['open', self.current_dir])
        else:
            print("Unsupported platform")