# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 660, 320 
set datafile separator ","
set output "/var/www/ping.1.png"
set terminal png
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%m-%d\n%H:%M"
set title "ping.sh"
set xlabel "Time"
set ylabel "[ms]"
#set grid
set xtic auto
set ytic auto
#set xrange ["2014-08-28 00:00:00":"2014-08-31 23:59:59"]
#show xrange
set style line 1 lt 1 lw 1 pt 0 lc rgb "gray"
set style line 2 lt 1 lw 1 pt 0 lc rgb "blue"
set style line 3 lt 1 lw 1 pt 0 lc rgb "gray"
set style line 4 lt 1 lw 1 pt 2 lc rgb "red"
plot "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $6:1/0) title "max" ls 1,\
     "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $5:1/0) title "avg" with linespoints ls 2,\
     "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $4:1/0) title "min" ls 3
