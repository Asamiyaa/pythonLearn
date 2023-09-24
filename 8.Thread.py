import time
import threading


# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time())))


# 创建两个线程
try:
   # threading.start_new_thread( print_time, ("Thread-1", 2, ) )
   # threading.start_new_thread( print_time, ("Thread-2", 4, ) )
   thread = threading.Thread(target=print_time("Thread-1",2))
   thread.start()

   thread = threading.Thread(target=print_time("Thread-2", 2))
   thread.start()


except:
   print("Error: unable to start thread")


while 1:
   pass