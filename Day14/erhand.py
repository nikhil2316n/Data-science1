
#23/09/25

def cube(x):
    if x<0:
        raise ValueError("Input cannot be negative") #rasie: used to raise a error/define a error
    
    
    else:
        return x**3

print(cube(-1))

