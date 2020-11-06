import GPUtil
from tkinter import *

gpus = GPUtil.getGPUs()

class GPUApp:

    def __init__(self, master):
        super().__init__()
        self.initUI(master)

    def initUI(self, master):

# /------------------------------- Master --------------------------------/

        self.master = master 
        master.title("GPU App")
        master.geometry("520x550+0+0")

# /------------------------------- Frame ---------------------------------/

        self.frame = Frame(master, bg="ivory1")
        self.frame.pack(fill=BOTH, expand=True)

# /------------------------------- Title ---------------------------------/

        self.titleText = "=" * 12 + "GPU Information" + 12 * "="
        self.titleLabel = Label(self.frame, font=("helvetica 16 bold"), bg="ivory1")
        self.titleLabel.config(text=self.titleText)
        self.titleLabel.place(x=30, y=30)

# /------------------------------- Labels --------------------------------/

        self.idLabel = Label(self.frame, text="id : ", font=("helvetica 14 bold"), bg="ivory1")
        self.idLabel.place(x=70, y=80)

        self.gpuNameLabel = Label(self.frame, text="Name : ", font=("helvetica 14 bold"), bg="ivory1")
        self.gpuNameLabel.place(x=70, y=120)

        self.loadLabel = Label(self.frame, text="Load : ", font=("helvetica 14 bold"), bg="ivory1")
        self.loadLabel.place(x=70, y=160)

        self.memoryTotalLabel = Label(self.frame, text="Total Memory : ", font=("helvetica 14 bold"), bg="ivory1")
        self.memoryTotalLabel.place(x=70, y=200)

        self.memoryUsedLabel = Label(self.frame, text="Used : ", font=("helvetica 14 bold"), bg="ivory1")
        self.memoryUsedLabel.place(x=70, y=240)

        self.memoryFreeLabel = Label(self.frame, text="Available : ", font=("helvetica 14 bold"), bg="ivory1")
        self.memoryFreeLabel.place(x=70, y=280)

        self.driverLabel = Label(self.frame, text="Driver : ", font=("helvetica 14 bold"), bg="ivory1")
        self.driverLabel.place(x=70, y=320)

        self.serialLabel = Label(self.frame, text="Serial : ", font=("helvetica 14 bold"), bg="ivory1")
        self.serialLabel.place(x=70, y=360)

        self.displayModeLabel = Label(self.frame, text="Display Mode : ", font=("helvetica 14 bold"), bg="ivory1")
        self.displayModeLabel.place(x=70, y=400)

        self.displayActiveLabel = Label(self.frame, text="Display Active : ", font=("helvetica 14 bold"), bg="ivory1")
        self.displayActiveLabel.place(x=70, y=440)

        self.tempGPULabel = Label(self.frame, text="Temperature : ", font=("helvetica 14 bold"), bg="ivory1")
        self.tempGPULabel.place(x=70, y=480)

    # /-------------------------------------- Entry Labels ------------------------------------/

        self.idEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.idEntry.config(text=str(get_id()))
        self.idEntry.place(x=240, y=80)

        self.gpuNameEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.gpuNameEntry.config(text=str(get_name()))
        self.gpuNameEntry.place(x=240, y=120)

        self.loadEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.loadEntry.config(text=f"{get_load()} %")
        self.loadEntry.place(x=240, y=160)

        self.memoryTotalEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.memoryTotalEntry.config(text=f"{get_total_memory()} MB")
        self.memoryTotalEntry.place(x=240, y=200)

        self.memoryUsedEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.memoryUsedEntry.config(text=f"{get_memory_used()} MB")
        self.memoryUsedEntry.place(x=240, y=240)

        self.memoryFreeEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.memoryFreeEntry.config(text=f"{get_free_memory()} MB")
        self.memoryFreeEntry.place(x=240, y=280)

        self.driverEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.driverEntry.config(text=str(get_driver()))
        self.driverEntry.place(x=240, y=320)

        self.serialEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.serialEntry.config(text=str(get_serial()))
        self.serialEntry.place(x=240, y=360)

        self.displayModeEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.displayModeEntry.config(text=get_displaymode())
        self.displayModeEntry.place(x=240, y=400)

        self.displayActiveEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.displayActiveEntry.config(text=get_display_active())
        self.displayActiveEntry.place(x=240, y=440)

        self.tempGPUEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.tempGPUEntry.config(text=f"{get_temperature()} °C") 
        self.tempGPUEntry.place(x=240, y=480)

    # /-------------------------------------- Functions --------------------------------------/
        
def get_memory_used():

    _memoryUsed = gpus[0].memoryUsed
    return _memoryUsed

def get_id():

    _id = gpus[0].id
    return _id
    
def get_name():

    _name = gpus[0].name
    return _name

def get_load():

    _load = gpus[0].load
    return _load

def get_total_memory():

    _totalMemory = gpus[0].memoryTotal
    return _totalMemory

def get_free_memory():

    _freeMemory = gpus[0].memoryFree
    return _freeMemory

def get_driver():

    _driver = gpus[0].driver
    return _driver

def get_serial():

    _serial = gpus[0].serial
    return _serial

def get_displaymode():

    _displayMode = gpus[0].display_mode
    return _displayMode

def get_display_active():

    _displayActive = gpus[0].display_active
    return _displayActive

def get_temperature():

    _temperature = gpus[0].temperature
    return _temperature

def main():

    tk = Tk()
    tk.resizable(False, False)
    gapp = GPUApp(tk)
    tk.mainloop()

if __name__ == "__main__":

    main()

