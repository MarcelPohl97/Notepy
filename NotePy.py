from tkinter import *



class Window:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.resizable(0, 0)
        self.root.title("NotePy")
        self.root.configure(background='#519839')

        

class Icons:
    def __init__(self):
        self.add = PhotoImage(file="check.png")
        self.about = PhotoImage(file="about.png")
        self.add_frame = PhotoImage(file="add_frame.png")
        self.add_window = PhotoImage(file="add_window.png")
        self.chat = PhotoImage(file="chat.png")
        self.delete = PhotoImage(file="delete.png")
        self.menu = PhotoImage(file="menu.png")
        self.uncheck = PhotoImage(file="uncheck.png")
        self.uncheck2 = PhotoImage(file="uncheck2.png")
        self.change_bg = PhotoImage(file="color.png")
        self.info = PhotoImage(file="info.png")

class Frames:
    def __init__(self):
        self.notes_frame = Frame(window.root, bg="#343841", relief="sunken")
        self.notes_frame.place(width=270, height=300)
        self.note_title = Label(self.notes_frame, text=menu.add_title_frame.get(), anchor="w", bg="#8F9297")
        self.note_title.place(relx=0, rely=0, relwidth=1, relheight=0.11)
        self.deleteB = Button(self.note_title, text="X", image=icons.uncheck, command=self.delete_frame, bg="#8F9297")
        self.deleteB.pack(side=RIGHT)
        self.addB = Button(self.notes_frame, text="ADD NOTE", image=icons.add_frame, command=self.add_note, bg="#8F9297")
        self.addB.place(rely=0.12, relx=0.733)
        self.deleteN = Button(self.notes_frame, text="DEL-N", image=icons.delete, command=self.del_Note, bg="#8F9297")
        self.deleteN.place(rely=0.12, relx=0.843)
        self.note_list = Listbox(self.notes_frame, bg="#8F9297", relief="ridge")
        self.note_list.place(rely=0.22, relx=0.05, relheight=0.7, relwidth=0.9)
        self.entry_list = Entry(self.notes_frame)
        self.entry_list.place(rely=0.118, relx=0.27, height=30)
        self.check_Note = Button(self.notes_frame, text="Check", image=icons.add, command=self.check_note, bg="#8F9297")
        self.check_Note.place(rely=0.12, relx=0.05)
        self.uncheck_Note = Button(self.notes_frame, text="Uncheck", image=icons.uncheck2, command=self.uncheck_note, bg="#8F9297")
        self.uncheck_Note.place(rely=0.12, relx=0.163)

    def delete_frame(self):
        self.notes_frame.destroy()
        frames.remove(self)

    def add_note(self):
        self.note_list.insert(END, self.entry_list.get())

    def del_Note(self):
        self.note_list.delete(self.note_list.curselection())

    def check_note(self):
        self.get_note = self.note_list.curselection()
        self.note_list.itemconfig(self.get_note, bg="green")
        

    def uncheck_note(self):
        self.get_note = self.note_list.curselection()
        self.note_list.itemconfig(self.get_note, bg="white")

        
class DragNDrop:
    def __init__(self):
        pass
    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y

    def on_drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)
        

class Menu:
    def __init__(self):
        self.header = Label(window.root, text="NotePy", font=("Arial", 14), fg="#FFFFFF", bg="#458131", height=2)
        self.header.pack(fill=X)
        self.size_options = ["1920x1080", "1680x1050", "1440x900", "1280x800", "1024x768", "800x600"]
        self.get_size = {"1920x1080": "1920x1080",
                         "1680x1050": "1680x1050",
                         "1440x900": "1440x900",
                         "1280x800": "1280x800",
                         "1024x768": "1024x768",
                         "800x600": "800x600"}
        self.size = StringVar(window.root)
        self.app_size = OptionMenu(self.header, self.size, *self.size_options, command=self.set_window_size)
        self.app_size.pack(side=RIGHT)
        self.app_size.config(indicatoron=0, image=icons.menu, bg='#EBECF0')
        self.add_note_frame = Button(self.header, bg="#EBECF0", image=icons.add_window, command=self.add_frames)
        self.add_note_frame.pack(side=RIGHT)
        self.add_title_frame = Entry(self.header, width=25)
        self.add_title_frame.pack(side=RIGHT, fill=Y,padx=1)
        self.about = Button(self.header, bg="#EBECF0", image=icons.about)
        self.about.pack(side=LEFT)
        self.info = Button(self.header, bg="#EBECF0", image=icons.info)
        self.info.pack(side=LEFT)
        self.size_options = ["orange", "blue", "red", "green", "purple", "lightblue"]
        self.get_colors = {"orange": ["#B37B2C", "#D29034"],
                         "blue": ["#0067A3", "#0079BF"],
                         "red": ["#963C2B", "#B04632"],
                         "green": ["#458131", "#519839"],
                         "purple": ["#755286", "#89609E"],
                         "lightblue": ["#0094AE", "#00AECC"]}
        self.background = StringVar(window.root)
        self.color_change= OptionMenu(self.header, self.background, *self.get_colors, command=self.change_bg)
        self.color_change.pack(side=LEFT)
        self.color_change.config(indicatoron=0, image=icons.change_bg, bg='#EBECF0')
        self.chat_open = Button(self.header, bg="#EBECF0", image=icons.chat)
        self.chat_open.pack(side=LEFT, padx=1)


    def add_frames(self):
        frames.append(Frames())

    def set_window_size(self, resolution):
        action = self.get_size.get(resolution)
        if action:
            window.root.geometry(action)
            window.root.resizable(0, 0)

    def change_bg(self, bg):
        self.background_color = self.get_colors.get(bg)
        if self.background_color:
            self.header["bg"] = self.background_color[0]
            window.root.configure(bg=self.background_color[1])
            
                
        
window = Window()

icons = Icons()

frames = []

drag = DragNDrop()

menu = Menu()



while True:
    for i in frames:
        drag.make_draggable(i.notes_frame)
    window.root.after(1)
    window.root.update()


