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

#Passing Multiple Arguments:
def repeat_string(s, times):
    print(s * times)

thread = threading.Thread(target=repeat_string, args=("Hello! ", 3))

#Callable Objects with Arguments:
class Worker:
    def __call__(self, number):
        print(f"Number squared: {number * number}")

worker = Worker()
thread = threading.Thread(target=worker, args=(4,))

