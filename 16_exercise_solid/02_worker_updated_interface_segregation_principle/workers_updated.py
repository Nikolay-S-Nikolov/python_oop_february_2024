# ISP - Classes should not be forced to implement interfaces they do not use.

from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        ...


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        ...


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class LazyWorker(Eatable):

    def eat(self):
        print("I'm lazy. I'm only eating....")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkManager(BaseManager):

    def set_worker(self, worker):
        if not isinstance(worker, Workable):
            raise AssertionError(f"`worker` must be of type {Workable}")

        self.worker = worker

    def manage(self):
        self.worker.work()


class BrakeManager(BaseManager):

    def set_worker(self, worker):
        if not isinstance(worker, Eatable):
            raise AssertionError(f"`worker` must be of type {Eatable}")
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


manager = WorkManager()
r_worker = Robot()
manager.set_worker(r_worker)
manager.manage()

super_worker = SuperWorker()
b_manger = BrakeManager()
b_manger.set_worker(super_worker)
b_manger.lunch_break()
b_manger.set_worker(r_worker)
# l_worker = LazyWorker()
# manager.set_worker(l_worker)



