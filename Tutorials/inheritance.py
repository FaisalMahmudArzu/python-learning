class A:

    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B: #It means class B is a child class of A, it will inherit everything from A

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        print("In C init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feat()
# b1 = B()
# c1 = C()

# a1.feature1()
# a1.feature2()

# b1.feature3()
# b1.feature1()

# c1.feature5()
# c1.feature4()