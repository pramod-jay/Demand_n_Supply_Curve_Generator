import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image

#tkinter library for create Graphical User Interface
#matplotlib library for grnerate graph
#PIL library for import images(Logos) and customize them 

root = tk.Tk()

root.title('Econocode')
root.configure(background='#373A49')
root.geometry('480x750')
root.resizable(width='False', height='False')
root.iconbitmap("Images\icon.ico")

def about():
    top = tk.Toplevel()
    top.geometry('480x200')
    top.title('About')
    top.configure(background='#373A49')
    top.iconbitmap("Images\icon.ico")
    top.resizable(width='False', height='False')

    global img
    img_logo1=tk.Label(top,image=img,borderwidth=0, background='#373A49')
    img_logo1.place(relx=0.1, rely=0.1, relheight=0.3, relwidth=0.8)

    lbl_module = tk.Label(top, text="Principal of Economics\tIS1020", bg="#373A49", fg="white", font=("Times New Roman", 15))
    lbl_module.place(relx=0.05, rely=0.4, relheight=0.07, relwidth=0.9)

    lbl_assignment = tk.Label(top, text="Assignment 02 (Individual)", bg="#373A49", fg="white", font=("Times New Roman", 15))
    lbl_assignment.place(relx=0.05, rely=0.55, relheight=0.07, relwidth=0.9)
    
    lbl_name = tk.Label(top, text="205045J\tJayathilaka DDPD", bg="#373A49", fg="white", font=("Times New Roman", 13))
    lbl_name.place(relx=0.05, rely=0.7, relheight=0.07, relwidth=0.9)

def btn_command():
    try:
        x=[]
        y=[]
        x.append(int(demand_from.get()))
        x.append(int(demand_to.get()))
        y.append(int(price_from.get()))
        y.append(int(price_to.get()))

        delQD=x[1]-x[0]
        delP=y[1]-y[0]
        if(delP==0):
            if(delQD>0):
                lbl_answer.config(text='inf', fg='white')
                lbl_class.config(text="Perfectly Elastic Demand")
            else:
                lbl_answer.config(text='-inf', fg='white')
                lbl_class.config(text="Perfectly Elastic Demand")
        else:
            PED=(delQD/delP)*(y[0]/x[0])
            PED=round(PED,2)
            if((PED>-1) and (PED<1) and (PED!=0)):
                    lbl_answer.config(text=PED, fg='white')
                    lbl_class.config(text="Inelastic Demand")
            elif((PED<-1) or (PED>1)):
                    lbl_answer.config(text=PED, fg='white')
                    lbl_class.config(text="Elastic Demand")
            elif(PED==0.0):
                    lbl_answer.config(text=PED, fg='white')
                    lbl_class.config(text="Perfectly Inelastic Demand")
            elif((PED==1) or (PED==-1)):
                    lbl_answer.config(text=PED, fg='white')
                    lbl_class.config(text="Unitary Elastic Demand")
      
        fig = Figure(figsize=(4,4), dpi=80, facecolor='#282a35')
        plot1=fig.add_subplot(111)
        plot1.set_xlabel('Quantity of Demand')
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
        canvas1.get_tk_widget().grid(row=8, column=0, columnspan=2)
      
    except ValueError:
        lbl_answer.config(text="Please Enter Valid Data!!!", fg='red')


menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

about_menu=tk.Menu(menu_bar)
menu_bar.add_cascade(label="About", command=about)

global img
img=Image.open('Images/logo.png')
img=img.resize((130,50))
img=ImageTk.PhotoImage(img)
img_logo=tk.Label(root,image=img,borderwidth=0, background='#373A49')
img_logo.place(relx=0.1, rely=0, relheight=0.06, relwidth=0.8)

lbl_title = tk.Label(root, text="This application is designed to find the price-demand\nelasticity of a product and to classify\ndemand according to the extent of that elasticity.", bg="#373A49", fg="white", font=("Calibri", 11))
lbl_title.place(relx=0.05, rely=0.065, relheight=0.07, relwidth=0.9)

frame=tk.Frame(root, bg='#282a35', highlightbackground="white", highlightcolor="white", highlightthickness=3)
frame.place(relx=0.05, rely=0.15, relheight=0.8, relwidth=0.9)

lbl_title = tk.Label(frame, text="Enter Relevant Details to Calculate", bg="#282a35", fg="white", font=("Calibri", 15),padx=60)
lbl_title.grid(row=0, column=0, columnspan=2)

lbl_price = tk.Label(frame, text="Price", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_price.grid(row=1, column=0)

lbl_demand = tk.Label(frame, text="Demand (Q)", bg="#282a35", fg="white", font=("Calibri", 12))
lbl_demand.grid(row=1, column=1)

price_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
price_from.grid(row=2, column=0, padx=10, pady=5)

demand_from = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
demand_from.grid(row=2, column=1, padx=10, pady=5)

lbl_to1 = tk.Label(frame, text="To", bg="#282a35", fg="white", font=("Calibri", 8))
lbl_to1.grid(row=3, column=0)

lbl_to2 = tk.Label(frame, text="To", bg="#282a35", fg="white", font=("Calibri", 8))
lbl_to2.grid(row=3, column=1)

price_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
price_to.grid(row=4, column=0, padx=10, pady=5)

demand_to = tk.Entry(frame, bg="#282a35", fg="white", highlightthickness=2, highlightcolor="white", highlightbackground="white", width=10, font=("Calibri", 12), justify="center", insertbackground="white")
demand_to.grid(row=4, column=1, padx=10, pady=5)

btn_img=tk.PhotoImage(file='Images/btn.png')
button=tk.Button(frame, image=btn_img, command=btn_command, borderwidth=0)
button.grid(row=5, column=0, columnspan=2)

lbl_answer = tk.Label(frame, text='', bg="#282a35", fg="white", font=("Calibri", 15))
lbl_answer.grid(row=6, column=0, columnspan=2)

lbl_class = tk.Label(frame, text='', bg="#282a35", fg="white", font=("Calibri", 15))
lbl_class.grid(row=7, column=0, columnspan=2)

root.mainloop()