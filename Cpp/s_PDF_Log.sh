#load 's_PDF_Log'

reset


set term pngcairo enhanced
set termoption dashed
#set term wxt enhanced
#set term wxt
#set terminal postscript eps enhanced



set xrange [-50:1000]
set yrange [0.0000001:1]
set logscale y 10

set xtics font ",15"
set ytics font ",15"
set format y "10^{%L}"

set pointsize 0.3

#set style fill solid 0.5

set xlabel "|u|^{2} [W]" font ",16"
set ylabel "PDF(|u|^{2})" font ",16" offset -2.5,0,0

set output "PDF.png"
#set output "PDF.eps"

#unset key
set key font ",15"

set arrow from 3,0.0000001 to 3,0.1 nohead lw 3 lc rgb "black" 

plot "PDF_100.dat" u 1:2 w points pointtype 5 lc rgb "blue" title "100m", "PDF_200.dat" u 1:2 w points pointtype 5 lc rgb "green" title "200m","PDF_500.dat" u 1:2 w points pointtype 5 lc rgb "yellow" title "500m","PDF_1000.dat" u 1:2 w points pointtype 5 lc rgb "orange" title "1000m","PDF_1500.dat" u 1:2 w points pointtype 5 lc rgb "red"title "1500m"

#pause -1 "Press enter"
