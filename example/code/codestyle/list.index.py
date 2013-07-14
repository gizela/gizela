"""
finding with method index of type list is two times sloewr then in dictionary
"""

l=["abcd", "abc", "aaa", "bbb", "ccc"]
d={"abcd":0, "abc":1, "aaa":2, "bbb":3, "ccc":4}

id1="abc"
id2="abcd"
id3="aaa"

i=1

if i==0:
    for i in xrange(10000000):
        p=l.index(id1)
        p=l.index(id2)
        p=l.index(id3)
        
else:
    for i in xrange(10000000):
        p=d[id1]
        p=d[id2]
        p=d[id3]
