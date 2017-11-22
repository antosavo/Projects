#######Function#######

reset

#imposta il terminale
#set term wxt enhanced
set term pngcairo enhanced

#imposta i range del grafico
set xrange [-10:10]
set yrange [0:120]


#imposta i nomi degli assi
set xlabel "t"
set ylabel "|U|^{2}" font ",13" offset -2.5,0,0

set xtics font ",13"
set ytics font ",13"
#set format y "10^{%L}"

#disabilita la leggenda
#unset key

#do for [i=1:40] {

#x=1
#set title "Intensity Op=".x."
#set output "Intensity_".x.".png"
set output "Intensity.png"

#fa il grafico leggendo dal file hist.dat la colonna 1 e 2
plot "Intensity_0.dat" u 1:2 w lines lt 1 lw 2 lc rgb "blue" title "z_0", "Intensity_1.dat" u 1:2 w lines lt 1 lw 2 lc rgb "green" title "z_1","Intensity_2.dat" u 1:2 w lines lt 1 lw 2 lc rgb "yellow" title "z_2","Intensity_3.dat" u 1:2 w lines lt 1 lw 2 lc rgb "orange" title "z_3","Intensity_4.dat" u 1:2 w lines lt 1 lw 2 lc rgb "red"title "z_4"