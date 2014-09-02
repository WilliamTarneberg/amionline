set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 1000, 500
set datafile separator ","
set output "/var/www/ping.1.png"
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%m-%d\n%H:%M"
set title "ping.sh"
set xlabel "Time"
set ylabel "Latency [ms]"
#set grid
set xtic auto
set ytic auto
set xrange ["2014-08-31 16:00:00":*]
#set yrange [-1:100]
set style line 1 lt 1 lw 1 pt 0 lc rgb "#6666FF"
set style line 2 lt 1 lw 1 pt 0 lc rgb "#0000FF"
set style line 3 lt 1 lw 1 pt 0 lc rgb "#6666FF"
set style line 4 lt 1 lw 1 pt 2 lc rgb "#FF0000"
set style fill transparent solid 0.25 border
set style data lines
# "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $6:1/0) title "max" ls 1
# "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $4:1/0) title "min" ls 3
plot "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $4:1/0):6 \
            title "min max" with filledcurve lc rgb "#CCCCCC",\
     "/var/log/amionline.ping.log" using 1:(stringcolumn(2) eq "8.8.8.8"? $5:1/0) \
            title "avg" with linespoint ls 2, \
     "/var/log/amionline.ping.log" using 1:(stringcolumn(3) eq "FAILED"? 0:1/0) \
            title "failed" with points ls 4
