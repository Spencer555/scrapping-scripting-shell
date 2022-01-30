# # sys module
# import subprocess
# import sys
#
#
# print(sys.version)
# # current py version
#
#
# print(sys.argv)
# #list of commanding arguments passed to a script
#
#
# # stderr - store error messages, stdint - accept user input, stdout print output, exit - end a python script
#
# # os module
# # interact with the os primary use is to create folders move folders copy them or change working directory
#
# import os
#
# print(os.getcwd())
# # get current working directory
#
# # os.chdir("")
# # change current working directory
#
#
# os.mkdir('Edureka')
# # create a folder
#
#
# os.rmdir('Edureka')
# # delete a file
#
#
# os.remove('text.txt')
# # to delete a file
#
#
#
# # os.path
# os.path.join("curent path", "path u want to join to the current path")
#
#
# os.path.split("path u want to split")
# # this split it into the path and current folder e.g. D:\spl\python_scription\osmodule would become splited into D:\spl\python_scrpt osmodule
#
#
# os.path.exists('path')
# # check if path exists


# subprocess module
# this lets u interacts with the os and let u pass information in and out of them and gets return codes
# subprocess.call(write the process u want hereit runs the command waith for it to finish and get he return code)

# math module
# perform math functions
#
# import math
#
# math.pi #value of pi
# math.e #value of constance e
# math.degrees(0.1) #convert an angle from radus to degeree
# math.acos(0.5) #get cos of a number
# math.asin(0.5) #get sin of a number
# math.atan(0.5) #get tan of a number
# math.exp(2) #this returns e raised to the power 2
# math.log(10, 10) #log with one argument u can return x to the base of the num or with 2 arguments to the base of the arguments


# random module
# import random
# random.randrange(10) #not more than the number entered
# random.randrange(0, 10, 2)#means start at 0 to 10 and increase or decrease in twos
# random.randint(0,20) #random integer between 0 to 20
#
# #datetime module
# import datetime
#
# datetime.date.today()#get current time
# now = datetime.datetime.today()
# other= datetime.datetime(2020,12,12, 17, 59)
# print(now - other)


# json module

employee_data =''' {
 "people" : [
  {
  "name" :"Sept" ,
  "email":["spl@gmail.com", "naa@gmail.com"],
  "married":true
  },
  {
  "name" :"Sept" ,
  "email":["spl@gmail.com", "naa@gmail.com"],
  "married":true
  },
  {
  "name" :"Sept" ,
  "email":["spl@gmail.com", "naa@gmail.com"],
  "married":true
  }
]
}
'''

# print(employee_data)
#
# import json
# #passing it to python loading it into json
# data=json.loads(employee_data)
#
# #to dump a json file into file or output it as a string
# data=json.loads(employee_data)
#
# print(data)


#gui
import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

# create a tk object
root = Tk()

# root.title('First gui using python')
# ttk.Button(root, text="Hello Spencer Lewis").grid()
# root.mainloop() #close this window
#

#basic components in a gui app
# labels
# buttons
# frame
# grid
# radio buttons
# check buttons


#create a frame - a widget which surround other widgets
#
# frame =Frame(root)
# labelText=StringVar()
# #
# label = Label(frame, textvariable= labelText)
# button=Button(frame, text="Hey, i am a button")
#
# labelText.set('Hey this is how u change a label text')
#
# label.pack()#define how a component are arragned in a window
# button.pack()
# frame.pack()
#
# #pack everything u used
#
# #close
# root.mainloop()


# frame = Frame(root)
# Label(frame, text="Hey!").pack()
# Button(frame, text="Click me").pack(side=LEFT, fill=Y) #fill where it would be streteched
# Button(frame, text="Click me 1").pack(side=RIGHT, fill=X) #fill where it would be streteched
# Button(frame, text="Click me 2").pack(side=TOP, fill=Y) #fill where it would be streteched
# Button(frame, text="Click me 3").pack(side=LEFT, fill=Y) #fill where it would be streteched
#
# frame.pack()
# root.mainloop()

# #
# Label(root, text='Name').grid(row=0, column=0, sticky=N)   # sticky direction can be N for north and first capital for other directions #this a geometry manager to structure diff component in the window
# Entry(root, width=50).grid(row=0, column=1)
#
# Button(root, text='Submit').grid(row=0, column=5)
#
#
#
# Label(root, text='Gender').grid(row=1, column=0, sticky=N)
# Radiobutton(root, text="F", value=1).grid(row=1, column=1, sticky=N)
# Radiobutton(root, text="M", value=2).grid(row=1, column=2, sticky=N)
#
# Label(root, text='Courses').grid(row=1, column=0, sticky=N)
# Checkbutton(root, text="Java").grid(row=3, column=1, sticky=N)
# Checkbutton(root, text="Python").grid(row=4, column=1, sticky=N)
# Checkbutton(root, text="Php").grid(row=5, column=1, sticky=N)
#
# root.mainloop()

def square(event):
    a=int(num1.get())
    b=a*a
    #delete the previous results from screen
    result.delete(0,'end')
    #passing answert to the result screen
    result.insert(0,b)

root=Tk()
Label(root, text="Find the square of a number").pack()
num1= Entry(root)
num1.pack(side=LEFT)

btn= Button(root, text="Square to")
btn.bind("<Button-1>", square)
btn.pack(side=LEFT)

result=Entry(root)
result.pack(side=LEFT)
root.mainloop()