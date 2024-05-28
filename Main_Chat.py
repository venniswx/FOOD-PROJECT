from tkinter import *
import tkinter as tk
from tkinter import messagebox
from Chat_Assistant import *

root= tk.Tk()
root.title("The WOK- Home Page")
root.geometry('1920x1080')
root.attributes("-fullscreen",True)

def home_page():
    home_frame = tk.Frame(main_frame)
    home_frame.place(relwidth=1, relheight=1)
    mainlb = tk.Label(home_frame, text='Home Page\n\nPage:1', font=('Bold', 30))
    mainlb.place(x=100,y=50)

def profile_page():
    profile_frame= tk.Frame(main_frame)
    profilelb =tk.Label(profile_frame,text='My Profile\n\nPage:2',font=('Bold',30))
    profilelb.place(x=100,y=50)
    profile_frame.place(relwidth=1, relheight=1)

def menu_page():
    menu_frame= tk.Frame(main_frame)
    menulb =tk.Label(menu_frame,text='Food & Drinks\n\nMenu',font=('Bold',30))
    menulb.place(x=100,y=50)
    menu_frame.place(relwidth=1, relheight=1)

def reservation_page():
    reservation_frame= tk.Frame(main_frame)
    reservationlb =tk.Label(reservation_frame,text='Reservation\n\nPage:4',font=('Bold',30))
    reservationlb.place(x=100,y=50)
    reservation_frame.place(relwidth=1, relheight=1)

def location_page():
    location_frame = tk.Frame(main_frame)
    locationlb = tk.Label(location_frame, text='Location\n\nPage:5', font=('Bold', 30))
    locationlb.place(x=100,y=50)
    location_frame.place(relwidth=1, relheight=1)

def feedback_page():
    feedback_frame = tk.Frame(main_frame)
    feedbacklb = tk.Label(feedback_frame, text='Leave your feedback.\n\nWe appreciate it.', font=('Bold', 30))
    feedbacklb.place(x=100,y=50)
    feedback_frame.place(relwidth=1, relheight=1)

def chatAssist_page():
    chatAssist_frame = tk.Frame(main_frame)
    chatAssist_frame.place(relwidth=1, relheight=1)  # Make sure the frame takes the full space or a sufficient space
    chatAssistlb = tk.Label(chatAssist_frame, text="Hi", font=('Bold', 30))
    chatAssistlb.place(x=100, y=50)

def Exit_page():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()

def hide_indicators():
    global home_indicate, profile_indicate, menu_indicate, reservation_indicate, location_indicate, feedback_indicate, chatAssist_indicate, Exit_indicate
    home_indicate.config(bg='brown')
    profile_indicate.config(bg='brown')
    menu_indicate.config(bg='brown')
    reservation_indicate.config(bg='brown')
    location_indicate.config(bg='brown')
    feedback_indicate.config(bg='brown')
    chatAssist_indicate.config(bg='brown')
    Exit_indicate.config(bg='brown')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(lb,page):
    hide_indicators()
    lb.config(bg='white')
    delete_pages()
    page()
def toggle_menu():
    global home_indicate, profile_indicate, menu_indicate, reservation_indicate, location_indicate, feedback_indicate, chatAssist_indicate, Exit_indicate

    def collapse_toggle_menu():
        global home_indicate, profile_indicate, menu_indicate, reservation_indicate, location_indicate, feedback_indicate, chatAssist_indicate, Exit_indicate
        toggle_menu_fm.destroy()
        toggle_btn.config(text=' ≡ ')
        toggle_btn.config(command=toggle_menu)


    toggle_menu_fm= tk.Frame(root,bg='brown')

    home_btn= tk.Button(toggle_menu_fm,text='Home',font=('times new roman',20),bd=0,fg='white',bg='brown',activebackground='brown',command=lambda: indicate(home_indicate,home_page))
    home_btn.place(x=20,y=0)
    home_indicate= tk.Label(toggle_menu_fm,text='',bg='brown')
    home_indicate.place(x=3,y=0,width=5,height=45)

    profile_btn= tk.Button(toggle_menu_fm,text='Profile',font=('times new roman',20),bd=0,fg='white',bg='brown',activebackground='brown',command=lambda: indicate(profile_indicate,profile_page))
    profile_btn.place(x=20,y=50)
    profile_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    profile_indicate.place(x=3, y=50, width=5, height=45)

    menu_btn = tk.Button(toggle_menu_fm, text='Menu', font=('times new roman', 20), bd=0, fg='white', bg='brown',activebackground='brown',command=lambda: indicate(menu_indicate,menu_page))
    menu_btn.place(x=20, y=100)
    menu_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    menu_indicate.place(x=3, y=100, width=5, height=45)

    reservation_btn = tk.Button(toggle_menu_fm, text='Reservation', font=('times new roman', 20), bd=0, fg='white', bg='brown',activebackground='brown',command=lambda: indicate(reservation_indicate,reservation_page))
    reservation_btn.place(x=20, y=150)
    reservation_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    reservation_indicate.place(x=3, y=150, width=5, height=45)

    location_btn = tk.Button(toggle_menu_fm, text='Location', font=('times new roman', 20), bd=0, fg='white', bg='brown',activebackground='brown',command=lambda: indicate(location_indicate,location_page))
    location_btn.place(x=20, y=200)
    location_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    location_indicate.place(x=3, y=200, width=5, height=45)

    feedback_btn = tk.Button(toggle_menu_fm, text='Feedback', font=('times new roman', 20), bd=0, fg='white',bg='brown',activebackground='brown',command=lambda: indicate(feedback_indicate,feedback_page))
    feedback_btn.place(x=20, y=250)
    feedback_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    feedback_indicate.place(x=3, y=250, width=5, height=45)

    chatAssist_btn = tk.Button(toggle_menu_fm, text='Chat Assistant', font=('times new roman', 20), bd=0, fg='white', bg='brown',activebackground='brown',command=initialisingChat)
    chatAssist_btn.place(x=20, y=300)
    chatAssist_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    chatAssist_indicate.place(x=3, y=300, width=5, height=45)

    Exit_btn = tk.Button(toggle_menu_fm, text='Exit', font=('times new roman', 20), bd=0, fg='white',bg='brown', activebackground='brown',command=lambda: indicate(Exit_indicate, Exit_page))
    Exit_btn.place(x=20, y=350)
    Exit_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
    Exit_indicate.place(x=3, y=350, width=5, height=45)

    window_height=1080 #root.winfo_height()
    toggle_menu_fm.place(x=0,y=50, height=window_height, width=250)

    toggle_btn.config(text=' X ')
    toggle_btn.config(command=collapse_toggle_menu)


head_frame= tk.Frame(root, bg='brown')
                     #,highlightbackground='white',highlightthickness=1)

toggle_btn= tk.Button(head_frame,text=' ≡ ',bg='brown',fg='white',font=('Bold',20),bd=0,activebackground='brown',activeforeground='yellow',command=toggle_menu)
toggle_btn.place(x=10,y=0)

title_lb= tk.Label(head_frame,text='The WOK- Chinese Restaurant',fg='white',bg='brown',font=('Impact',20))
title_lb.place(x=60,y=5)

toggle_exitButton= tk.Button(head_frame,text='X',bg='brown',fg='white',font=('Bold',20),bd=0,activebackground='brown',activeforeground='yellow',command=Exit_page)
toggle_exitButton.place(x=1870,y=0)

#Logo
#image_path = r"C:\Users\Vennis\Downloads\restaurant_logo_gif.gif"
#image = tk.PhotoImage(file=image_path)
#scale_factor = 15
#resized_image = image.subsample(scale_factor, scale_factor)
#label = tk.Label(root, image=resized_image)
#label.image = resized_image
#label.place(x=60, y=5)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

main_frame= tk.Frame(root)
main_frame.pack(side=tk.RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(height=1080, width=1730)


root.mainloop()
