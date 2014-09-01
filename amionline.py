import re
import subprocess
import platform
import sys
import time
import matplotlib.pyplot as plt

def main(argv):
    os_type = platform.system()
    targets = ["www.apple.com", "www.google.com"]
    nbr_pings = 1
    inter_ping = 10 #sec
    plot_length = 200

    achart = ASCIIChart(10,5)

    y_max = -1

    x_data = []
    y_data = []

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

	    y_data.append(float(average))

	    if average > y_max:
	    	y_max = average

	    if len(y_data) > plot_length:
	    	del y_data[0]
	    	del x_data[0]

	    print y_data

	    achart.renderGraph(y_data)

	    time.sleep(inter_ping)

def ping_win(target,nbr_pings):
	return -3.0

def ping_unix(target,nbr_pings):
	average = -1.0

	try:
	    ping = subprocess.Popen(["ping", "-n", "-c",str(nbr_pings), target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    out, error = ping.communicate()
	    if out:
			#temp = out.split("min/avg/max/mdev = ",1)[1]    # Debian
	    	temp = out.split("min/avg/max/stddev = ",1)[1]  #Darwin
	    	average = temp.split("/")[1]

	except subprocess.CalledProcessError:
	    average = -2.0

	return float(average)

class ASCIIChart:
	y_max = 50
	y_min = 0
	x = -1
	y = -1
	thresh = -1

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.chart_map = [[' ' for x in xrange(x+1)] for x in xrange(y+4)] 
		self.thresh = self.y_max/self.y

	description = "ASCII Chart"
	author = "William Tarneberg"

	def renderGraph(*y_data):
		index = 4

		for value in reversed(y_data):
			if value[0] > ASCIIChart.y_max:
				y_max = value[0] + 5
				thresh = y_max / self.y

			y_corr = value[0]/ASCIIChart.thresh
			ASCIIChart.chart_map[index][y_corr] = '*'
			value +1

		print chart_map

if __name__ == "__main__":
	main(sys.argv)