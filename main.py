from tkinter import *

def calculate_bmi():
    try:
        height = float(entry1.get()) / 100  # Convert height from cm to meters
        weight = float(entry2.get())

        if weight <= 0 or height <= 0:
            result_label.config(text="Geçersiz giriş. Lütfen pozitif değerler girin.")
            return

        bmi = weight / (height * height)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Geçersiz giriş. Lütfen sayısal değerler girin.")

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200, height=150)

my_label = Label(text="Boyunuzu giriniz(cm): ")
my_label.pack()

entry1 = Entry(width=20)
entry1.pack()

my_label_2 = Label(text="Kilonuzu giriniz(kg): ")
my_label_2.pack()

entry2 = Entry(width=20)
entry2.pack()

my_button = Button(text="Hesapla", command=calculate_bmi)
my_button.pack()

result_label = Label(text="")
result_label.pack()

window.mainloop()