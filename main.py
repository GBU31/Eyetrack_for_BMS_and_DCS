from core.tkapp import *

def main():
    root = tk.Tk()
    root.geometry('300x200')
    root.title('Eyetrack')
    root.iconbitmap('core/favicon.ico')
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()