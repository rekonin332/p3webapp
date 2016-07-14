class Base(object):
  def __init__(self):
    print("Base init")


class Medium1(Base):
    def __init__(self):
        super().__init__()

        print("Medium1 init")


class Medium2(Base):
  def __init__(self):
    super().__init__()

    print("Medium2 init")


class Leaf(Medium1, Medium2):
  def __init__(self):
    super().__init__()

    print ("Leaf init")


l = Leaf()
print(Leaf.mro())


