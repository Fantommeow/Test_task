class NetworkDevice:                  #Базовый класс NetworkDevice, который будет содержать общие свойства и методы для всех сетевых устройств
    def __init__(self, name, ip_address):
        self.name = name              #Название устройства
        self.ip_address = ip_address  #IP-адрес
        self.status = "Inactive"      #Статус устройства

    def power_on(self):                #Включить устройство
        self.status = "Active"
        print(f"Device {self.name} is powered on.")

    def power_off(self):               #Выключить устройство
        self.status = "Inactive"
        print(f"Device {self.name} is powered off.")

    def get_info(self):               #Возвращает информацию о устройстве (имя, IP, статус)
        return f"Device: {self.name}\nIP Address: {self.ip_address}\nStatus: {self.status}"


class Router(NetworkDevice):          #Класс Router, который наследует от NetworkDevice
    def __init__(self, name, ip_address):
        super().__init__(name, ip_address)
        self.routing_table = {}                #Таблица маршрутизации

    def add_route(self, destination, gateway): #Добавляет маршрут в таблицу
        self.routing_table[destination] = gateway
        print(f"Route added: {destination} -> {gateway}")

    def remove_route(self, destination):       #Удаляет маршрут из таблицы
        if destination in self.routing_table:
            del self.routing_table[destination]
            print(f"Route removed: {destination}")
        else:
            print(f"Route {destination} not found.")

    def get_info(self):                  #Переопределяет метод базового класса, добавляя информацию о таблице маршрутизации
        info = super().get_info()
        info += f"\nRouting Table: {self.routing_table}"
        return info


class Switch(NetworkDevice):             #Класс Switch, который наследует от NetworkDevice
    def __init__(self, name, ip_address):
        super().__init__(name, ip_address)
        self.vlan = None                 #VLAN, к которому принадлежит коммутатор

    def create_vlan(self, vlan_id):      #Cоздает VLAN
        self.vlan = vlan_id
        print(f"VLAN {vlan_id} created.")

    def delete_vlan(self):               #Удаляет VLAN
        if self.vlan is not None:
            self.vlan = None
            print(f"VLAN deleted.")
        else:
            print(f"No VLAN to delete.")

    def get_info(self):                  #Переопределяет метод базового класса, добавляя информацию о VLAN
        info = super().get_info()
        if self.vlan is not None:
            info += f"\nVLAN: {self.vlan}"
        return info


# Тестирование
router1 = Router("Router1", "192.168.1.1")
router1.power_on()
router1.add_route("192.168.2.0", "192.168.1.254")
print(router1.get_info())

switch1 = Switch("Switch1", "192.168.1.2")
switch1.power_on()
switch1.create_vlan(10)
print(switch1.get_info())

router1.power_off()
router1.remove_route("192.168.2.0")
print(router1.get_info())

