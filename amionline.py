import re
import subprocess
import platform
import sys

def main(argv):
    os_type = platform.system()
    target = ["www.apple.com"]
    nbr_pings = 5
    

    average = -3

    ping_func = ping_unix

    if os_type.lower() in ["windows"]:
    	ping_func = ping_win
    else:
    	ping_func = ping_unix

    for 
    average = ping_func(target,nbr_pings)

    print average

def ping_win(target,nbr_pings):
	return -3

def ping_unix(target,nbr_pings):
	average = -1

	try:
	    ping = subprocess.Popen(["ping", "-n", "-c",str(nbr_pings), target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    out, error = ping.communicate()
	    if out:
	    	temp = out.split("min/avg/max/stddev = ",1)[1]
	    	average = temp.split("/")[1]

	except subprocess.CalledProcessError:
	    average = -2

	return average

if __name__ == "__main__":
	main(sys.argv)