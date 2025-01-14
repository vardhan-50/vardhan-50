class Laptop:
    def __init__(self,l_namae,l_model,l_cost):
        self.l_name=l_namae
        self.l_model=l_model
        self.l_cost=l_cost
    def laptop_details(self):
        print(self.l_name)
        print(self.l_model)
        print(self.l_cost)
l1=Laptop('acer','aspire3',20000)
l1.laptop_details()
l2=Laptop('dell','inspiron15',40000)
print(l2.l_name)
print(l2.l_model)
print(l2.l_cost)
