Result=0

def cal():
    Result = 50 + 60
    print("Inside The Method: ",Result)

def cal2():
    global Result
    Result = 60 + 80
    print("Global Variable Inside the Method: ",Result)

def cal3():
    a=20
    print("Outer Method: ",a)
    
    def inner():
        nonlocal a
        a=10
        print("Inner Function: ",a)

    inner()
    
cal()
cal2()
cal3()
print("Outside the Method: ",Result)