import subprocess
import re
import platform

website = "10.0.1.1"
count = "5"

print platform.system()

try:
   ping = subprocess.Popen(["/bin/ping","-n","-c",count,website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, error = ping.communicate()
   print out
   if out:
#       try:
           minimum = int(re.findall(r"Minimum = (\d+)", out)[0])
           maximum = int(re.findall(r"Maximum = (\d+)", out)[0])
           average = int(re.findall(r"Average = (\d+)", out)[0])
           packet = int(re.findall(r"Lost = (\d+)", out)[0])
           if packet > 1:
               packet = 5 / packet * 100

           print "average ms"
#       except:
#           print "no data for one of minimum,maximum,average,packet"
   else:
       print 'No ping'

except subprocess.CalledProcessError:
   print "Couldn't get a ping"
