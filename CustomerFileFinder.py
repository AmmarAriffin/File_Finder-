import tkinter as tk
from Explorer import ExplorerPointer
from GoogleSearchGUI import GoogleSearchListBox


MainDirectory = "./test"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.processor = ExplorerPointer(MainDirectory)
        
        # Get directories in the path
        MainDropdownData = self.processor.fetchAllDirectories()

        self.FirstSearch = GoogleSearchListBox(self.root, MainDropdownData)
        self.SecondSearch = GoogleSearchListBox(self.root)

        self.SecondSearch.dissappear()

        self.FirstSearch.bindFunctiontoEntry(self.SecondSearch.dissappear)
        self.FirstSearch.bindFunctiontoDropdown(self.getSelectedDirectory_SubDirectory)
        self.SecondSearch.bindFunctiontoDropdown(self.openDirectory)

    def getSelectedDirectory_SubDirectory(self):
        SelectedDir = self.FirstSearch.selectFromDropdown()
        self.processor.resetToOriginalPath()
        self.processor.gotoNextPath(SelectedDir)
        self.SecondSearch.updateDropdownDataFromDatabase(self.processor.fetchAllDirectories())
        self.FirstSearch.dissappearDropdown()
        self.SecondSearch.appear()
    
    def openDirectory(self):
        selected = self.SecondSearch.selectFromDropdown()
        self.processor.resetToOriginalPath()
        self.processor.gotoNextPath(self.FirstSearch.getEntryValue())
        self.processor.gotoNextPath(selected)
        self.SecondSearch.appearDropdown()
        self.processor.openCurrentDirectory()
    
    def mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.mainloop()