#!/bin/sh

#/bin/ping -n -i 300 8.8.8.8 | while read pong; do echo "$(date): $pong"; done >> /home/pi/ping.log

#HOSTS="8.8.8.8 213.100.83.1 10.0.1.1 10.0.1.53 10.0.1.2 10.0.1.51 10.0.1.52 10.0.1.54 10.0.1.55 10.0.1.56"
HOSTS="8.8.8.8"
COUNT=4

for theHost in $HOSTS
do
  time=$(date '+%Y-%m-%d %H:%M:%S')
  values=$(/bin/ping -n -c $COUNT $theHost | grep 'min/avg/max' | awk -F' ' '{print $4}' | sed 's/\//,/g')
  if [ "$values" != "" ]
    then
      echo "$time,$theHost,OK,$values" >> /var/log/amionline.ping.log
    else
      echo "$time,$theHost,FAILED,-1,-1,-1,-1" >> /var/log/amionline.ping.log
  fi
done
