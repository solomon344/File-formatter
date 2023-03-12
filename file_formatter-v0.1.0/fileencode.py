from tkinter import *
from tkinter.filedialog import askopenfilename
from base64 import b64encode,b64decode



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
        
        s = spil.replace(spil[-4:],"bin")
    else:
        s = spil.replace(spil[-3:],"bin")
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
    return rbfile.write(decode)
    
window = Tk()
window.title("file encode and decoder")


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
scrollbar.grid(row=2,column=1)

libox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=libox.yview)
p = ['jpg','jpeg','txt','png','mp4','mp3','txt','pdf','csv','json','xlsx','html','css','py','Js','exe','apk']

for i in p:
    libox.insert(0,i)
libox.grid(row=2,column=0)

window.mainloop()