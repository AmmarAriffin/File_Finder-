# File_Finder-

Made a GoogleSearch GUI style Listbox for tkinter. This is to make it easier to sift through a company Windows file explorer with massive branches. 

I use this code to go to a certain folder depending on the category (customer, place, time) and find the right product or sub-place according to the name of the directory.

To set to executable. I used pyinstaller .

~~~
pip install pyinstaller
pyinstall --onefile --noconsole CustomerFileFinder.py
~~~


There are 3 python files:

1. CustomerFileFinder.py 	- Template on how I used it
2. Explorer.py				- Windows File Explorer specific class
3. GoogleSearchGUI.py		- Google Search style listbox for tkinter
