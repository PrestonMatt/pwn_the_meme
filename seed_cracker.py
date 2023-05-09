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
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M-%S").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M-%S").date()
            unix_epoch = datetime.strptime("1970-01-01-00-00","%Y-%m-%d-%H-%M-%S").date()
            if end_date < start_date:
                messagebox.showerror("Error", "End date cannot be before start date.")
                
            elif(start_date < unix_epoch or end_date < unix_epoch):
                messagebox.showerror("Error", "Start or end date cannot be before system time of zero (unix epoch).")
            else:
                messagebox.showinfo("Date Range", "You entered the date range %s to %s." % (start_date,end_date) )
                password_guesser(start_date_str,end_date_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please enter dates in YYYY-MM-DD-HH-mm-SS format.")

def password_guesser(start_date_str,end_date_str):

    acceptable_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*\/?"

    guesses = []
    
    #translate the start date to unix time for the seed:
    start_date_ints = [int(s) for s in start_date_str.split("-")]
    start_date_time = datetime(year = start_date_ints[0],
    				month = start_date_ints[1],
    				day = start_date_ints[2],
    				hour = start_date_ints[3],
    				minute = start_date_ints[4],
    				second = start_date_ints[5])
    start_date_seed = time.mktime( start_date_time.timetule() )
    
    #translate the end date to unix time for the seed:
    end_date_ints = [int(e) for e in end_date_str.split("-")]
    end_date_time = datetime(year = end_date_ints[0],
    				month = end_date_ints[1],
    				day = end_date_ints[2],
    				hour = end_date_ints[3],
    				minute = end_date_ints[4],
    				second = end_date_ints[5])
    end_date_seed = time.mktime( end_date_time.timetule() )
    
    #start_date = datetime.strptime(start_date_str, "%Y-%m-%d-%H-%M-%S").time()
    #end_date = datetime.strptime(end_date_str, "%Y-%m-%d-%H-%M-%S").time()

    #TODO fix this so that it doesn't just see it as 00:00:00 - FIXED
    print("Starting date %s for starting seed: %d" % (start_date_time, start_date_seed))
    print("Ending date %s for ending seed: %d" % (end_date_time, end_date_seed))

    #TODO Fix this iteration loop to work with the date range - FIXED
    for rand_seed in range(start_date_seed,end_date_seed):
        print("Generating potential password for seed of date: %s" % system_times)
        password = "".join(random.sample(acceptable_characters,
                                         8).seed(a=rand_seed))
        guesses.append(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = DateRangeDialog(root)
    root.mainloop()
