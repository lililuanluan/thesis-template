set terminal pngcairo size 800,600 enhanced font 'Verdana,10'
set output 'plot.png'

set title "Coordinates Plot"
set xlabel "iteration"
set ylabel "execution"

set grid
plot 'big00.txt' using 1:2 with linespoints title 'Data Points'
