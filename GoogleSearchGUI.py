from tkinter import StringVar, Listbox, ttk


class GoogleSearchListBox():
    def __init__(self, root, dropdownData=[]):
        self.variable = StringVar()
        font = ("Arial", 12)
        self.entry = ttk.Entry(root, textvariable=self.variable, font=font)
        self.dropdown = Listbox(root, width=50, font=font)
        self.dropdownData = dropdownData
        self.isKeyPress = False
        self.defaultSetup()

    def defaultSetup(self):
        self.entry.pack()
        self.bindFunctiontoEntry(self.updateDropdownFromEntry)
        self.updateDropdownFromEntry()
        self.setupKeyboardDropdownBehaviour()

    def setupKeyboardDropdownBehaviour(self):
        self.dropdown.bind("<FocusIn>", self.onKeyPressEvent)
        self.dropdown.bind("<Key>", self.onKeyPressEvent)
    
    def updateDropdownDataFromDatabase(self, data):
        self.dropdownData = data

    def bindFunctiontoEntry(self, functionName):
        self.variable.trace_add('write', lambda *args : functionName())
    
    def updateDropdownFromEntry(self):
        typed = self.entry.get().lower()

        if typed:
            matches = [option for option in self.dropdownData if typed in option.lower()]
        else:
            matches = self.dropdownData

        self.clearAllDropdownOptions()
        self.insertDropdownOptions(matches)
        self.appearDropdown()
    
    def insertDropdownOptions(self, match_list):
        for option in match_list:
            self.dropdown.insert('end', option)

    def clearAllDropdownOptions(self):
        self.dropdown.delete(0, 'end')

    def bindFunctiontoDropdown(self, functionName : callable):
        self.dropdown.bind('<<ListboxSelect>>', lambda *args : functionName() if not self.isKeyPress else self.resetKeyPress())
        self.dropdown.bind('<Return>', lambda *args : functionName())

    def dissappearDropdown(self):
        self.clearAllDropdownOptions()
        self.dropdown.pack_forget()
    
    def selectFromDropdown(self):
        selected = ""
        if index := self.dropdown.curselection():
            selected = self.dropdown.get(index)
            self.variable.set(selected)
        return selected

    def appearDropdown(self):
        self.dropdown.pack()

    def getEntryValue(self):
        return self.variable.get()
    
    def dissappearEntry(self):
        self.clearEntry()
        self.entry.pack_forget()

    def appearEntry(self):
        self.entry.pack()
        
    def appear(self):
        self.appearEntry()
        self.appearDropdown()

    def dissappear(self):
        self.dissappearEntry()
        self.dissappearDropdown()

    def resetKeyPress(self):
        self.isKeyPress = False

    def onKeyPressEvent(self, event):
        self.isKeyPress = True
        if not self.dropdown.curselection():
            self.dropdown.select_set(0)

    def clearEntry(self):
        self.variable.set("")