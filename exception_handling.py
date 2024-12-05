"""syntax of exception handling
try:
    code to check error aauna sakni code
except:
    handling an Exception
finally:
    running the code to be run after exception checking        """
a=1
b=0

try:
    print("resource open")
    print(a/b)
    print("resource closed")# yeo line run hudaina because already exception is occur in a/b
except Exception as e:
    print(e)
    print("you can not divide a number by 0")
finally:
    print("this is run after try catch block")
