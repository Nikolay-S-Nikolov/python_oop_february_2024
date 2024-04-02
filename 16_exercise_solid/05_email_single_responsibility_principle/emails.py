# A class should have only one job.
# If a class has more than one responsibility, it becomes coupled.
from abc import ABC, abstractmethod


class MyContent(ABC):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class MyMl(MyContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(MyContent):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class Protocol(ABC):
    @abstractmethod
    def message(self):
        ...


class IMProtocol(Protocol):
    def message(self):
        return "I'm "


class Correspondent:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Email:

    def __init__(self, protocol: Protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: Correspondent):
        self.__sender = ''.join([self.protocol.message(), str(sender)])

    def set_receiver(self, receiver: Correspondent):
        self.__receiver = ''.join([self.protocol.message(), str(receiver)])

    def set_content(self, content: MyContent):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


my_protocol = IMProtocol()
email = Email(my_protocol)
my_sender = Correspondent('qmal')
my_receiver = Correspondent('james')
email.set_sender(my_sender)
email.set_receiver(my_receiver)
my_content = MyMl('Hello, there!')
email.set_content(my_content)
print(email)
