class Robot:

    def __init__(self,name):
        self.name = name
        print("robot {name} is created now".format(name=name))


    def left(self):
        print("{name} turning left".format(name=self.name))

    def right(self):
        print("{name} turning right".format(name=self.name))

    def forward(self):
        print("{name} going forward".format(name=self.name))

    def backward(self):
        print("{name} going backward".format(name=self.name))

    def stop(self):
        print("{name} stopped".format(name=self.name))

    def rotate_360(self):
        print("{name} rotating 360".format(name=self.name))
