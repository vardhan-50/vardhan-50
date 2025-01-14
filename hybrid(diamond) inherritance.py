class Human:
    def work(self):
        print("humans will work")
class Dad(Human):
    def drive(self):
        print("dad will drive")
class Mother(Human):
    def cook(self):
        print("mother will cook")
class Child(Dad,Mother):
    def play(self):
        print("children will play")
c=Child()
c.work()
c.drive()
c.cook()
c.play()