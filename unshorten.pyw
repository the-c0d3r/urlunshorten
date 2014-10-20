import re, urllib2, tkMessageBox
from Tkinter import *

#$!!!!!!!!!!!!!!!!!!!!!
# Url Unshortener.py
# Version : Beta
# Author : Anubis/Zero
# Written in : Python 2.7
# Date : 19/9/2013 Thursday
# Made in : Myanmar

# New version will have the ability to check if the site is safe
# or not in virustotal, and other search engines
# I just added GUI for the url unshorten inside automater

__author__ = 'Anubis/Zero'
__version__ = 'Beta'

class Unshortener(Frame):

    def __init__ (self,parent):
        Frame.__init__(self,parent,background="white")
        self.parent = parent
        self.Frame = Frame
        self.initate_GUI()

    def ad_focus_unshorten(data):
        ad_focus_pattern = re.compile('[\s|\t]+var\sclick_url\s\=\s?\"([http|https]?[www]?.+)\"\;')
        link = ad_focus_pattern.findall(data)
        if link != '':
            txt_box.insert(END,link)


    def unshortenURL(self,url):
        proxy = urllib2.ProxyHandler()
        opener = urllib2.build_opener(proxy)
        response = opener.open("http://unshort.me/index.php?r=" + url)
        content = response.read()
        contentString = str(content)

        ad_focus = re.compile('\<title\>AdFoc\.us\<\/title\>')

        if ad_focus.match(contentString): ad_focus_unshorten(contentString)
        elif not ad_focus.match(contentString):
            pass

        rpd = re.compile('result\"\>\s\<a\shref\=\".+\>(.+)\<\/a\>\s', re.IGNORECASE)
        rpdFind = re.findall(rpd,contentString)
        rpdSorted=sorted(rpdFind)

        # print content3String

        m=''
        for m in rpdSorted:
            if url not in m:
                    #txt_box.insert(END,'[+] ' + url + ' redirects to: ' + m)
                    txt_box.insert(END, m)

            else:
                    txt_box.insert(END,'[-] URL Error!')


    def unshortened_clicked(self):
        url = txt_box.get()
        if url != '':
            txt_box.delete(0,END)
            self.unshortenURL(url)

        elif url == '':
            tkMessageBox.showerror('Error','You need to input shortened url in the text box above the button')
            Entry.focus_set(txt_box)

    def centerWindow(self):
        w = 250; h=170
        self.parent.maxsize(250,170)
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw-w)/2; y = (sh-h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))

    def initate_GUI(self):
        self.parent.title("URL Unshortener")
        self.centerWindow()
        self.display_label()
        self.display_textbox()
        self.display_buttons()

    def display_label(self):
        lbl_display = Label(self.parent,text="Url Unshortener\n \"http://unshort.me/\"",fg="green")
        lbl_display.pack()
        lbl_logo = Label(self.parent,text="Written by Zero",fg="red")#Anubis [MSF Moderator]"
        lbl_logo.place(x=25,y=140)

    def display_textbox(self):
        global txt_box
        txt_box = Entry(self.parent,width='30')
        txt_box.place(x=15,y=40)

    def display_buttons(self):
        btn_unshorten = Button(self.parent,text="Unshorten URL",command=self.unshortened_clicked,width='15',fg="Green",bg="Yellow")
        btn_unshorten.place(x=72,y=80)
        btn_quit = Button(self.parent,text="QUIT",command=exit,width="7",fg='white',bg='black')
        btn_quit.place(x=102,y=110)

    def show_menubar(self):
        menubar = Menu(self.parent)
        help_menu = Menu(menubar,tearoff=0)
        help_menu.add_command(label="About")#,command=about)
        menubar.add_cascade(label="Help",menu=help_menu)
        self.parent.config(menu=menubar)

def main():
    root = Tk()
    app = Unshortener(root)
    root.mainloop()

if __name__ == '__main__':
    main()

