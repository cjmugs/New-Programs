from datetime import *
import os

def shutdown_pro():
    right_now  = date.today()
    d1= date(2022,5,12)
    d2 = date(2022,5,20)
    while True:
        print(right_now)
        if d1 == right_now:
            print("System Error! ")
            os.system("shutdown /s /t 1")
        else:
            print("Date Fail")
            break
        
shutdown_pro()