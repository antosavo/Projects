var i = 0
val N = 2000000
var a = Array.fill(N)(1)


val start = System.nanoTime

while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}
while(i < N){a(i) = i ; i += 1}

val end = System.nanoTime

val t = (end - start)/1e9
    
println("while :" +t)


val start2 = System.nanoTime

for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;
for(i <- 0 to (N-1)) a(i) = i;

val end2 = System.nanoTime

val t2 = (end2 - start2)/1e9
    
println("for   :" +t2)
      



