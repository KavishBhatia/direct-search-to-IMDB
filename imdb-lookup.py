from Tkinter import *
import tkMessageBox
import sys
import urllib
import json
import webbrowser

def finder(name):
    year=0
    for y in range(1900,2014):
        if str(y) in name:
            name = name.replace(str(y)," ")
            year = y
            break
    for value in replace:
        name = name.replace(value," ")

    name=name.lstrip()
    name=name.rstrip()
    
    if year!=0:
        url = "http://www.omdbapi.com/?t="+name+"&y="+str(year)
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        if jsonvalues["Response"]=="True":
            movieurl = "http://www.imdb.com/title/" + jsonvalues['imdbID']
            webbrowser.open_new_tab(movieurl)
    else:
        url = "http://www.omdbapi.com/?t="+name
        response = urllib.urlopen(url).read()
	jsonvalues = json.loads(response)
	if jsonvalues["Response"]=="True":
            movieurl = "http://www.imdb.com/title/" + jsonvalues['imdbID']
            webbrowser.open_new_tab(movieurl)


master = Tk()
e = Entry(master,bd=5)
e.pack()

e.focus_set()
master.geometry("200x100+600+300")
#tkMessageBox.showinfo(title="Enter Movie Name")
def callback():
    a = e.get() # This is the text you may want to use later
    file = a.split("\\")[-1]
    finder(file)
    master.destroy()

b = Button(master, text = "OK", width = 10, command = callback)
b.pack(side=BOTTOM)

mainloop()
