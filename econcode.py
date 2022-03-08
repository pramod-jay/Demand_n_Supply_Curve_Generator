import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


root = tk.Tk()

root.title('ECONOCODE')

def btn_command():
    x = [0,50,55]
    y = [0,50,55] 
   
    fig = Figure(figsize=(4,4), dpi=90)
    plot1=fig.add_subplot(111)
    plot1.set_xlabel('Good 1')
    plot1.set_ylabel('Good 2')
    plot1.plot(x,y)

    canvas1 = FigureCanvasTkAgg(fig, master=frame)
    canvas1.draw()
    canvas1.get_tk_widget().grid(row=5, column=0, columnspan=2)
    toolbar=NavigationToolbar2Tk(canvas1, root)
    toolbar.update()
    canvas1.get_tk_widget().grid()

canva=tk.Canvas(root, height=700, width=800)
canva.pack()

frame=tk.Frame(root, bg="#282a35")
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

lbl_title = tk.Label(frame, text="Enter Relevant Details to Calculate:", bg="#282a35", fg="white", font=("Calibri", 15))
lbl_title.grid(row=0, column=0, columnspan=2)

lbl_from = tk.Label(frame, text="Demand", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_from.grid(row=1, column=0)

lbl_to = tk.Label(frame, text="Price", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_to.grid(row=1, column=1)

demand_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12))
demand_from.grid(row=2, column=0, padx=10, pady=5)

price_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12))
price_from.grid(row=2, column=1, padx=10, pady=5)

demand_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12))
demand_to.grid(row=3, column=0, padx=10, pady=5)

price_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12))
price_to.grid(row=3, column=1, padx=10, pady=5)

btn_img=tk.PhotoImage(file='Images/btn.png')
button=tk.Button(frame, image=btn_img, command=btn_command, borderwidth=0)
button.grid(row=4, column=0, columnspan=2)

root.mainloop()



