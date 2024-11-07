class Bird:
    def __init__(self):
        print("Bird is Ready")

    def Who(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

class Peginum(Bird):
    def __init__(self):
        super().__init__()
        print("Yowai Mo")

    def Who(self):
        print("Peginum")

    def run(self):
        print("Run")

bird = Bird()
bird.Who()
bird.swim()


peginum = Peginum()
peginum.Who()
peginum.swim()
peginum.run()
