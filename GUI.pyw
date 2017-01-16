from Tkinter import *
import numpy as np
from multiprocessing import Process, Queue
from Queue import Empty
import cv2
import cv2.cv as cv
import tkFont,time
from PIL import Image,ImageTk
class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg = '#c0c0c0')
        self.parent = parent
        self.parent.title('Future ROV Station')
        self.pack(fill = BOTH,expand = 1)
        global state
        state = False
        self.m = 2
        self.s = 0
        self.i = 1
        self.CW()
        
    def CW(self):
        
        font1 = tkFont.Font(size = 30,weight = 'bold')
        self.speedfont = tkFont.Font(family = 'DS-Digital',size = 30)
        self.controlfont = tkFont.Font(family = 'DS-Digital',size = 15)
        self.directionfont = tkFont.Font(size = 45)
        #cam
        self.image_label = Label(master=self)
        self.image_label.place(x = 310,y = 5)
        #speedometer
        # w = Canvas(self,bg = '#c0c0c0',height = 223,width = 505)
        # w.create_arc(20,20,210,210,start = 0, extent = 270,style = ARC,
        #              outline = 'red',dash=(10,3))
        # w.create_arc(10,10,220,220,start = 0, extent = 270, style = ARC,
        #              outline = 'blue')
        # w.create_line(110,110,110,195,arrow = LAST,fill = 'red')
        # w.create_rectangle(125,125,310 ,215,outline = 'blue')
        # w.create_oval(95,95,125,125,outline = 'blue')
        # w.create_arc(220,10,430,220,outline = 'blue',start =180 ,extent =-270,
        #              style = ARC)
        # w.create_arc(230,20,420,210,outline ='red',start = 180,extent = -270,
        #             style = ARC,dash = (10,3))
        # w.create_oval(310,95,340,125,outline = 'blue')
        # w.create_line(325,110,240,110,fill = 'red',arrow = LAST)
        # w.create_text(220,170,text = '000Km/h',fill = 'red',
        #               font = self.speedfont)
        # w.place(x = 760,y= 492)
        # self.slow = Radiobutton(w,text = 'Slow',bg = '#c0c0c0',fg = 'blue',font = self.controlfont)
        # self.slow.place(x = 435,y = 20)
        # self.slow = Radiobutton(w,text = 'Med',bg = '#c0c0c0',fg = 'blue',font = self.controlfont)
        # self.slow.place(x = 435,y = 60)
        # self.slow = Radiobutton(w,text = 'High',bg = '#c0c0c0',fg = 'blue',font = self.controlfont)
        # self.slow.place(x = 435,y = 100)
        self.timerfont = tkFont.Font(family = 'DS-Digital',size = 95)
        #w.create_text(460,190,text = 'N',fill = 'red',font = self.directionfont)
        #Tasks
        self.tasklbl = Label(self,text = 'Tasks',bg ='#c0c0c0',fg = 'blue',
                             font = 36)
        self.tasklbl.place(x = 10,y = 10)
        #read sensor
        self.sep1 = Label(self,text = '_________________________________',bg = '#c0c0c0',
                               fg = 'white',font = 50)
        self.sep1.place(x = 5,y = 405)
        self.sensorlbl = Label(self,text = 'Water conductivity:',bg = '#c0c0c0',
                               fg = 'red',font = 50)
        self.sensorlbl.place(x = 5, y = 430)
        
        self.sensorval = Label(self,text = '0',fg = 'blue',width = 10,relief = RIDGE)
        self.sensorval.place(x = 145,y = 433)

        self.readsensor = Button(self,text = 'Get',fg= 'blue',width = 10)
        self.readsensor.place(x = 225,y = 430)
        #kind
        self.sep2 = Label(self,text = '_________________________________',bg = '#c0c0c0',
                               fg = 'white',font = 50)
        self.sep2.place(x = 5,y = 455)
        self.lengthlbl=Label(self,text = 'Length:',bg ='#c0c0c0',fg = 'red',font = 50 )
        self.lengthlbl.place(x = 5,y = 480)
        self.length = Entry(self)
        self.length.place(x = 70, y = 480)
        self.getlength = Button(self,text = 'Get',fg = 'blue',width = 10)
        self.getlength.place(x = 210,y = 480)
        
        self.widthlbl=Label(self,text = 'Width:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.widthlbl.place(x = 5,y = 510)
        self.width = Entry(self)
        self.width.place(x = 70, y = 510)
        self.getwidth = Button(self,text = 'Get',fg = 'blue',width = 10)
        self.getwidth.place(x = 210,y = 510)

        self.heightlbl=Label(self,text = 'Height:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.heightlbl.place(x = 5,y = 540)
        self.height = Entry(self)
        self.height.place(x = 70, y = 540)
        self.getheight = Button(self,text = 'Get',fg = 'blue',width = 10)
        self.getheight.place(x = 210,y = 540)
        
        self.arealbl=Label(self,text = 'Area:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.arealbl.place(x = 5,y = 570)
        self.area = Entry(self)
        self.area.place(x = 70, y = 570)
        self.getarea = Button(self,text = 'Estimate',fg = 'blue',width = 10)
        self.getarea.place(x = 210,y = 570)
        
        self.massele=Label(self,text = 'Masseles:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.massele.place(x = 5,y = 600)
        self.masseles = Entry(self,width = 15)
        self.masseles.place(x = 100, y = 600)
        self.getmasseles = Button(self,text = 'Estimate',fg = 'blue',width = 10)
        self.getmasseles.place(x = 210,y = 600)
        
        self.allmasselelbl=Label(self,text = 'All Massles:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.allmasselelbl.place(x = 5,y = 630)
        self.allmasseles = Entry(self,width = 15)
        self.allmasseles.place(x = 100, y = 630)
        self.getallmasseles = Button(self,text = 'Estimate',fg = 'blue',width = 10)
        self.getallmasseles.place(x = 210,y = 630)

        self.ship=Label(self,text = 'Ship:',bg ='#c0c0c0',fg = 'red',font = 50)
        self.ship.place(x = 5,y = 670)
        self.shipkind = Entry(self)
        self.shipkind.place(x = 70, y = 670)
        self.getship = Button(self,text = 'Identify',fg = 'blue',width = 10)
        self.getship.place(x = 210,y = 670)

        self.screenshot = Button(self,text = 'Screen shot',fg = 'blue',width = 10)
        self.screenshot.place(x = 320,y = 500)

        self.capvid = Button(self,text = 'Capture video',fg = 'blue',width = 10)
        self.capvid.place(x = 430,y = 500)

        self.photomo = Button(self,text = 'Create phtomosaic',fg = 'blue',width = 20)
        self.photomo.place(x = 540,y = 500)
        
        Label(self,text = 'Informations:',bg = '#c0c0c0',fg = 'red',font = 50).place(x = 960,y = 10)
        self.txt = Text(self,width = 55,height = 37,bg = '#ffff80')
        self.txt.place(x = 970,y = 35)
        
        #logo
        # self.logo = Image.open('logo2.jpg')
        # logo = ImageTk.PhotoImage(self.logo)
        # self.logolbl = Label(self,image = logo)
        # self.logolbl.image = logo
        # self.logolbl.place(x = 320,y = 537)
        #not complete
        tasks = ['1.Measure the lenght,width,and height',
                 '2.Scanning the ship',
                 '3.Create a photomosaic',
                 '4.Determining the type']
        self.tasklist = Listbox(self,bg = '#ffff80',fg='red',font = 20,
                                width = 30)
        for i in tasks:
            self.tasklist.insert(END,i)
        self.tasklist.bind('<<ListboxSelect>>',self.taskEnd)
        self.tasklist.place(x = 20,y = 40)
        
        #Timer
        self.timeval = StringVar()
        self.timer = Label(self,text = '05:00',font = self.timerfont,
                           bg = '#c0c0c0',fg = 'blue',relief = RIDGE )
        self.timer.place(x = 10, y = 250)
        
        self.start = Button(self,text = 'Start',command = self.startTimer,
                            width = 19,fg = 'blue')
        self.start.place(x=10,y=390)
        
        self.stop = Button(self,text = 'Stop',command = self.stopTimer,
                           width = 19,fg = 'red')
        self.stop.place(x=160,y=390)
        self.updatetime()   
    def updatetime(self):
        
        if self.i % 2 == 0:
            self.start.config(text = 'Pause',fg = 'red')
            if self.s == 00:
                if self.m == 0 :self.m = 15
                self.m-=1
                self.s =60
            self.s -= 1
            if self.s < 10:
                self.timer.config(text = '0%d:0%d'%(self.m,self.s))
                if self.m == 0 :self.timer.config(fg = 'red')
            else :self.timer.config(text = '0%d:%d'%(self.m,self.s),fg = 'blue')
        else:self.start.config(text = 'Start',fg = 'blue')
        self.after(1000, self.updatetime)
    def startTimer(self):
        self.i+=1
        
    def stopTimer(self):
        self.i = 1
        self.start.config(text = 'Start',fg = 'blue')
        self.m = 5
        self.s = 0
        self.timer.config(text = '0%d:0%d'%(self.m,self.s))
        
    def taskEnd(self,task):
        sender = task.widget
        taskidx = sender.curselection()
        self.tasklist.delete(taskidx)
        #tkinter GUI functions----------------------------------------------------------
    def quit_(self, process):
        process.terminate()
        self.destroy()

    def update_image(self,image_label, queue):
        frame = queue.get()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        a = Image.fromarray(im)
        b = ImageTk.PhotoImage(image=a)
        image_label.configure(image=b)
        image_label._image_cache = b  # avoid garbage collection
        self.update()

    def update_all(self, image_label, queue):
        self.update_image(image_label, queue)
        self.after(0, func=lambda: update_all(self, image_label, queue))

#multiprocessing image processing functions-------------------------------------
    def image_capture(self,queue):
        vidFile = cv2.VideoCapture(0)
        while True:
            try:
                flag, frame=vidFile.read()
                if flag==0:
                    break
                queue.put(frame)
                cv2.waitKey(20)
            except:
                continue



def main():
    queue = Queue()
    print 'queue initialized...'
    root = Tk()
    #app = GUI()
    print 'GUI initialized...'
    #image_label = self.Label(master=root)# label for the video frame
    #image_label.pack()
    print 'GUI image label initialized...'
    p = Process(target=app.image_capture, args=(queue,))
    p.start()
    print 'image capture process has started...'
    # quit button
    quit_button = Button(master=root, text='Quit',command=lambda: GUI.quit_(root,p))
    quit_button.pack()
    print 'quit button initialized...'
    app = GUI(root)
    # setup the update callback
    root.after(0, func=lambda: app.update_all(app.image_label, queue))
    print 'root.after was called...'
    #root.mainloop()
    print 'mainloop exit'
    p.join()
    print 'image capture process exit'
    #root = Tk()
    root.geometry('1270x720+0+0')
    
    root.mainloop()

    
if __name__ == '__main__':main()
                  
