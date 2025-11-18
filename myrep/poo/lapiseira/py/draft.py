class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self):
        return self.__thickness
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size
    
    def setSize(self, value: int):
        self.__size = value

    def usagePerSheet(self) -> int:
        gasto = {"HB": 1, "2B": 2, "3B":3, "4B":4, "6B":6}
        return gasto[self.__hardness]
    
    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

class Tambor:
    def __init__(self, qtd: int):
        self.__qtd: list[Lead | None] = []
        for i in range (qtd):
            self.__qtd.append(None)
    
    def __str__(self):
        return f"{self.__qtd}"
    
class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip: Lead | None = None
        self.__tambor: list[Lead] = []

    def getTambor(self):
        return self.__tambor
    
    def __str__(self):
        tip_str = "[]" if self.__tip is None else str(self.__tip) 

        tambor_str = "".join(str(lead) for lead in self.__tambor)
        return f"calibre: {self.__thickness}, bico: {tip_str}, tambor: <{tambor_str}>"

    def getLead(self):
        return self.__tip
    
    def setLead(self, value: Lead):
        self.__tip = value

    def insert(self, grafite: Lead):
        if self.__tip is not None:
            print("fail ja existe grafite")
            return
        if grafite.getThickness() != self.__thickness:
            print("fail: calibre incompatível")
            return
        self.__tambor.append(grafite)

    def remove(self):
        if self.__tip == None:
            print("fail: nao existe grafite")
            return
        self.__tip = None
    
    def pull(self):
        if self.__tip is not None:
            print("fail: ja existe grafite no bico")
            return
        if not self.__tambor:
            print("fail: tambor vazio")
            return
        puxou = self.__tambor[0]
        del self.__tambor[0]
        self.__tip = puxou

    def write(self):
        if self.__tip is None:
            print("fail: nao existe grafite no bico")
            return
        
        gasto = self.__tip.usagePerSheet()
        size = self.__tip.getSize()

        if size <= 10:
            print("fail: tamanho insuficiente")
            return
        
        if size - gasto < 10:
            self.__tip.setSize(10)
            print("fail: folha incompleta")
            return
        
        self.__tip.setSize(size - gasto)


def main():
    pencil =  None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(pencil)

        elif args[0] == "init":
            pencil = Pencil(float(args[1]))

        elif args[0] == "insert":
            pencil.insert(Lead(float(args[1]), args[2], int(args[3])))

        elif args[0] == "pull":
            pencil.pull()

        elif args[0] == "remove":
            pencil.remove()

        elif args[0] == "write":
            pencil.write()

        else:
            print("fail: comando invalido")

main()