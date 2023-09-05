def outer_function(n1,n2):
    def inner_function(n1,n2):
        return n1+n2
    sum=inner_function(n1,n2)
    return sum+5
print(outer_function(155,20))
