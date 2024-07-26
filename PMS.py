# Parking Management System
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# In-memory storage for car accounts and parking status
car_accounts = {}
parking_slots = {}


# GUI setup
root = tk.Tk()
root.title("Parking Management System")
root.geometry("500x500")  # Set the window size to 400x400 pixels
root.config(bg="white")  # Set the background color to white


# Add heading
heading_label = tk.Label(root, text="Parking Management System", font=("Arial", 16, "bold"), bg="white", fg="black")
heading_label.pack(pady=20)


def add_car():
    car_number = car_number_entry.get()
    owner_name = owner_name_entry.get()
    if car_number and owner_name:
        if car_number not in car_accounts:
            car_accounts[car_number] = owner_name
            messagebox.showinfo("Success", "Car added successfully!")
        else:
            messagebox.showerror("Error", "Car already exists!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")


def delete_car():
    car_number = car_number_entry.get()
    if car_number:
        if car_number in car_accounts:
            del car_accounts[car_number]
            parking_slots.pop(car_number, None)  # Remove from parking if present
            messagebox.showinfo("Success", "Car deleted successfully!")
        else:
            messagebox.showerror("Error", "Car does not exist!")
    else:
        messagebox.showerror("Error", "Please provide the car number")


def enter_parking():
    car_number = car_number_entry.get()
    if car_number:
        if car_number in car_accounts:
            if car_number not in parking_slots:
                parking_slots[car_number] = datetime.now()
                messagebox.showinfo("Success", "Car entered parking successfully!")
            else:
                messagebox.showerror("Error", "Car is already parked!")
        else:
            messagebox.showerror("Error", "Car does not exist!")
    else:
        messagebox.showerror("Error", "Please provide the car number")


def exit_parking():
    car_number = car_number_entry.get()
    if car_number:
        if car_number in parking_slots:
            entry_time = parking_slots.pop(car_number)
            exit_time = datetime.now()
            duration = exit_time - entry_time
            messagebox.showinfo("Success", f"Car exited parking successfully!\nDuration: {duration}")
        else:
            messagebox.showerror("Error", "Car is not parked!")
    else:
        messagebox.showerror("Error", "Please provide the car number")


# GUI components
car_number_label = tk.Label(root, text="Car Number", bg="white", fg="black", font="bold_font")
car_number_label.pack(pady=10)
car_number_entry = tk.Entry(root)
car_number_entry.pack(pady=10)


owner_name_label = tk.Label(root, text="Owner Name", bg="white", fg="black", font=("bold_font"))
owner_name_label.pack(pady=10)
owner_name_entry = tk.Entry(root)
owner_name_entry.pack(pady=10)


add_car_button = tk.Button(root, text="Add Car", command=add_car, bg="green", fg="white", border="6", height="1",width="12")
add_car_button.pack(pady=10)


delete_car_button = tk.Button(root, text="Delete Car", command=delete_car, bg="red", fg="white", border="6", height="1",width="12")
delete_car_button.pack(pady=10)


enter_parking_button = tk.Button(root, text="Enter Parking", command=enter_parking, bg="blue", fg="white", border="6", height="1",width="12")
enter_parking_button.pack(pady=10)


exit_parking_button = tk.Button(root, text="Exit Parking", command=exit_parking, bg="gray", fg="white", border="6", height="1",width="12")
exit_parking_button.pack(pady=10)


# Start the GUI event loop
root.mainloop()


car_accounts()
