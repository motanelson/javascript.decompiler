import tkinter as  tk





class myapps:
    def __init__(self,root:tk.Tk,titles:str,rcolor:bool,gcolor:bool,bcolor:bool,colorr:int,colorg:int,colorb:int,w:int,h:int):
        self.root=root
        self.root.title(titles)
        self.root.geometry(str(w)+"x"+str(h))
        self.root.configure(background="#888888")
        self.canvas=tk.Canvas(background="#888888",width=w,height=h)
        self.canvas.pack(padx=0,pady=0)
        ww:float=float(float(w)/float(255))
        a:float=0
        c:int=0
        #print (ww)
        ww = w / 255.0
        a = 0.0
        c = 0

        while c <= 255:
            rr = colorr
            gg = colorg
            bb = colorb

            if rcolor:
                rr = c
            if gcolor:
                gg = c
            if bcolor:
                bb = c
            ggg="00"+hex(gg).replace("0x","")
            bbb="00"+hex(bb).replace("0x","")
            rrr="00"+hex(rr).replace("0x","")
            cor="#"+bbb[-2:]+ggg[-2:]+rrr[-2:]
            #cor = f"#{rr:02X}{gg:02X}{bb:02X}"

            self.canvas.create_rectangle(
                int(a),
                0,
                int(a + ww + 1),
                h,
                fill=cor,
                outline=cor
            )

            a += ww
            c += 1









def starts(titles:str,rcolor:bool,gcolor:bool,bcolor:bool,colorr:int,colorg:int,colorb:int,w:int,h:int):
    root=tk.Tk()
    apps=myapps(root,titles,rcolor,gcolor,bcolor,colorr,colorg,colorb,w,h)
    root.mainloop()

starts("gradiente",True,True,True,0,0,0,640,480)