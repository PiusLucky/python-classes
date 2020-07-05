# method override - Two(2) classes scenario
class parent:
    def method1(self):
        print('Iam a Viking, a Legend meant to be in Valhalla')


class child1(parent):
    def method1(self):
        print('Iam Bjorn, the first child of Ragnar Lothbrok')
        super().method1() # Add method1 from the super-class[parent] to child1's method1


child1_obj = child1()
child1_obj.method1()

# Output:
# Iam Bjorn, the first child of Ragnar Lothbrok
# Iam a Viking, a Legend meant to be in Valhalla



# method override - Three(3) classes scenario
class parent:
    def method1(self):
        print('Iam a Viking, a Legend meant to be in Valhalla')


class child1(parent):
    def method1(self):
        print('Iam Bjorn, the first child of Ragnar Lothbrok')
        super().method1() # Add method1 from the super-class[parent] to child1's method1


class child2(child1):
    def method1(self):
        print('Iam Ivar the Boneless, you must have heard of me!')
        super().method1() # Add method1 from the super-class[child1] to child2's method1


child2_object = child2()
child2_object.method1()
# Output:
# Iam Ivar the Boneless, you must have heard of me!
# Iam Bjorn, the first child of Ragnar Lothbrok
# Iam a Viking, a Legend meant to be in Valhalla