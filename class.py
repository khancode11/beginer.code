class Persion:
    name = "Persion"
    def __init__(self, name):
        self.name = name
jeffrey = Persion("Jeffrey")
print("%s name is %s" % (Persion.name, jeffrey.name))