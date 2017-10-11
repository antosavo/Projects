a = "Hello World"

print "a=", a
print "len(a)=", len(a)
print "upper a=", a.upper()
print "split a=", a.split()

b = " The dog is hungry . The cat is bored . The snake is awake ."
print "split b=", b.split(".")

s = b.split(".")
print "join the splitted:", ".".join(s)
