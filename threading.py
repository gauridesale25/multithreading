import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

func(4)
func(3)
func(2)

#output
#sleeping for 4 seconds
#sleeping for 3 seconds
#sleeping for 2 seconds

#same code using threads
#threading syntax-> t1(variable)=threading.Thread(target=function_name, args=[arguments])

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t2=threading.Thread(target=func,args=[2])
#.start() function is used to start the thread and starts the work as soon as it is written and therefore ee
t1.start()
t2.start()
t3.start()

