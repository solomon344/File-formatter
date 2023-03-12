from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from base64 import b64encode,b64decode
import os
import string
import time
with open("user_manual.txt","w") as my_file:
    r_file = my_file.write(""" Welcome to file formatter! 
     
        This is an easy to use application,I guessed you alrady knew.
        
        To use this application:
        
        1.Open the application as administrative.
        
        * To encode a file:
            
        1.Click on the open file button.
        
        2.Select any file format to be encodded,click open.
        
        3.Click on the encode button, 
        save the file to the location you want to decode it to and file formatter will do the magic.

        * Time for decoding:
            
        1.Click open file and select a binary file a .B64/.BIN file and open.
        
        2.On the dashboard there is a list of file type extensions in a tabular form, choose the one that best matches your binary file and click it, eg.  png .
        
        3.Select the one your binary file is eg. if your binary file was an image select png or jpg.
        
        4.Click on the decode button and save your decoded file to your desired destination.
                            
                        Yay!!! you can now use file formatter v-3.0
        
        **If your file type is not listed in the file extension list, type in the file extension in the entry field and click the 'Add ext' Button
        
        and the file extension will be added in the list. 
        
        *You can also delete unneccessary or accidental added extensions
        by selecting the file and click the 'Del Ext' button.
        
         ___________________GOOD LUCK!_____________________ 
        
        
        * 'Binary file'?.... It is the file format that a file has been encoded to, it has a '.B64/.BIN'  entension etc, but before decoding make sure you know the file type
        
        ***You can send queries on my facebook https://www.facebook.com/solomon.williams.9406417/
        
        or what'sApp 2207036433 if not work try adding the '+ sign 
        or email me at 'willamssolomon672@gmail.com'
        
        *AUTHOR: Solomon Williams
        
        *Author's Occupation: Informational Technology / IT - Programmer- Data Ananlyst and Sofware Algorithm builder.
        ___________________________________________________________
        ...........................................................""")
        
def opendiag():
    diag = askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.*"),("all files","*.*")))
    l1.configure(text=diag,fg='white')
            

def encode():
    try:
       file = open(l1.cget('text'),'rb')
    except FileNotFoundError:
        l1.configure(text='please select a valid file',fg='red')
    else:
        dir = askdirectory(initialdir='/',title='select dir',mustexist=True)
        reader = file.read()
        encoded = b64encode(reader)
        old_name = l1.cget('text')
        splitter = old_name.split('/')[-1]
        new_name = splitter.replace(splitter[splitter.index('.') + 1:],'b64')
        new_file = open(dir + "/" + new_name,'wb')
        l1.configure(text='successfully encoded')
        return new_file.write(encoded)
p = ['jpg','jpeg','txt','png','mp4','mp3','txt','pdf','csv','json','xlsx','html','css','py','js']       

def decode():
    try:
        file = open(l1.cget('text'),'rb')
    except FileNotFoundError:
        l1.configure(text='please select a valid file',fg="red")
    else:
        reader = file.read()
        decoded = b64decode(reader)
        old_name = l1.cget('text')
        splitter = old_name.split('/')[-1]
        try:
            new_name = splitter.replace(splitter[splitter.index('.') + 1:],libox.get(libox.curselection()))
        except TclError:
            l1.configure(text='perhaps you forgot to select a file extension',fg='orange')
        else:
            dir = askdirectory(initialdir='/',title='select dir',mustexist=True)
            new_file = open(dir + "/" + new_name,'wb')
            l1.configure(text='successfully decoded',fg='white')
            return new_file.write(decoded)
    
def add_extension():
    ext = entry.get()
    
    if len(ext) > 5:
        l1.configure(text='lenth of extension exceeds than expected',fg='red')
    elif len(ext) < 1:
        l1.configure(text='lenth of extension is breifer than expected',fg='red')
    elif " " in ext:
        l1.configure(text='Invalid extension type \" \" ',fg='red')
    elif ext.lower() in p:
        l1.configure(text='extension already existed',fg='red')     
    else: 
        p.append(ext.lower())
        libox.configure(libox.insert(0,ext.lower()))  
        print('seccess')
        l1.configure(text='Wating for file',fg='white')
    
    
def remove():
    try:
        ext = libox.get(libox.curselection())
        libox.delete(libox.curselection())
    except TclError:
        l1.configure(text='no extension selected',fg='red')
    else:
        p.remove(ext)
        l1.configure(text='Waiting for file',fg='white')
    

window = Tk()
window.title("File Formatter v0.1.1")


l1 = Label(window,text="Waiting for file",font = 15,bg = "blue",fg='white')
l1.place(relx=0.44,rely=0.05)
window.configure(bg="blue")

entry = Entry(window,width=17,bg="blue",fg='white')
entry.place(relx=0.44,rely=0.25)

btn = Button(window,width=11,font=10,text= "Add Ext",bg="blue",command=add_extension,fg='white')
btn.place(relx=0.1,rely=0.25)

btn0 = Button(window,width=11,font=10,text="Del Ext",bg="blue",command=remove,fg='white')
btn0.place(relx=0.9,rely=0.25)

btn1 = Button(window,bg="blue", text = "Open File",command=opendiag,width=11,font=10,fg='white')
btn1.place(relx=0.1,rely=0.05)

btn2 = Button(window,text="Encode",bg="blue",command=encode,width=11,font=10,fg='white')
btn2.place(relx=0.9,rely=0.05)
btn3 = Button(window,text="Decode",bg="blue",command=decode,font=10,width=11,fg='white')
btn3.place(relx=0.1,rely=0.75)
libox  = Listbox(window,bg="blue",selectmode=SINGLE,fg='white')
scrollbar = Scrollbar(window)
scrollbar.place(relx=0.877,rely=0.478)

libox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=libox.yview)


for i in p:
    libox.insert(0,i)
libox.place(relx=0.8,rely=0.4)

def download():
     return os.system(r"user_manual.txt")

    
    
    
window.geometry("1000x600")

l3 = Label(window,text="Please checkout the user manual before using!",bg="blue",font=17,fg='white')
l3.place(relx=0.64,rely=0.75)

btn4 = Button(window,bg="blue",text = "View manual",command=download,font=10,fg='white')
btn4.place(relx=0.9, rely=0.75)

window.mainloop()
