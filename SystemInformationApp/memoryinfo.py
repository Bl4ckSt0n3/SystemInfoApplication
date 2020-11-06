import psutil
from tkinter import *



class RAMApp:

    def __init__(self, master):
        super().__init__()
        self.initUI(master)

    def initUI(self, master):

    # /------------------------ Master Node -----------------------------/

        self.master = master 
        master.title("RAM App")
        master.geometry("520x460+0+0")

    # /---------------------------- Frame ---------------------------------/

        self.frame = Frame(self.master, bg="ivory1")
        self.frame.pack(fill=BOTH, expand=True)

    # /---------------------------- Labels -------------------------------/

        self.memTitleText = "=" * 10 + "Memory Information" + 10 * "="
        self.titleLabel = Label(self.frame, font=("helvetica 16 bold"), bg="ivory1")
        self.titleLabel.config(text=self.memTitleText)
        self.titleLabel.place(x=40, y=30)
        
        self.totalSizeLabel = Label(self.frame, text="Total Memory Size: ", font=("helvetica 14 bold"), bg="ivory1")
        self.totalSizeLabel.place(x=80, y=100)

        self.availableLabel = Label(self.frame, text="Available: ", font=("helvetica 14 bold"), bg="ivory1")
        self.availableLabel.place(x=80, y=140)

        self.usedLabel = Label(self.frame, text="Used: ", font=("helvetica 14 bold"), bg="ivory1")
        self.usedLabel.place(x=80, y=180)

        self.usagePercentLabel = Label(self.frame, text="Usage Percentage: ", font=("helvetica 14 bold"), bg="ivory1")
        self.usagePercentLabel.place(x=80, y=220)

    # /----------------------------- Entry Labels -----------------------------/
        
        self.totalSizeEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.totalSizeEntry.config(text=get_ram_size(_virtual_mem_size.total))
        self.totalSizeEntry.place(x=300, y=100)

        self.availableEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.availableEntry.config(text=get_ram_size(_virtual_mem_size.available))
        self.availableEntry.place(x=300, y=140)

        self.usedEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.usedEntry.config(text=get_ram_size(_virtual_mem_size.used))
        self.usedEntry.place(x=300, y=180)

        self.usagePercentEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.usagePercentEntry.config(text=f"{get_ram_size(_virtual_mem_size.percent)} (%)")
        self.usagePercentEntry.place(x=300, y=220)


    # /----------------------------- Functions ------------------------------/

    
_virtual_mem_size = psutil.virtual_memory()

def get_ram_size(byteSize):

    _status_dict = {1:"B", 2:"KB", 3:"MB", 4:"GB", 5:"TB", 6:"PB"}
    _key = 0
    while(True):
       _key += 1

       if byteSize < 1024:
           return f"{byteSize:.4f} {_status_dict[_key]}"

       byteSize /= 1024





        



    
def main():

    tk = Tk()
    tk.resizable(False, False)
    memApp = RAMApp(tk)
    tk.mainloop()


if __name__ == "__main__": # delete here
 
    main()


