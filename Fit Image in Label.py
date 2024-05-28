from tkinter import *

root = Tk()
root.title('The WOK- Menu')
root.geometry('1920x1080')

photo = PhotoImage(file=r"C:\Users\Vennis\Downloads\friedrice.png")

# Create a resized version of the image
resized_photo = photo.subsample(2, 2)  # Example: downscale the image by a factor of 2

def fit_size():
    global resized_photo
    # Get the desired width and height
    width = label.winfo_width()
    height = label.winfo_height()
    # Calculate the subsample factors to maintain aspect ratio
    x_subsample = photo.width() // width
    y_subsample = photo.height() // height
    # Use the larger subsample factor to avoid distortion
    subsample_factor = max(x_subsample, y_subsample)
    # Create a resized image
    resized_photo = photo.subsample(subsample_factor)
    # Update the label with the new image
    label.configure(image=resized_photo)
    label.image = resized_photo

label = Label(root, image=resized_photo, width=300, height=300)
label.image = resized_photo
button = Button(root, text='Resize', command=fit_size)

label.place(x=50, y=50)
button.place(x=50, y=400)

root.mainloop()














from tkinter import *

root = Tk()
root.title('The WOK- Menu')
root.geometry('1920x1080')

photo = PhotoImage(file=r"C:\Users\Vennis\Downloads\friedrice.png")

# Create a resized version of the image
resized_photo = photo.subsample(2, 2)  # Example: downscale the image by a factor of 2

def fit_size(event):
    global resized_photo
    # Get the desired width and height from the event
    width = event.width
    height = event.height
    # Calculate the subsample factors to maintain aspect ratio
    x_subsample = max(1, photo.width() // width)
    y_subsample = max(1, photo.height() // height)
    # Use the larger subsample factor to avoid distortion
    subsample_factor = max(x_subsample, y_subsample)
    # Create a resized image
    resized_photo = photo.subsample(subsample_factor)
    # Update the label with the new image
    label.configure(image=resized_photo)
    label.image = resized_photo

label = Label(root, image=resized_photo, width=300, height=300)
label.image = resized_photo

# Bind the <Configure> event to the fit_size function
label.bind('<Configure>', fit_size)

label.place(x=50, y=0)

root.mainloop()