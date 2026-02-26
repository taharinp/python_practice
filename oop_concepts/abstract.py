from abc import abstractmethod, ABC


class Parent(ABC):

    def meth1(self):
        print("meth1")




    @abstractmethod
    def meth2(self):
      #  print("meth2")
         pass


class child(Parent):
    def meth3(self):
        print("child meth3")
    def meth2(self):
        print("child meth2")

c=child()
c.meth2()