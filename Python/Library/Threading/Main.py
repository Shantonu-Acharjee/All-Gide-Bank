import threading
import time

def func(y):
    print('Ran')
    time.sleep(1)
    print('Done')
    print(y)


x = threading.Thread(target=func, args=(4,))
x.start()


print(threading.activeCount())