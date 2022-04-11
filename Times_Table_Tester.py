#Write a times table tester with a GUI

from tkinter import *

def quit():
    main_window.destroy()

def details():
    global total_entries, name_count, details



#Create Column Headings
    name_count = 0 
    Label(main_window, font=("Helvetica 10 bold"), text="Check Answer").grid(column = 2, row = 10)
    Label(main_window, font=("Helvetica 10 bold"), text="Next").grid(column = 3, row = 10)

    while name_count < total_entries:
       Label(main_window, text=(details[name_count][0])).grid(column=1,row=name_count+11)
       Label(main_window, text=(details[name_count][1])).grid(column=2,row=name_count+11)
       main_window.geometry("")
       name_count +=1

       if len(re.findall(r'\w+', entry_name.get())) == 0:
        entry_name_blank.destroy()
        entry_name_first.destroy()
        entry_name_blank = Label(main_window,fg="red", text="Sorry - this can't be blank, please enter the customers Full Name")
        entry_name_blank.grid(row=4, column=2)



def main()
#Create GUI
main_window = Tk()
GUI()
PlaceHolder()

main_window.title("Times Table Tester")

main_window.mainloop()

main()


