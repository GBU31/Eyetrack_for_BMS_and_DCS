import tkinter as tk
from core.eyetrack import *
import threading

class App(EyeTrack):
    def __init__(self, master):
        super().__init__()

        self.master = master
        
        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=10)
        
        self.check_var = tk.BooleanVar()
        self.check_button = tk.Checkbutton(master, text="Visualize", variable=self.check_var, command=self.checker)
        self.check_button.pack(pady=10)
        
        
    def start(self):
        if not self.is_running:
            self.is_running = True
        
        thread = threading.Thread(target=self.eyetrack)
        thread.start()
            
            
            
    def stop(self):
        if self.is_running:
            self.is_running = False
            
            
    def checker(self):
        checked = self.check_var.get()
        if not checked:
            self.vis = False
        else:
            self.vis = True
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x200')
    root.title('Eyetrack')
    root.iconbitmap(r'C:\Users\RD\Desktop\Eyetrack_for_BMS_and_DCS\core\favicon.ico')
    app = App(root)
    root.mainloop()
