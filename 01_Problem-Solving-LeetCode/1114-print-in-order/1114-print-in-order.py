# Method 1 -------------------------------------------------------------------

class Foo:
    def __init__(self):
        self.firstDone = False
        self.secondDone = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.firstDone = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.firstDone:
            continue
        printSecond()
        self.secondDone = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.secondDone:
            continue
        printThird()
        
        
# Method 2 -------------------------------------------------------------------
        
import threading
class Foo:
    def __init__(self):
		# create lock to control sequence between first and second functions
        self.lock1 = threading.Lock()
        self.lock1.acquire()
		# create another lock to control sequence between second and third functions
        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
		# since second function is waiting for the lock1, let's release it
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
		# wait for first funtion to finish
        self.lock1.acquire()
        printSecond()
		# let's release lock2, so third function can run
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
		# wait for second funtion to finish
        self.lock2.acquire()
        printThird()


# Method 3 -------------------------------------------------------------------
        
import threading
class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()
