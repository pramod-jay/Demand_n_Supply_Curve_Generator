import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline



root = tk.Tk()

root.title('ECONOCODE')

def btn_command():
    x = np.array([2,10,30,80])
    y = np.array([50,40,10,2])
   
    x_smooth=np.linspace(x.min(), x.max(), 300)
    spl=make_interp_spline(x, y, k=3)
    y_smooth=spl(x_smooth)

    fig = Figure(figsize=(4,4), dpi=90)
    plot1=fig.add_subplot(111)
    plot1.set_xlabel('Good 1')
    plot1.set_ylabel('Good 2')
    plot1.plot(x_smooth,y_smooth)

    canvas1 = FigureCanvasTkAgg(fig, master=frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=3, column=0, columnspan=2)
    toolbar=NavigationToolbar2Tk(canvas1, root)
    toolbar.update()
    canvas1.get_tk_widget().grid()

canva=tk.Canvas(root, height=700, width=800)
canva.pack()

frame=tk.Frame(root, bg="#1b181b")
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

lbl1 = tk.Label(frame, text="Enter Product 1:", bg="#1b181b", fg="Dark Orange", font=("Arial Nova", 15))
lbl1.grid(row=0, column=0)

entry1 = tk.Entry(frame, bg="#1b181b", fg="white", highlightthickness=2, highlightcolor="dark Orange", highlightbackground="Dark Orange", width=50, font=("Arial Nova", 10))
entry1.grid(row=0, column=1)

lbl2 = tk.Label(frame, text="Enter Product 2:", bg="#1b181b", fg="Dark Orange", font=("Arial Nova", 15))
lbl2.grid(row=1, column=0)

entry2 = tk.Entry(frame, bg="#1b181b", fg="white", highlightthickness=2, highlightcolor="dark Orange", highlightbackground="Dark Orange", width=50, font=("Arial Nova", 10))
entry2.grid(row=1, column=1) 

btn = tk.Button(frame, text="Calculate", bg="gray", fg="black", command=btn_command)
btn.grid(row=2, column=0, columnspan=2)



root.mainloop()




