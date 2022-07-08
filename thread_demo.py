import threading
import time
import logging

logging.info("hello")
logging.warning("Watch out!")
logging.debug("这是个bug！")
logging.basicConfig(filename="example.log",level=logging.DEBUG)


def task():
    time.sleep(5)

def main():
    start_time = time.time()
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    end_time = time.time()
    print(end_time-start_time)

if __name__ == '__main__':
    main()
