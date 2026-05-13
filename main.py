class Company:
    def __init__(self, company_name, workers):
        self.company_name = company_name
        self.__workers = workers

    def get_workers(self):
        return self.__workers

    def set_workers(self, new_workers):
        self.__workers = new_workers


c1 = Company('Google', 150000)

print(c1.company_name)
print(c1.get_workers())

c1.set_workers(200000)

print(c1.get_workers())
