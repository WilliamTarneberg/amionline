import re
import subprocess
website = "google.com"

def main(argv):
    # My code here
    pass

if __name__ == "__main__":
    main(sys.argv)

def ping(target)
try:
    ping = subprocess.Popen(["ping", "-n", "-c 5", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = ping.communicate()
    if out:
        try:
            minimum = int(re.findall(r"Minimum = (\d+)", out)[0])
            maximum = int(re.findall(r"Maximum = (\d+)", out)[0])
            average = int(re.findall(r"Average = (\d+)", out)[0])
            packet = int(re.findall(r"Lost = (\d+)", out)[0])
            if packet > 1:
                packet = 5 / packet * 100

            print "average ms"
        except:
            print "no data for one of minimum,maximum,average,packet"
    else:
        print 'No ping'

except subprocess.CalledProcessError:
    print "Couldn't get a ping"