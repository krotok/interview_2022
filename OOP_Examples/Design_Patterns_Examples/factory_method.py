#Это такй сложныи; оператор IF, который созфают объекты класса в соответствии с импутом пришедшим в метод
#1. Работать с Кром или Мозила в данном тесте
#2. Создавать разные нагрузки в разных тестах
class Transport:
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Deliver by land"

class Ship(Transport):
    def deliver(self):
        return "Deliver by sea"

def transport_factory(type):
    if type == "truck":
        return Truck()
    elif type == "ship":
        return Ship()

t = transport_factory("ship")
print(t.deliver())  # Deliver by sea
