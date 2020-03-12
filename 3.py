class Disk():

    def __init__(self, name, x, y, height, width):

        self.name = name

        self.x = x

        self.y = y

        self.height = height

        self.width = width



    def showdisk(self):

        pu()

        goto(self.x, self.y)

        pd()

        fillcolor("blue")

        begin_fill()

        fd(self.width / 2)

        lt(90)

        fd(self.height)

        lt(90)

        fd(self.width)

        lt(90)

        fd(self.height)

        lt(90)

        fd(self.width / 2)

        end_fill()



    def newpos(self, x, y):

        self.cleardisk()

        self.x = x

        self.y = y

        self.showdisk()



    def cleardisk(self):

        pu()

        goto(self.x, self.y)

        pd()

        pencolor("white")

        fillcolor("white")

        begin_fill()

        fd(self.width / 2)

        lt(90)

        fd(self.height)

        lt(90)

        fd(self.width)

        lt(90)

        fd(self.height)

        lt(90)

        fd(self.width / 2)

        end_fill()


        