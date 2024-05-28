from tkinter import *

root = Tk()
root.title("THE WOK - Chinese Restaurant")
root.state("zoomed")

image_path = r"C:\Users\Vennis\Downloads\restaurant_logo_gif.gif"
image = PhotoImage(file=image_path)
scale_factor = 2
resized_image = image.subsample(scale_factor, scale_factor)
label = Label(root, image=resized_image)
label.pack(pady=20)

def mainpage():
    global mainFrame
    mainFrame = Frame(root)  # Frame match with root window, make sure using same window(root) to link the frame
    mainFrame.pack()
    mylabel= Label(root,text="Welcome to THE WOK - Chinese Restaurant",font=("Impact",30))
    mylabel.pack(pady=20)

mainpage()

def click_menu():
    mainFrame.destroy()
    menu_window = Toplevel(root)  # Create a new window
    menu_window.title("The Wok- Food & Drinks Menu")
    menu_window.state("zoomed")

    frame_menu = Frame(menu_window, bg="light blue")
    label_menu = Label(frame_menu, text="The Wok- Food & Drinks Menu", font=("times new roman", 20))
    label_menu.pack(pady=20)
    frame_menu.pack(fill=BOTH, expand=True)
    frame_reservation.pack_forget()
    frame_direction.pack_forget()
    frame_review.pack_forget()
    frame_home.pack_forget()

def click_reservation():
    reservation_window = Toplevel(root)  # Create a new window
    reservation_window.title("The Wok- Reservation")
    reservation_window.state("zoomed")

    frame_reservation = Frame(reservation_window, bg="light blue")
    label_reservation = Label(frame_reservation, text="The Wok- Reservation", font=("times new roman", 20))
    label_reservation.pack(pady=20)
    frame_reservation.pack(fill=BOTH,expand=True)
    frame_menu.pack_forget()
    frame_direction.pack_forget()
    frame_review.pack_forget()

def click_direction():
    direction_window = Toplevel(root)  # Create a new window
    direction_window.title("The Wok- Direction & Business Hours")
    direction_window.state("zoomed")

    frame_direction = Frame(direction_window, bg="light blue")
    label_direction = Label(frame_direction, text="The Wok- Direction & Business Hours", font=("times new roman", 20))
    label_direction .pack(pady=20)
    frame_direction.pack(fill=BOTH,expand=True)
    frame_menu.pack_forget()
    frame_reservation.pack_forget()
    frame_review.pack_forget()

def click_review():
    review_window = Toplevel(root)  # Create a new window
    review_window.title("The Wok- Review")
    review_window.state("zoomed")

    frame_review = Frame(review_window, bg="light blue")
    label_review = Label(frame_review, text="The Wok- Review", font=("times new roman", 20))
    label_review.pack(pady=20)
    frame_review.pack(fill=BOTH,expand=True)
    frame_menu.pack_forget()
    frame_reservation.pack_forget()
    frame_direction.pack_forget()


# Function to change background color when button is hovered
def on_enter(event):
    event.widget.config(bg="yellow",fg="blue")

# Function to change background color when mouse pointer leaves the button
def on_leave(event):
    event.widget.config(bg="SystemButtonFace",fg="black")

def show_frame(frame):
    frame.tkraise()

frame_menu= Frame(mainFrame,bg="light blue")
label_menu= Label(frame_menu, text="The Wok- Food & Drinks Menu",font=("times new roman",20))
label_menu.pack(pady=20)

#Frame for RESERVATION
frame_reservation= Frame(mainFrame,bg="light blue")
label_reservation= Label(frame_reservation, text="The Wok- Reservation",font=("times new roman",20))
label_reservation.pack(pady=20)

#Frame for DIRECTION
frame_direction= Frame(mainFrame,bg="light blue")
label_direction= Label(frame_direction, text="The Wok- Address & Business Hours",font=("times new roman",20))
label_direction.pack(pady=20)

#Frame for REVIEW
frame_review= Frame(mainFrame,bg="light blue")
label_review= Label(frame_review, text="The Wok- Leave your review",font=("times new roman",20))
label_review.pack(pady=20)

buttonframe= Frame(root)

buttonframe.grid_columnconfigure(1, weight=1)
buttonframe.grid_columnconfigure(3, weight=1)
buttonframe.grid_columnconfigure(5, weight=1)
buttonframe.grid_columnconfigure(7, weight=1)

menu_btn = Button(buttonframe, text="View Menu",command=click_menu,font=("times new roman",18))
menu_btn.grid(row=0, column=0, padx=(0, 10))
menu_btn.bind("<Enter>", on_enter)
menu_btn.bind("<Leave>", on_leave)

reservation_btn = Button(buttonframe, text="Make Reservations", command=click_reservation,font=("times new roman",18))
reservation_btn.grid(row=0, column=2, padx=(10, 10))
reservation_btn.bind("<Enter>", on_enter)
reservation_btn.bind("<Leave>", on_leave)

direction_btn = Button(buttonframe, text="Get Directions", command=click_direction,font=("times new roman",18))
direction_btn.grid(row=0, column=4, padx=(10, 10))
direction_btn.bind("<Enter>", on_enter)
direction_btn.bind("<Leave>", on_leave)

review_button = Button(buttonframe, text="Make Review",command=click_review, font=("times new roman",18))
review_button.grid(row=0, column=6, padx=(10, 0))
review_button.bind("<Enter>", on_enter)
review_button.bind("<Leave>", on_leave)

buttonframe.pack()

root.mainloop()