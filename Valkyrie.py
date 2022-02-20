# Beautiful is better than ugly
# 一个有关女武神信息的类
class Valkyrie:
    def __init__(self, name, fight):
        self.name = name
        self.fight = fight


def do_housework():
    print("B级女武神只能做打杂的工作")


class ValkyrieB(Valkyrie):
    def __init__(self, name, fight):
        super().__init__(name, fight)

    do_housework()


class ValkyrieA(Valkyrie):
    def __init__(self, name, fight):
        super().__init__(name, fight)
