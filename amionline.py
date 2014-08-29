import re
import subprocess
import platform
import sys
import time

def main(argv):
    os_type = platform.system()
    targets = ["www.apple.com", "www.google.com"]
    nbr_pings = 1
    inter_ping = 30

    while True:
	    average = -3.0

	    ping_func = ping_unix

	    if os_type.lower() in ["windows"]:
	    	ping_func = ping_win
	    else:
	    	ping_func = ping_unix

	    for target in targets:
	    	average = average + ping_func(target,nbr_pings)/len(targets)

	    print average

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