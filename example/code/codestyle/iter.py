def gen_a():
    for i in range(10):
        yield i

def gen_b():
    for i in (1,2):
        for j in gen_a():
            yield j


#for i in gen_a():
#    print i

for i in gen_b():
    print i 
