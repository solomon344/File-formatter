from tkinter import *
from tkinter.filedialog import askopenfilename
from base64 import b64encode,b64decode
import os

with open("user_manual.txt","w") as my_file:
    r_file = my_file.write(""" Welcome to file formatter! 
     
        This is an easy to use application,I guessed you alrady knew.
        
        To use this application:
        
        1.Open the application as an administrative.
        
        *If you wanted to encode a file:
        1.click on the open file button.
        2.select any file format to be encodded,click open.
        
        3.click on the encode button, and file formatter will do the magic.
        
        4.just go to the directory where you opened the app or selected the file, then you will see a .bin file. Bravo! you encoded a file.
        
        *Time for decoding:
        1.click open file and select a binary file or .bin file to open.
        
        2.On the dashboard there is a list of file types, choose the one you want to decode your file to.
        
        3.Select the one your file was encoded with.
        
        4.Click on the decode button and file formatter will do the trick.
        
        5.Also go to the directory to see your file decoded
        
         ___________________GOOD LUCK!_____________________ 
        
        
        * 'Binary file'?.... Is the file that has been encoded to, it has a '.B64/.BIN' entension, but before decoding make sure you know the file type
        
        ***If your file is not listed in the list send a query on my facebook https://www.facebook.com/solomon.williams.9406417/
        
        or what'sApp 2207036433 if not work try adding the '+ sign 
        or email me at 'willamssolomon672@gmail.com'
        
        *AUTHOR: Solomon Williams
        
        *Author's occupation: Informational Technology/IT Programmer- Data Ananlyst and sofware Algorithms builder.
        ___________________________________________________________
        ...........................................................""")
def opendiag():
    diag = askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.*"),("all files","*.*")))
    l1.configure(text=diag  )
            
def encode():
    
    #path = os.path.abspath(self.diag.n)
    old = l1.cget("text")
    flname = open(l1.cget("text"),"rb")
    rb = flname.read()
    encode = b64encode(rb)
    spil = old.split("/")[-1]
    print(spil[-4:])
    if spil[-4] != ".":
        
        s = spil.replace(spil[-4:],"b64")
    else:
        s = spil.replace(spil[-3:],"b64")
    new = open(s,"wb")
    l1.configure(text="successfuly encoded")
    return new.write(encode)
        
def decode():
    old = l1.cget("text")
    spil = old.split("/")[-1]
    if spil[-4] != ".":
        s = spil.replace(spil[-4:],libox.get(libox.curselection()))
    else:
        s = spil.replace(spil[-3:],libox.get(libox.curselection()))
    print(s)
    file = open(l1.cget('text'),'rb')
    readed = file.read()
    decode = b64decode(readed)
    rbfile = open(s,'wb')
    l1.configure(text="successfuly decoded")
    return rbfile.write(decode)
    
window = Tk()
window.title("File Formatter v0.1")


l1 = Label(window,text="waiting for file",font = 12,bg = "lightblue",fg="blue")
l1.grid(row=0,column=0)
window.configure(bg="lightblue")
btn1 = Button(window,bg="blue", text = "open file",command=opendiag)
btn1.grid(row=1,column=0)

btn2 = Button(window,text="encode",bg="blue",command=encode)
btn2.grid(row=0,column=1)
btn3 = Button(window,text="decode",bg="blue",command=decode)
btn3.grid(row=1,column=1)
libox  = Listbox(window,bg="lightblue",selectmode=SINGLE)
scrollbar = Scrollbar(window)
scrollbar.grid(row=2,column=0)

libox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=libox.yview)
p = ['jpg','jpeg','txt','png','mp4','mp3','txt','pdf','csv','json','xlsx','html','css','py','Js']

for i in p:
    libox.insert(0,i)
libox.grid(row=2,column=0)

def download():
   
     return os.system(r"user_manual.txt")

    
    
    
window.geometry("500x300")

l3 = Label(window,text="Please checkout the user manual before using!",bg="lightblue")
l3.grid(row = 3,column=0)

btn4 = Button(window,bg="blue",text = "View manual",command=download)
btn4.grid(row=3,column=1)


window.mainloop()
