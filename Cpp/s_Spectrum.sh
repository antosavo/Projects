#######Function#######

reset

#imposta il terminale
#set term wxt enhanced
set term pngcairo enhanced

#imposta i range del grafico
set xrange [-100:100]
set log y
set yrange [0.000001:1]


#imposta i nomi degli assi

set xlabel "{/Symbol \167} (1/ps)"
set ylabel "U_{r}({/Symbol \167})^{2}+U_{i}({/Symbol \167})^{2}" font ",13" offset -2.5,0,0

set xtics font ",13"
set ytics font ",13"
set format y "10^{%L}"

#disabilita la leggenda
#unset key


#do for [i=1:40] {

#x=1
#set title "Spectrum P=".x."
#set output "Spectrum_".x.".png"
set output "Spectrum.png"

#fa il grafico leggendo dal file hist.dat la colonna 1 e 2
plot "Spectrum_4.dat" u 1:(($2*$2+$3*$3)/900000) w lines lt 1 lw 2 lc rgb "red"title "Spectrum"

#}


