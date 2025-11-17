class Cliente():
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return self.__nome
    
class Market():
    def __init__(self, numCounters: int):
        self.__counters: list[Cliente | None] = []
        for _ in range (numCounters):
            self.__counters.append(None)
        self.__waiting: list[Cliente] = []


    def arrive(self, cliente: Cliente):
        self.__waiting.append(cliente)

    def call(self, index: int):
        if index < 0 or index >= len(self.__counters):
            print("indice inexistente")
            return
        
        if self.__counters[index] is not None:
            print("fail: caixa ocupado")
            return
        
        if len(self.__waiting) == 0:
            print("fail: sem clientes")
            return
        
        self.__counters[index] = self.__waiting[0]
        del self.__waiting[0]

    def finish(self, index: int) -> Cliente | None:
        if index < 0 or index >= len(self.__counters):
            print("fail: caixa inexistente")
            return
        if self.__counters[index] == None:
            print("fail: caixa vazio")
            return
        self.__counters[index] = None
            

    def __str__(self):
        counters = ", ".join(["-----" if x is None else str(x) for x in self.__counters])
        waiting = ", ".join([str(x) for x in self.__waiting])
        return f"Caixas: [{counters}]\nEspera: [{waiting}]"
        


def main():
    budega = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            budega = Market(int(args[1]))

        elif args[0] == "show":
            print(budega)

        elif args[0] == "arrive":
            pessoa = (args[1])
            budega.arrive(pessoa)
        
        elif args[0] == "call":
            budega.call(int(args[1]))

        elif args[0] == "finish":
            budega.finish(int(args[1]))
        
        else:
            print("fail: comando invalido")


main()
       