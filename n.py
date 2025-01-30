from tkinter import Tk, Button

def open_chatbot():
    # Your function to open the chatbot goes here
    pass

root = Tk()
root.geometry("300x200")  # Set window size for demonstration

start_button_bottom = Button(root, text="Start", command=open_chatbot, width=20, height=2, bg="#0097b2")
start_button_bottom.pack(side="bottom", pady=20, anchor='s')

root.mainloop()
