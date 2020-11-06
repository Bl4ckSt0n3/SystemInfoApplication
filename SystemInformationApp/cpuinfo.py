from tkinter import *
import psutil
import platform


uname = platform.uname()

class CpuApp:

    def __init__(self, master):
        super().__init__()

        self.initUI(master)
    def initUI(self, master):

    # /-------------------------------- Master --------------------------------/

        self.master = master
        master.title("cpuInfo")
        master.geometry("620x680+0+0")

    # /------------------------------- Frame ----------------------------------/

        self.frame = Frame(master, bg="ivory1")
        self.frame.pack(fill=BOTH, expand=True)

    # /------------------------------- Title ----------------------------------/

        self.infotext = "=" * 17 + "CPU Information" + "=" * 17
        self.infotextLabel = Label(self.frame, font=("helvetica 15 bold"), bg="ivory1")
        self.infotextLabel.config(text=self.infotext)
        self.infotextLabel.place(x=25, y=20)

    # /-------------------------------- CPU Info Labels ---------------------------------/ 

        self.processorLabel = Label(self.frame, text="Processor : ", font=("helvetica 14 bold"), bg="ivory1")
        self.processorLabel.place(x=40, y=80)

        self.machineNameLabel = Label(self.frame, text="Machine : ", font=("helvetica 14 bold"), bg="ivory1")
        self.machineNameLabel.place(x=40, y=115)

        self.physicalCoreLabel = Label(self.frame, text="Number of Physical Core : ", font=("helvetica 14 bold"), bg="ivory1")
        self.physicalCoreLabel.place(x=40, y=150)

        self.logicalCoreLabel = Label(self.frame, text="Number of Logical Core : ", font=("helvetica 14 bold"), bg="ivory1")
        self.logicalCoreLabel.place(x=40, y=185)

        self.maxFreqLabel = Label(self.frame, text="Max CPU Frequency : ", font=("helvetica 14 bold"), bg="ivory1")
        self.maxFreqLabel.place(x=40, y=220)

        self.minFreqLabel = Label(self.frame, text="Min CPU Frequency : ", font=("helvetica 14 bold"), bg="ivory1")
        self.minFreqLabel.place(x=40, y=255)

        self.curFreqLabel = Label(self.frame, text="Current CPU Frequency : ", font=("helvetica 14 bold"), bg="ivory1")
        self.curFreqLabel.place(x=40, y=290)

    # /-------------------------------- Total CPU Usage -------------------------------------/

        self.totalCpuUsageLabel = Label(self.frame, text="Total CPU Usage(%)", font=("helvetica 15 bold"), bg="ivory1")
        self.totalCpuUsageLabel.place(x=340, y=420)

        self.totalCpuUsageEntry = Label(self.frame, font=("helvetica 15 bold"), bg="ivory1")
        self.totalCpuUsageEntry.config(text=str("{} %".format(psutil.cpu_percent())))
        self.totalCpuUsageEntry.place(x=400, y=460)

    # /------------------------------- CPU Info Entry Labels ----------------------------------------/

        self.processorEntry = Label(self.frame, font=("helvetica 13 bold"), bg="ivory1")
        self.processorEntry.config(text=str(uname.processor))
        self.processorEntry.place(x=180, y=84)

        self.machineNameEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.machineNameEntry.config(text=str(uname.machine))
        self.machineNameEntry.place(x=320, y=115)

        self.physicalCoreEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.physicalCoreEntry.config(text=str(self.get_physical_core()))
        self.physicalCoreEntry.place(x=320, y=150)

        self.logicalCoreEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.logicalCoreEntry.config(text=str(self.get_logical_core()))
        self.logicalCoreEntry.place(x=320, y=185)

        self.maxFreqEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.maxFreqEntry.config(text=str("{} Mhz".format(self.get_max_freq())))
        self.maxFreqEntry.place(x=320, y=220)

        self.minFreqEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.minFreqEntry.config(text=str("{} Mhz".format(self.get_min_freq())))
        self.minFreqEntry.place(x=320, y=255)

        self.curFreqEntry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.curFreqEntry.config(text=str("{} Mhz".format(self.get_current_freq())))
        self.curFreqEntry.place(x=320, y=290)
    
    # /---------------------------------- Core Info Labels ------------------------------------/

        self.corePercentageTitle = Label(self.frame, text="Usage Percentages Of Cores", font=("helvetica 16 bold"), bg="ivory1")
        self.corePercentageTitle.place(x=30, y=340)
    

        self.core1Label = Label(self.frame,text="Core 1  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core1Label.place(x=70, y=390)

        self.core2Label = Label(self.frame,text="Core 2  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core2Label.place(x=70, y=420)

        self.core3Label = Label(self.frame,text="Core 3  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core3Label.place(x=70, y=450)

        self.core4Label = Label(self.frame,text="Core 4  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core4Label.place(x=70, y=480)

        self.core5Label = Label(self.frame,text="Core 5  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core5Label.place(x=70, y=510)

        self.core6Label = Label(self.frame,text="Core 6  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core6Label.place(x=70, y=540)

        self.core7Label = Label(self.frame,text="Core 7  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core7Label.place(x=70, y=570)

        self.core8Label = Label(self.frame,text="Core 8  :  ", font=("helvetica 14 bold"), bg="ivory1")
        self.core8Label.place(x=70, y=600)
    
    # /--------------------------------- Core Info Entry Labels ----------------------------------/

        self.core1Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core1Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[0])))
        self.core1Entry.place(x=170, y=390)

        self.core2Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core2Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[1])))
        self.core2Entry.place(x=170, y=420)

        self.core3Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core3Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[2])))
        self.core3Entry.place(x=170, y=450)

        self.core4Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core4Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[3])))
        self.core4Entry.place(x=170, y=480)

        self.core5Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core5Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[4])))
        self.core5Entry.place(x=170, y=510)

        self.core6Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core6Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[5])))
        self.core6Entry.place(x=170, y=540)

        self.core7Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core7Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[6])))
        self.core7Entry.place(x=170, y=570)

        self.core8Entry = Label(self.frame, font=("helvetica 14 bold"), bg="ivory1")
        self.core8Entry.config(text=str("% {}".format(psutil.cpu_percent(percpu=True)[7])))
        self.core8Entry.place(x=170, y=600)


    # /------------------------------------ Functions --------------------------------------/

    def get_physical_core(self):

        self.physicalCores = psutil.cpu_count(logical=False)
        return self.physicalCores

    def get_logical_core(self):

        self.logicalCores = psutil.cpu_count(logical=True)
        return self.logicalCores
    
    def get_max_freq(self):

        self.cpuFreq = psutil.cpu_freq()
        self.maxFreq = self.cpuFreq.max
        return self.maxFreq

    def get_min_freq(self):

        self.cpuFreq = psutil.cpu_freq()
        self.minFreq = self.cpuFreq.min
        return self.minFreq

    def get_current_freq(self):

        self.cpuFreq = psutil.cpu_freq()
        self.currFreq = self.cpuFreq.current
        return self.currFreq


def main():

    tk = Tk()
    tk.resizable(False, False)
    cpuApp = CpuApp(tk)
    tk.mainloop() 


if __name__ == "__main__": # delete here
 
    main()