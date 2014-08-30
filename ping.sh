#!/bin/sh

#/bin/ping -n -i 300 8.8.8.8 | while read pong; do echo "$(date): $pong"; done >> /home/pi/ping.log

HOSTS="8.8.8.8 213.100.83.1 10.0.1.1 10.0.1.53 10.0.1.2 10.0.1.51 10.0.1.52 10.0.1.54 10.0.1.55 10.0.1.56"
COUNT=4

for theHost in $HOSTS
do
  times=$(/bin/ping -n -c $COUNT $theHost | grep 'rtt' | awk -F' ' '{ print $4 }')
  if [ "$times" != "" ]
    then
      echo "$(date) - PING $theHost OK - $times" >> /home/pi/ping.log
    else
      echo "$(date) - PING $theHost FAILED" >> /home/pi/ping.log
  fi
done
