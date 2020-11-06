from tkinter import *
import socket
import platform
import cpuinfo
import gpuinfo
import memoryinfo

uname = platform.uname()

class SystemInfoApp:

    def __init__(self, master):

        super().__init__()
        self.initUI(master)
    
    def initUI(self, master):

    # /-------------------------------- Master --------------------------------/

        self.master = master
        master.title("SystemInfo")
        master.geometry("520x480+0+0")

    # /------------------------------- Menubars -------------------------------/
        
        menubar = Menu(master)
        master.config(menu=menubar)
        
        selectMenu = Menu(menubar, bg="ivory1", fg="black")
        menubar.add_cascade(label="Select Process", menu=selectMenu)
        selectMenu.add_command(label="CPU", command=cpuinfo.main)
        selectMenu.add_command(label="GPU", command=gpuinfo.main)
        selectMenu.add_command(label="RAM", command=memoryinfo.main)

    # /------------------------------- Frame ----------------------------------/

        self.frame = Frame(master, bg="ivory2")
        self.frame.pack(fill=BOTH, expand=True)

    # /-------------------------------- Labels ---------------------------------/ 

        self.infotext = "=" * 11 + "System Information" + "=" * 11
        self.infotextLabel = Label(self.frame, font=("helvetica 16 bold"), bg="ivory2")
        self.infotextLabel.config(text=self.infotext)
        self.infotextLabel.place(x=32, y=20)

        self.systemLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.systemLabel.place(x=60, y=100)
        self.systemLabel.config(text="Operating System: ")

        self.releaseSystemLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.releaseSystemLabel.place(x=60, y=150)
        self.releaseSystemLabel.config(text="OS Release: ")

        self.versionSystemLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.versionSystemLabel.place(x=60, y=200)
        self.versionSystemLabel.config(text="OS Version: ")

        self.machineNameLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.machineNameLabel.place(x=60, y=250)
        self.machineNameLabel.config(text="Machine: ")

        self.hostnameLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.hostnameLabel.place(x=60, y=300)
        self.hostnameLabel.config(text="Hostname: ")

        self.hostIPLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.hostIPLabel.place(x=60, y=350)
        self.hostIPLabel.config(text="Host IP: ")

    # /--------------------------------- Entries --------------------------------------/

        self.systemEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.systemEntry.place(x=280, y=100)
        self.systemEntry.config(text=str(self.get_system()))

        self.releaseSystemEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.releaseSystemEntry.place(x=280, y=150)
        self.releaseSystemEntry.config(text=str(self.get_release_system()))

        self.versionSystemEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.versionSystemEntry.place(x=280, y=200)
        self.versionSystemEntry.config(text=str(self.get_system_version()))

        self.machineNameEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.machineNameEntry.place(x=280, y=250)
        self.machineNameEntry.config(text=str(self.get_machine_name()))

        self.hostnameEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.hostnameEntry.place(x=280, y=300)
        self.hostnameEntry.config(text=str(self.get_hostname()))

        self.hostIPEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory2")
        self.hostIPEntry.place(x=280, y=350)
        self.hostIPEntry.config(text=str(self.get_ip()))

    def get_system(self):

        self.OS = uname.system
        return self.OS
    

    def get_release_system(self):

        self.systemRelease = uname.release
        return self.systemRelease

    def get_system_version(self):

        self.systemVersion = uname.version
        return self.systemVersion


    def get_machine_name(self):
        
        self.machineName = uname.machine
        return self.machineName

    def get_hostname(self):

        self.hostName = socket.gethostname()
        return self.hostName

    def get_ip(self):

        self.hostName = socket.gethostname()
        self.IP = socket.gethostbyname(self.hostName)
        return self.IP
        
          
def main():

    tk = Tk()
    tk.resizable(False, False)
    scktApp = SystemInfoApp(tk)
    tk.mainloop()
    

if __name__ == "__main__":

    main()
