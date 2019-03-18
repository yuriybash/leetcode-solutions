def outer():

    x = 3

    def inner():
        
        x = x + 1

    inner()

outer()