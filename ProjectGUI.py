from tkinter import *
from DrawersEX  import *
from Read import *
from testdrawer import *
import threading, time

g_SHOULD_READ = True

#setup
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg ="white")
        parent.attributes("-fullscreen", True)
        self.drawer_stats = [False, False, False]
        self.setupGUI()
        
    def setupGUI(self):
        MyLabel = Label(self, text="Select a Drawer to Open or Close", anchor=CENTER, bg="white", height=2,\
                             width=15, font=("TextGyreAdventor", 30))
        MyLabel.grid(row=0,column=0, columnspan=3, sticky=E+W+N+S)

        self.display = Label(self, text="", anchor=CENTER, bg="white", height=2,\
                             width=15, font=("TextGyreAdventor", 40))
        self.display.grid(row=1,column=0, columnspan=3, sticky=E+W+N+S)

        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(2):
            Grid.columnconfigure(self, col, weight=1)
        #Button layout is as follows currently
        #   "Select a Drawer to Open or Close"
        # [text to indicate drawer opening or closing]
        #   Open 1          Close 1
        #   Open 2          Close 2
        #   Open 3          Close 3

        #Open 1
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/open.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("1"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)
 
        #Open 2
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/open2.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("2"))
        button.image = img
        button.grid(row=3, column=0, sticky=N+S+E+W)

        #Open 3
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/open3.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("3"))
        button.image = img
        button.grid(row=4, column=0, sticky=N+S+E+W)

        #Close 1
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/close.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("-1"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)
        
        #Close 2
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/close2.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("-2"))
        button.image = img
        button.grid(row=3, column=1, sticky=N+S+E+W)

        #Close 3
        img = PhotoImage(file="/home/pi/Desktop/our pi things/testimg/close3.gif")
        button = Button(self, bg="white", image=img,borderwidth=0, highlightthickness=0,\
                       activebackground="white", command=lambda:self.process("-3"))
        button.image = img
        button.grid(row=4, column=1, sticky=N+S+E+W)

        
            
        #pack GUI
        self.pack(fill=BOTH, expand=1)

    def process(self, button):
        if (button == "1"):
            self.display["text"] = "Drawer 1 Opening"
            # check if drawer 1 is open
            if self.drawer_stats[0] == True:
                # Close Drawer
                self.display["text"] = "Drawer 1 Closing"
                Drawer1open()
                # set flag to closed
                self.drawer_stats[0] = False
            else:
                # open drawer
                Drawer1close()
                # set flag to open
                self.drawer_stats[0] = True
        if (button == "2"):
            self.display["text"] = "Drawer 2 Opening"
            # check if drawer 2 is open
            if self.drawer_stats[1] == True:
                # Close Drawer
                self.display["text"] = "Drawer 2 Closing"
                Drawer2close()
                # set flag to closed
                self.drawer_stats[1] = False
            else:
                # open drawer
                Drawer2open()
                # set flag to open
                self.drawer_stats[1] = True
        if (button == "3"):
            self.display["text"] = "Drawer 3 Opening"
            # check if drawer 3 is open
            if self.drawer_stats[2] == True:
                # Close Drawer
                self.display["text"] = "Drawer 3 Closing"
                Drawer3close()
                # set flag to closed
                self.drawer_stats[2] = False
            else:
                # open drawer
                Drawer3open()
                # set flag to open
                self.drawer_stats[2] = True
        if (button == "-1"):
            self.display["text"] = "Drawer 1 Closing"
            Drawer1close()
        if (button == "-2"):
            self.display["text"] = "Drawer 2 Closing"
            Drawer2close()
        if (button == "-3"):
            self.display["text"] = "Drawer 3 Closing"
            Drawer3close()


def readNFC(p, reader):
    print("STARTING READING THREAD...")
    while g_SHOULD_READ:
        nfc = readcard(reader)
        p.process(nfc)
        time.sleep(2)
    print("g_SHOULD_READ=FALSE")

#########################################
try:
    reader = SimpleMFRC522()
    window = Tk()
    window.title("Drawers v1.4")
    p = MainGUI(window)

    read_thread = threading.Thread(target=readNFC, args=[p, reader])
    read_thread.start()
    
    window.mainloop()
except KeyboardInterrupt:
    GPIO.cleanup()
    g_SHOULD_READ = False
    read_thread.join()
    print("Clean")
