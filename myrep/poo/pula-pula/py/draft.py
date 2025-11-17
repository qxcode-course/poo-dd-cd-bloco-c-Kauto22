class Kid():
    def __init__(self, nome: str, age: int):
        self.__nome = nome
        self.__age = age

    def getNome(self):
        return self.__nome
    def getAge(self):
        return self.__age
    
    def __str__(self):
        return f"{self.__nome}:{self.__age}"
    
class Trampoline():
    def __init__(self):
        self.__waiting: list[Kid] = []
        self.__trampolineUser: list[Kid] = []

    def __str__(self):
        waiting = ", ".join(str(x) for x in reversed(self.__waiting))
        trampolineUser = ", ".join(str(x) for x in reversed(self.__trampolineUser))
        
        return f"[{waiting}] => [{trampolineUser}]"
        
    def arrive(self, kid: Kid):
        self.__waiting.append(kid)
    
    def enter(self):
        if len(self.__waiting) == 0:
            return
            
        kid = self.__waiting[0]
        del self.__waiting[0]
        self.__trampolineUser.append(kid)

    def leave(self):
        if len(self.__trampolineUser) == 0:
            return
        
        kid = self.__trampolineUser[0]
        del self.__trampolineUser[0]
        self.__waiting.append(kid)
    
    def remove(self, name: str):
        for i in range(len(self.__waiting)):
            if self.__waiting[i].getNome() == name:
                del self.__waiting[i]
                return
            
        for i in range(len(self.__trampolineUser)):
            if self.__trampolineUser[i].getNome() == name:
                del self.__trampolineUser[i]
                return
            
        print(f"fail: {name} nao esta no pula-pula")


        
def main():
    trampoline = Trampoline()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        
        elif args[0] == "show":
            print(trampoline)

        elif args[0] == "arrive":
            kid = Kid(args[1], int(args[2]))
            trampoline.arrive(kid)
        
        elif args[0] == "enter":
            trampoline.enter()

        elif args[0] == "leave":
            trampoline.leave()

        elif args[0] == "remove":
            trampoline.remove(args[1])







main()