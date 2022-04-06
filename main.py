import matplotlib.pyplot as plt
import numpy as np
"""Chris Sequeira 8 April 2022
    Convert project data into graphs with numpy and matplot lib. 
    One graph per process level statistic, and one each for the system data 
    Nia, I'm sorry this isn't remotely optimized"""


#convert CSVs into decimal NumPy arrays
apm1 = np.loadtxt("APM1_metrics.csv", dtype=float, delimiter=",") #blue
apm2 = np.loadtxt("APM2_metrics.csv", dtype=float, delimiter=",") #black
apm3 = np.loadtxt("APM3_metrics.csv", dtype=float, delimiter=",") #red
apm4 = np.loadtxt("APM4_metrics.csv", dtype=float, delimiter=",") #green
apm5 = np.loadtxt("APM5_metrics.csv", dtype=float, delimiter=",") #yellow
apm6 = np.loadtxt("APM6_metrics.csv", dtype=float, delimiter=",") #cyan
system = np.loadtxt("system_metrics.csv", dtype=float, delimiter=",")

#output
def cpu():
#use second column (column #1)
    plt.plot(apm1[:,1], color = 'blue', label = 'apm1')
    plt.plot(apm2[:,1], color = 'black', label = 'apm2')
    plt.plot(apm3[:,1], color = 'red', label = 'apm3')
    plt.plot(apm4[:,1], color = 'green', label = 'apm4')
    plt.plot(apm5[:,1], color = 'yellow', label = 'apm5')
    plt.plot(apm6[:,1], color = 'cyan', label = 'apm6')

    plt.legend(loc='best')
    plt.ylabel('CPU Usage (%)')
    plt.xlabel('Time (s)')
    plt.title('CPU Usage over Time')
    plt.savefig('cpu.png')
    plt.close()

def memoryUtilization():
    #use third column (column #2)
    plt.plot(apm1[:,2], color = 'blue', label = 'apm1')
    plt.plot(apm2[:,2], color = 'black', label = 'apm2')
    plt.plot(apm3[:,2], color = 'red', label = 'apm3')
    plt.plot(apm4[:,2], color = 'green', label = 'apm4')
    plt.plot(apm5[:,2], color = 'yellow', label = 'apm5')
    plt.plot(apm6[:,2], color = 'cyan', label = 'apm6')

    plt.legend(loc='best')
    plt.ylabel('Memory Usage (%)')
    plt.xlabel('Time (s)')
    plt.title('Memory Usage over Time')
    plt.savefig('memory.png')
    plt.close()

def bandwidthUtilization():
    #rx data: second column (column #1)
    #tx data: third column (column #2)
    plt.plot(system[:,1], color = 'cyan', label = 'Read Volume')
    plt.plot(system[:,2], color = 'pink', label = 'Write Volume')
    plt.legend(loc='best')
    plt.ylabel('kB/s')
    plt.xlabel('Time (s)')
    plt.title('Badwidth Usage over Time')
    plt.savefig('bandwidth.png')
    plt.close()

def diskAccess():
    #disk access rates: fourth column (column #3)
    plt.plot(system[:,3], color = 'orange', label = 'Disk Access Rates')
    plt.legend(loc='best')
    plt.ylabel('Data Writes (kB/s)')
    plt.xlabel('Time (s)')
    plt.title('Disk Access over Time')
    plt.savefig('disk_access.png')
    plt.close()

def diskUtilization():
    #disk usage rates: fifth column (column #4)
    plt.plot(system[:,4], color = 'purple', label = 'Disk Usage (kB)')
    plt.legend(loc='best')
    plt.ylabel('Disk Capacity (Mb)')
    plt.xlabel('Time (s)')
    plt.title('Disk Utilization over Time')
    plt.show()
    plt.savefig('disk_util.png')
    plt.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cpu()
    memoryUtilization()
    bandwidthUtilization()
    diskAccess()
    diskUtilization()
