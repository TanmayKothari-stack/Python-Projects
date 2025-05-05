from tkinter import *
def scroll_window(window,width,height,bg,orient,mousescrolling):
        if orient == str("y") or orient == str("Y"):
                canvas = Canvas(window,bg=bg,width=width-20,height=height,highlightthickness=0)
                canvas.pack(side=LEFT,fill=BOTH,expand=True)
                scrollbar = Scrollbar(window,orient=VERTICAL,command=canvas.yview)
                scrollbar.pack(side=RIGHT,fill=BOTH)
                canvas.configure(yscrollcommand=scrollbar.set)
                def on_scroll(*args):
                        canvas.configure(scrollregion=canvas.bbox("all"))
                frame = Frame(canvas,bg=bg)
                canvas.create_window((0,0),window=frame,anchor='nw')
                frame.bind("<Configure>",on_scroll)
                if mousescrolling == True:
                        window.bind_all("<MouseWheel>",lambda event: canvas.yview_scroll(-1 * (event.delta // 120),"units"))
                return frame
        
        elif orient == str("x") or orient == str("X"):
                canvas = Canvas(window,bg=bg,width=width-20,height=height,highlightthickness=0)
                canvas.pack(side=TOP,fill=BOTH,expand=True)
                scrollbar = Scrollbar(window,orient=HORIZONTAL,command=canvas.xview)
                scrollbar.pack(side=BOTTOM,fill=BOTH)
                canvas.configure(xscrollcommand=scrollbar.set)
                def on_scroll(*args):
                        canvas.configure(scrollregion=canvas.bbox("all"))
                frame = Frame(canvas,bg=bg)
                canvas.create_window((0,0),window=frame,anchor='nw')
                frame.bind("<Configure>",on_scroll)
                if mousescrolling == True:
                        window.bind_all("<MouseWheel>",lambda event: canvas.xview_scroll(-1 * (event.delta // 120),"units"))     
                return frame
        
                
        if orient == str("both") or orient == str("Both") or orient == str("BOTH") or orient == str("xy") or orient == str("XY"):
                canvas = Canvas(window,bg=bg,width=width-20,height=height,highlightthickness=0)
                canvas.grid(row=0,column=0,sticky="nsew")
                scrollbarY = Scrollbar(window,orient=VERTICAL,command=canvas.yview)
                scrollbarY.grid(row=0,column=1,sticky="ns")
                
                scrollbarX = Scrollbar(window,orient=HORIZONTAL,command=canvas.xview)
                scrollbarX.grid(row=1,column=0,sticky="ew")
                
                canvas.configure(xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
                def on_scroll(*args):
                        canvas.configure(scrollregion=canvas.bbox("all"))
                frame = Frame(canvas,bg=bg)
                canvas.create_window((0,0),window=frame,anchor='nw')
                frame.bind("<Configure>",on_scroll)
                if mousescrolling == True:
                        window.bind_all("<MouseWheel>",lambda event: canvas.yview_scroll(-1 * (event.delta // 120),"units"))
                return frame
