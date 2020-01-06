from tkinter import *



class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.width = width
        self.height = height
        self.root.geometry(width + "x" + height)
        self.background = Frame(self.root, bg="green")
        self.background.place(width=800, height=600)
        

class Frames:
    def __init__(self):
        self.notes_frame = Frame(window.background, bg="red", height=300, width=300, relief="sunken")
        self.notes_frame.place(relwidth=0.3, relheight=0.3)
        self.note_title = Label(self.notes_frame, text=menu.add_title_frame.get(), bg="orange")
        self.note_title.place(relx=0, rely=0, relwidth=0.5, relheight=0.15)
        self.deleteB = Button(self.notes_frame, text="X", command=self.delete_frame, bg="blue")
        self.deleteB.place(rely=0, relx=0.92)
        self.addB = Button(self.notes_frame, text="ADD NOTE", command=self.add_note, bg="blue")
        self.addB.place(rely=0, relx=0.55)
        self.deleteN = Button(self.notes_frame, text="DEL-N", command=self.del_Note, bg="blue")
        self.deleteN.place(rely=0, relx=0.70)
        self.note_list = Listbox(self.notes_frame)
        self.note_list.place(rely=0.2, relx=0, height=100)
        self.entry_list = Entry(self.notes_frame)
        self.entry_list.place(rely=0.15, relx=0.53)
        self.check_Note = Button(self.notes_frame, text="Check", command=self.check_note, bg="blue")
        self.check_Note.place(rely=0.3, relx=0.53)
        self.uncheck_Note = Button(self.notes_frame, text="Uncheck", command=self.uncheck_note, bg="blue")
        self.uncheck_Note.place(rely=0.3, relx=0.73)

    def delete_frame(self):
        self.notes_frame.destroy()
        frames.remove(self)

    def add_note(self):
        self.note_list.insert(END, self.entry_list.get())

    def del_Note(self):
        self.note_list.delete(self.note_list.curselection())

    def check_note(self):
        global width
        self.get_note = self.note_list.curselection()
        self.note_list.itemconfig(self.get_note, bg="green")
        print(menu.size.get())

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
        self.add_note_frame = Button(window.background, width=3, height=1, bg="blue", command=self.add_frames)
        self.add_note_frame.pack()
        self.add_title_frame = Entry(window.background)
        self.add_title_frame.pack()
        self.size_options = ["1920x1080", "1680x1050", "1440x900", "1280x800", "1024x768", "800x600"]
        self.size = StringVar(window.root)
        self.app_size = OptionMenu(window.background, self.size, *self.size_options)
        self.app_size.pack()


    def add_frames(self):
        frames.append(Frames())
                
        
window = Window("1", "600")

frames = []

drag = DragNDrop()

menu = Menu()



while True:
    for i in frames:
        drag.make_draggable(i.notes_frame)
    window.root.after(1)
    window.root.update()

