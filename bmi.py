from tkinter import *
window=Tk()

# add widgets here

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_BMI():
    Weight = int(weight.get())
    Height = int(height.get())/100

    bmi = Weight/(Height * Height)
    bmi = round(bmi, 1)

    name = username.get()

    result_label.destroy()

    message = ''
    if bmi < 18.5:
        message='You are underweight'
    elif bmi > 18.5 and bmi <= 24.9:
        message='Your weight is in normal range'
    elif bmi > 25 and bmi <= 29.9:
        message='You are overweight'
    elif bmi > 30:
        message='You are obese'
    else:
        message='Something went wrong...'

    output_message=Label(result_frame,text=name+", your BMI is "+str(bmi)+" and "+ message, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20, y=40)
    output_message.pack()

app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label=Label(window, text="Your Height(in cm)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
height_label.place(x=20, y=140)

height=Entry(window, text="", bd=2, width=22)
height.place(x=150, y=142)

weight_label=Label(window, text="Your Weight(in kg)", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
weight_label.place(x=20, y=190)

weight=Entry(window, text="", bd=2, width=22)
weight.place(x=150, y=192)

calculate_button = Button(window, text="CALCULATE", fg="black", bg="cyan", bd=5, command=calculate_BMI)
calculate_button.place(x=20, y=240)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()