import re
import subprocess
import platform
import sys
import time
from matplotlib import pyplot as plt

def main(argv):
    os_type = platform.system()
    targets = ["www.apple.com", "www.google.com"]
    nbr_pings = 1
    inter_ping = 10 #sec
    plot_length = 200

    y_max = -1

    x_data = []
    y_data = []

    plt.ion()
    plt.grid()
    plt.tick_params(\
    	axis='x',
    	which='both',
    	bottom='off',
    	top='off',
    	labelbottom='off')  
    plt.ylabel('ms')

    plt.rcParams['toolbar'] = 'None'

    line, = plt.plot(y_data)

    ping_func = ping_unix
    
    while True:
	    average = -3.0

	    x_data.append(time.time())
	    
	    if os_type.lower() in ["windows"]:
	    	ping_func = ping_win
	    else:
	    	ping_func = ping_unix

	    for target in targets:
	    	average = average + ping_func(target,nbr_pings)/len(targets)

	    y_data.append(average)

	    if average > y_max:
	    	y_max = average

	    if len(y_data) > plot_length:
	    	del y_data[0]
	    	del x_data[0]

	    plt.ylim([0,y_max+5])
	    plt.xlim(min(x_data),max(x_data))

	    line.set_xdata(x_data)
	    line.set_ydata(y_data)

	    plt.draw()

	    time.sleep(inter_ping)

def ping_win(target,nbr_pings):
	return -3.0

def ping_unix(target,nbr_pings):
	average = -1.0

	try:
	    ping = subprocess.Popen(["ping", "-n", "-c",str(nbr_pings), target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    out, error = ping.communicate()
	    if out:
	    	temp = out.split("min/avg/max/stddev = ",1)[1]
	    	average = temp.split("/")[1]

	except subprocess.CalledProcessError:
	    average = -2.0

	return float(average)

if __name__ == "__main__":
	main(sys.argv)