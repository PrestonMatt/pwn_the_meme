import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from random import sample
import time

class DateRangeDialog:
    def __init__(self, parent):
        """
            Initiate the GUI interface for to take the range of dates as inputs.
        """

        #Create the initial window:
        self.parent = parent
        self.parent.title("Date Range")
        self.parent.geometry("300x150")
        self.parent.resizable(False, False)

        #instruction label
        self.instr_label = ttk.Label(
            parent,
            text="Please enter a date as YYYY-MM-DD-HH-mm format.",
            foreground = "white",
            background = "black")
        self.instr_label.pack()

        #First label
        self.start_label = ttk.Label(
            parent,
            text="Start Date:",
            foreground = "blue",
            background = "light grey")
        self.start_label.pack()

        #First button - input date 1
        self.start_date = ttk.Entry(parent)
        self.start_date.pack()

        #Second label
        self.end_label = ttk.Label(
            parent,
            text="End Date:",
            foreground = "blue",
            background = "light grey")
        self.end_label.pack()

        #Second button - input date 2
        self.end_date = ttk.Entry(parent)
        self.end_date.pack()

        #Third button, to submit the dates
        self.submit_button = ttk.Button(
            parent,
            text="Submit",
            command=self.submit)
        self.submit_button.pack()

    def submit(self):
        """
            Method that impliments the functionality of the submit button.
            Also checks if the date inputs are valid dates using the datetime module.
        """        
        start_date_str = self.start_date.get()
        end_date_str = self.end_date.get()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M").date()
            unix_epoch = datetime.strptime("1970-01-01-00-00","%Y-%m-%d-%H-%M").date()
            if end_date < start_date:
                messagebox.showerror("Error", "End date cannot be before start date.")
                
            elif(start_date < unix_epoch or end_date < unix_epoch):
                messagebox.showerror("Error", "Start or end date cannot be before system time of zero (unix epoch).")
            else:
                messagebox.showinfo("Date Range", "You entered the date range %s to %s." % (start_date,end_date) )
                password_guesser(start_date_str,end_date_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter dates in YYYY-MM-DD-HH-MM format.")

def password_guesser(start_date_str,end_date_str):

    acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*\/?"

    guesses = []
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M").time()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M").time()

    #TODO fix this so that it doesn't just see it as 00:00:00
    print("Starting seed: %s" % start_date)
    print("Ending seed: %s" % end_date)

    #TODO Fix this iteration loop to work with the date range
    for system_times in range(start_date,end_date):
        print("Generating potential password for seed of date: %s" % system_times)
        password = "".join(random.sample(acceptable_characters,
                                         8).seed(a=system_times))
        guesses.append(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = DateRangeDialog(root)
    root.mainloop()
