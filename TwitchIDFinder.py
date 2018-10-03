import tkinter as tk
import time
import os

from twitch import TwitchClient

class Application():
    def __init__(self,width,height, master = None):
        self.width = width
        self.height = height
        master.geometry('{}x{}'.format(self.width,self.height))
        self.button = tk.Button(master,text = 'Get ID', command = self.changeText)
        self.label = tk.Label(master,text ='')

        self.client = TwitchClient(client_id = '4xnr6ntfelm49s3b3ym1e5heo01cph')
        #self.channel = self.client.search.channels('Lady_Juleczka')
        self.editext = tk.Entry(master)


        self.button.grid(column = 0, row = 0)
        self.label.grid(column = 1, row = 0)
        self.editext.grid(column = 0,row = 1)

    def changeText(self):
        #self.label.config(text = 'Patryk Weber')
        self.str = self.editext.get()
        print(str)
        self.channelname = self.client.search.channels(self.str)
        self.label.config(text = "ID: "+str(self.channelname[0]['id']))


if __name__ =='__main__':
    root = tk.Tk()
    app = Application('400','200', root)

    root.mainloop()
