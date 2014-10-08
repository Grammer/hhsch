a = [0] * int(150)
methods=0
def foo(q,n,v):
    if n < q:
        return
    if q == 1:
        if n > v:
            return
        a[0] = n
        global methods
        methods+=1
        return
    if n < v:
        a[q-1] = n
    else:
        a[q-1] = v
    while a[q - 1]>0:
        a[q - 1]-=1
        foo( q - 1, n - a[q - 1], a[q - 1] )

n = int(input("Enter the number to count partitions for (number should be positive and less then 150): "))
k = int(input("Enter the number of partitions (also positive and less then 150): "))
if (n <= 0 or n > 150 or k <= 0 or k > 150 or n < k):
    print "Wrong numbers"

foo(k,n,n)
if n%k == 0:
    methods += 1
if methods == 0:
    print "No methods"
else:
    print "Number of methods: " +  str(methods)
