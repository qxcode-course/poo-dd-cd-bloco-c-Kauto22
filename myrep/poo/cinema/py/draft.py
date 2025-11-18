class Client():
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getId(self):
        return self.__id
    def getPhone(self):
        return self.__phone
    def setId(self, value:int):
        self.__id = value
    def setPhone(self, value:int):
        self.__phone = value
    
    def __str__(self):
        return (f'{self.__id}:{self.__phone}')
        
class Theater():
    def __init__(self, capacity: int):
        self.__capacity: list[Client | None] = []
        for i in range (capacity):
            self.__capacity.append(None)    

    def getCapacity(self):
        return self.__capacity

    def __str__(self):
        if len(self.__capacity) == 0:
            return "[]"
        capacity = " ".join(['-' if x is None else str(x) for x in self.__capacity])
        return f"[{capacity}]"
    
    def verifyIndex(self, index: int) -> bool:
        if index < 0 or index >= len(self.__capacity):
            return False
        return True

    def search(self, name: str) -> int:
        for i in range(len(self.__capacity)):
            if self.__capacity[i] != None and self.__capacity[i].getId() == name:
                return i
            return -1

    def reserve(self, id: str, phone: int, index: int) -> bool:
        if not self.verifyIndex(index):
            print("fail: cadeira nao existe")
            return False
        if self.search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return False
        if self.__capacity[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        
        self.__capacity[index] = Client(id, phone)
    
    def cancel(self, name: str) -> bool:
        index = self.search(name)

        if index == -1:
            print("fail: cliente nao esta no cinema")
            return False
        
        self.__capacity[index] = None
        return
        
    

def main():
    theater = Theater(0)

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(theater)

        elif args[0] == "init":
            theater = Theater(int(args[1]))
        
        elif args[0] == "reserve":
            theater.reserve(str(args[1]), int(args[2]), int(args[3]))
        
        elif args[0] == "cancel":
            theater.cancel(args[1])

        elif args[0] == "search":
            theater.search(str(args[1]))
        else:
            print("fail: comando invalido")

main()