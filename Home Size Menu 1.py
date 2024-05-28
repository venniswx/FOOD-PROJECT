import tkinter as tk

root= tk.Tk()
root.title("The WOK- Home Page")
root.geometry('1280x720')

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text=' ≡ ')
        toggle_btn.config(command=toggle_menu)


    toggle_menu_fm= tk.Frame(root,bg='brown')

    home_btn= tk.Button(toggle_menu_fm,text='Home',font=('times new roman',20),bd=0,fg='white',bg='brown')
    home_btn.place(x=20,y=0)

    profile_btn= tk.Button(toggle_menu_fm,text='Profile',font=('times new roman',20),bd=0,fg='white',bg='brown')
    profile_btn.place(x=20,y=50)

    menu_btn = tk.Button(toggle_menu_fm, text='Menu', font=('times new roman', 20), bd=0, fg='white', bg='brown')
    menu_btn.place(x=20, y=100)

    reservation_btn = tk.Button(toggle_menu_fm, text='Reservation', font=('times new roman', 20), bd=0, fg='white', bg='brown')
    reservation_btn.place(x=20, y=150)

    location_btn = tk.Button(toggle_menu_fm, text='Location', font=('times new roman', 20), bd=0, fg='white', bg='brown')
    location_btn.place(x=20, y=200)

    feedback_btn = tk.Button(toggle_menu_fm, text='Feedback', font=('times new roman', 20), bd=0, fg='white',bg='brown')
    feedback_btn.place(x=20, y=250)

    chatAssist_btn = tk.Button(toggle_menu_fm, text='Chat Assistant', font=('times new roman', 20), bd=0, fg='white', bg='brown')
    chatAssist_btn.place(x=20, y=300)

    window_height=1080 #root.winfo_height()
    toggle_menu_fm.place(x=0,y=50, height=window_height, width=300)

    toggle_btn.config(text=' X ')
    toggle_btn.config(command=collapse_toggle_menu)


head_frame= tk.Frame(root, bg='brown')
                     #,highlightbackground='white',highlightthickness=1)

toggle_btn= tk.Button(head_frame,text=' ≡ ',bg='brown',fg='white',font=('Bold',20),bd=0,activebackground='black',activeforeground='yellow',command=toggle_menu)
toggle_btn.pack(side=tk.LEFT)

title_lb= tk.Label(head_frame,text='The WOK- Chinese Restaurant',fg='white',bg='brown',font=('Impact',20))
title_lb.pack(side=tk.LEFT)


head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


root.mainloop()
