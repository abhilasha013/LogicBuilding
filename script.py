'''
#create two threads and ensure they run concurrently
import threading
def print_thread1():
   print("thread1")

def print_thread2():
   print("thread2")

thread1 = threading.Thread(target=print_thread1)
thread2 = threading.Thread(target=print_thread2)

#to strt thread
thread1.start() 
thread2.start()






thread1.join()
thread2.join()
'''
#Threading with arguments
#a thread which takes a list of integers as an argument and prints each integer squared.
import threading


def squares(numbers):
    print(f"The square of {numbers} is {numbers * numbers}")

numbers = 9
thread = threading.Thread(target=squares, args=(numbers,))
thread.start()
thread.join()

