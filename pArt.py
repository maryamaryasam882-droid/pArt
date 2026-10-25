from pydoc import cli
import tkinter as tk
from tkinter.colorchooser import *

root = tk.Tk()

root.title("pArt")
root.geometry("1200x1500")
root.configure(bg="pink")
label = tk.Label(root,bg="pink", text="welcome To pArt", font=("Press Start 2P", 20))
label.pack(pady=20,side="bottom")
p="""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"""
photo = tk.PhotoImage(data=p)
root.iconphoto(False, photo )
image_label = tk.Label(root, image=photo,bg="pink")
image_label.pack(pady=10)
cli="black"
def six():
  
    for widget in root.winfo_children():
        widget.destroy()
    def er():
        global cli
        cli="white"    
    def mycolor():
        global cli
        color=askcolor()[1]
        if color:
            cli=color
            
    bu=tk.Button(root,text="choose color",bg="#F9B4D9",command=mycolor)
    bu.place(relx=0.97, rely=1.0, anchor="se")
    be=tk.Button(root,text="erase",bg="#F9B4D9",command=er) 
    be.place(relx=1.0, rely=1.0, anchor="se")      
    back_button=tk.Button(root, text="←",command=clear)
    back_button.pack(anchor="nw")     
    can=tk.Canvas(root,width=320,height=320,bg="white")
    can.pack(expand=True)
    
    cell_size = 20
    for x in range(0,321,cell_size):
        can.create_line(x,0,x,320,fill="lightgray")
    for y in range(0,321,cell_size):
        
        can.create_line(0,y,320,y,fill="lightgray")    
    def draw(event):
        x=(event.x//cell_size)*cell_size
        y=(event.y//cell_size)*cell_size
        can.create_rectangle(x,y,x+cell_size,y+cell_size,fill=cli,outline="lightgray")
    can.bind("<B1-Motion>",draw)
    can.bind("<Button-1>",draw) 
    
def thirty():
    for widget in root.winfo_children():   
        widget.destroy()
    for widget in root.winfo_children():
            widget.destroy()
    def er():
        global cli
        cli="white"    
    def mycolor():
        global cli
        color=askcolor()[1]
        if color:
            cli=color    
    bu=tk.Button(root,text="choose color",bg="#F9B4D9",command=mycolor)
    bu.place(relx=0.97, rely=1.0, anchor="se")
    be=tk.Button(root,text="erase",bg="#F9B4D9",command=er) 
    be.place(relx=1.0, rely=1.0, anchor="se")         
    back_button=tk.Button(root, text="←",command=clear)
    back_button.pack(anchor="nw")  
    can=tk.Canvas(root,width=320,height=320,bg="white")
    can.pack(expand=True)  
    cell=10
    for x in range(0,321,cell):
        can.create_line(x,0,x,320,fill="lightgray")
    for y in range(0,321,cell):
        can.create_line(0,y,320,y,fill="lightgray")
    def draw(event):
            x=(event.x//cell)*cell
            y=(event.y//cell)*cell
            can.create_rectangle(x,y,x+cell,y+cell,fill=cli,outline="lightgray")
    can.bind("<B1-Motion>",draw)
    can.bind("<Button-1>",draw) 
            
        
def sixty():
    for widget in root.winfo_children():   
            widget.destroy()
    for widget in root.winfo_children():
                widget.destroy()
    def er():
            global cli
            cli="white"    
    def mycolor():
            global cli
            color=askcolor()[1]
            if color:
                cli=color    
    bu=tk.Button(root,text="choose color",bg="#F9B4D9",command=mycolor)
    bu.place(relx=0.97, rely=1.0, anchor="se")
    be=tk.Button(root,text="erase",bg="#F9B4D9",command=er) 
    be.place(relx=1.0, rely=1.0, anchor="se")         
    back_button=tk.Button(root, text="←",command=clear)
    back_button.pack(anchor="nw")  
    can=tk.Canvas(root,width=320,height=320,bg="white")
    can.pack(expand=True)  
    cell=5
    for x in range(0,321,cell):
            can.create_line(x,0,x,320,fill="lightgray")
    for y in range(0,321,cell):
            can.create_line(0,y,320,y,fill="lightgray")
    def draw(event):
                x=(event.x//cell)*cell
                y=(event.y//cell)*cell
                can.create_rectangle(x,y,x+cell,y+cell,fill=cli,outline="lightgray")
    can.bind("<B1-Motion>",draw)
    can.bind("<Button-1>",draw)
             
def cleara():
    for widget in root.winfo_children():
        widget.destroy()
    back_button=tk.Button(root, text="←",command=clearl)
    back_button.pack(anchor="w")      
    ##l1 = tk.Label(root, text="Now You Can Start ", font=("Press Start 2P", 20), bg="pink")
    ##l1.pack(pady=20, side="top")   
    ##b2=tk.Button(root,text="use blank canvas",command=clear,font=("Press Start 2P", 20),bg="pink",fg="black")
    ##b2.pack(pady=20,side="left")
def clear():
    for widget in root.winfo_children():
        widget.destroy()
    back_button=tk.Button(root, text="←",command=clearl)
    back_button.pack(anchor="w")    
    ll = tk.Label(root, text="Good luck >_< ", font=("Press Start 2P", 20), bg="pink")
    ll.pack(pady=20, side="top")   
    bb=tk.Button(root,text="16x16",command=six,font=("Press Start 2P", 20),bg="#F9B4D9",fg="black",height=4,width=10)
    bb.pack(pady=20,side="top",fill="x")
    bn=tk.Button(root,text="32x32",command=thirty,font=("Press Start 2P", 20),bg="#F9B4D9",fg="black",height=4,width=10)
    bn.pack(pady=20,side="top",fill="x")
    bm=tk.Button(root,text="64x64",command=sixty,font=("Press Start 2P", 20),bg="#F9B4D9",fg="black",height=4,width=10)
    bm.pack(pady=20,side="top",fill="x")
def clearl():
    for widget in root.winfo_children():
        widget.destroy()
    l1 = tk.Label(root, text="Now You Can Start ", font=("Press Start 2P", 40), bg="pink")
    l1.pack(pady=20, side="top")   
    b2=tk.Button(root,text="Use Blank Canvas",command=clear,font=("Press Start 2P", 20),bg="#F9B4D9",fg="black", width=15, height=3)
    b2.pack(pady=20,side="bottom",fill="x")
    ##b3=tk.Button(root,text="Use Image Canvas",command=cleara,font=("Press Start 2P", 20),bg="#F9B4D9",fg="black", width=15, height=3)
    ##b3.pack(pady=20,side="bottom",fill="x")
bs = tk.Button(root, text="Get Started ",command=clearl, font=("Press Start 2P", 20), bg="#F9B4D9", fg="black", width=15, height=3)
bs.pack(pady=20,side="bottom",fill="x")
root.mainloop()
