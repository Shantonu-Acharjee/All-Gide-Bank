'''

from tkinter import *
root = Tk()
theLabel = Label(root, text='Shantonu Acharjee')
theLabel.pack()
root.mainloop()

'''

# Video 1 Done.

'''

from tkinter import *
root = Tk()

frame = Frame(root)

button1 = Button(frame, text='Button1')
button2 = Button(frame, text='Button2')
button3 = Button(frame, text='Button3')

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
frame.pack()


bottomFrame = Frame(root)
button4 = Button(bottomFrame, text= 'Button4')


button4.pack()
bottomFrame.pack(side= BOTTOM)
root.mainloop()

'''


'''

from tkinter import *

from sympy import root
root = Tk()
frame = Frame(root, width=300, height=300)
frame.pack()
root.mainloop()

'''

# Video 2 Done.

"""

from tkinter import *

root = Tk()
one = Label(root, text='One', bg = 'red')
tow = Label(root, text='Tow', bg = 'green')
three = Label(root, text='Three', bg = 'blue')

one.pack(fill = X)
tow.pack()
three.pack(side= LEFT, fill= Y)
root.mainloop()

"""

# Video 3 Done.
