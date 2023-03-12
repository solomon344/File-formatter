from tkinter import *
from tkinter.filedialog import askopenfilename
from base64 import b64encode,b64decode
import os
import string
with open("user_manual.txt","w") as my_file:
    r_file = my_file.write(""" Welcome to file formatter! 
     
        This is an easy to use application,I guessed you alrady knew.
        
        To use this application:
        
        1.Open the application as administrative.
        
        * To encode a file:
            
        1.Click on the open file button.
        
        2.Select any file format to be encodded,click open.
        
        3.Click on the encode button, and file formatter will do the magic.
        
        4.Just go to the directory where you opened the app, then you will see a .B64 file. Bravo! you encoded a file.
        
        * Time for decoding:
            
        1.Click open file and select a binary file or .B64/.BIN file to open.
        
        2.On the dashboard there is a list of file type extension in a tabular form, choose the one that best matches your binary file and click it, eg.  png .
        
        3.Select the one your binary file is.
        
        4.Click on the decode button and file formatter will do the trick.
        
        5.Also go to the same directory to see your file decoded.
        
        **If your file is not listed in the file extension list, type in the file extension in the entry field and click the 'Add ext' Button
        
        and the file extension will be added in the list. 
        
        *You can also delete unneccessary or accidental added extensions.
        
         ___________________GOOD LUCK!_____________________ 
        
        
        * 'Binary file'?.... It is the file format that a file has been encoded to, it has a '.B64/.BIN'  entension etc, but before decoding make sure you know the file type
        
        ***You can send queries on my facebook https://www.facebook.com/solomon.williams.9406417/
        
        or what'sApp 2207036433 if not work try adding the '+ sign 
        or email me at 'willamssolomon672@gmail.com'
        
        *AUTHOR: Solomon Williams
        
        *Author's Occupation: Informational Technology / IT / Programmer- Data Ananlyst and Sofware Algorithms builder.
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
    
    s = spil.replace(spil[spil.index(".") + 1:],"b64")
   
    new = open(s,"wb")
    l1.configure(text="successfuly encoded")
    return new.write(encode)
p = ['jpg','jpeg','txt','png','mp4','mp3','txt','pdf','csv','json','xlsx','html','css','py','Js']       

def decode():
    old = l1.cget("text")
    spil = old.split("/")[-1]
    
    s = spil.replace(spil[spil.index(".") + 1:],libox.get(libox.curselection()))
    
    print(s)
    
    file = open(l1.cget('text'),'rb')
    readed = file.read()
    decode = b64decode(readed)
    rbfile = open(s,'wb')
    l1.configure(text="successfuly decoded")
    return rbfile.write(decode)
    
def add_extension():
    ext = entry.get()
    
    if len(ext) > 5:
        pass
    elif len(ext) < 1:
        pass
    else:
        libox.configure(libox.insert(0,ext))
    
def remove():
    libox.delete(libox.curselection())
    

window = Tk()
window.title("File Formatter v0.1.1")


l1 = Label(window,text="Waiting for file",font = 15,bg = "blue",)
l1.place(relx=0.44,rely=0.05)
window.configure(bg="blue")

entry = Entry(window,width=17,bg="blue")
entry.place(relx=0.44,rely=0.25)

btn = Button(window,width=11,font=10,text= "Add Ext",bg="blue",command=add_extension)
btn.place(relx=0.1,rely=0.25)

btn0 = Button(window,width=11,font=10,text="Del Ext",bg="blue",command=remove)
btn0.place(relx=0.9,rely=0.25)

btn1 = Button(window,bg="blue", text = "Open File",command=opendiag,width=11,font=10)
btn1.place(relx=0.1,rely=0.05)

btn2 = Button(window,text="Encode",bg="blue",command=encode,width=11,font=10)
btn2.place(relx=0.9,rely=0.05)
btn3 = Button(window,text="Decode",bg="blue",command=decode,font=10,width=11)
btn3.place(relx=0.1,rely=0.75)
libox  = Listbox(window,bg="blue",selectmode=SINGLE)
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

l3 = Label(window,text="Please checkout the user manual before using!",bg="blue",font=17,)
l3.place(relx=0.64,rely=0.75)

btn4 = Button(window,bg="blue",text = "View manual",command=download,font=10)
btn4.place(relx=0.9, rely=0.75)

window.mainloop()
