set terminal postscript eps enhanced
set title relay
set size 1,1
set key top right Left
set xtic auto
set ytic auto
set xlabel "Days"
set ylabel "BW Deviation"
plot relay."/gabelmoo.csv" u 1:2 title 'gabelmoo' w lines lw 2 lt 0 lc rgb "red", \
     relay."/maatuska.csv" u 1:2 title 'maatuska' w lines lw 2 lt 1 lc rgb "blue", \
     relay."/moria1.csv" u 1:2 title 'moria1' w lines lw 2 lt 2 lc rgb "green", \
     relay."/tor26.csv" u 1:2 title 'tor26' w lines lw 2 lt 3 lc rgb "black"