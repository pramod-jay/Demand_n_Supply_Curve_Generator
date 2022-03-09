from cProfile import label
import tkinter as tk
from turtle import bgcolor, color, width
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import ImageTk, Image


root = tk.Tk()

root.title('ECONOCODE')
root.configure(background='#373A49')
root.geometry('480x750')
root.resizable(width='False', height='False')

def btn_command():
    x = [0,50,55]
    y = [0,50,55] 
   
    fig = Figure(figsize=(4,4), dpi=85, facecolor='#282a35')
    plot1=fig.add_subplot(111)
    plot1.set_xlabel('Demand')
    plot1.set_ylabel('Price')
    plot1.set_facecolor("#282a35")
    plot1.xaxis.label.set_color('white')     
    plot1.yaxis.label.set_color('white')
    plot1.tick_params(axis='x', colors='white')  
    plot1.tick_params(axis='y', colors='white')
    plot1.spines['left'].set_color('white')       
    plot1.spines['right'].set_color('white')
    plot1.spines['top'].set_color('white')
    plot1.spines['bottom'].set_color('white')
    plot1.grid(color = 'white', linestyle = '--', linewidth = 0.5)
    plot1.plot(x,y, color='#00ff00')

    canvas1 = FigureCanvasTkAgg(fig, master=frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10)
    toolbar=NavigationToolbar2Tk(canvas1, root)
    toolbar.update()
    canvas1.get_tk_widget().grid()


img=Image.open('Images/logo.png')
img=img.resize((130,50))
img=ImageTk.PhotoImage(img)
tk.Label(root,image=img,borderwidth=0,pady=0.10).pack()

frame=tk.Frame(root, bg="#282a35", highlightbackground="white", highlightcolor="white", highlightthickness=3)
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

lbl_title = tk.Label(frame, text="Enter Relevant Details to Calculate", bg="#282a35", fg="white", font=("Calibri", 15),padx=41)
lbl_title.grid(row=0, column=0, columnspan=2)

lbl_demand = tk.Label(frame, text="Demand", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_demand.grid(row=1, column=0)

lbl_price = tk.Label(frame, text="Price", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_price.grid(row=1, column=1)


demand_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
demand_from.grid(row=2, column=0, padx=10, pady=5)

price_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
price_from.grid(row=2, column=1, padx=10, pady=5)

lbl_to1 = tk.Label(frame, text="To", bg="#282a35", fg="white", font=("Calibri", 8))
lbl_to1.grid(row=3, column=0)

lbl_to2 = tk.Label(frame, text="To", bg="#282a35", fg="white", font=("Calibri", 8))
lbl_to2.grid(row=3, column=1)

demand_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
demand_to.grid(row=4, column=0, padx=10, pady=5)

price_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
price_to.grid(row=4, column=1, padx=10, pady=5)

btn_img=tk.PhotoImage(file='Images/btn.png')
button=tk.Button(frame, image=btn_img, command=btn_command, borderwidth=0)
button.grid(row=5, column=0, columnspan=2)

root.mainloop()