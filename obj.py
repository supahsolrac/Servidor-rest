class chara:

    def __init__(self,nome,cls,nivel,exp,vida,vidamax):
        self.nome=nome
        self.cls=classes()
        self.cls.add(cls)
        self.nivel=nivel
        self.exp=exp
        self.vida=vida
        self.vidamax=vidamax

    def att(self,nivel,exp,vida,vidamax):
        self.nivel=nivel
        self.exp=exp
        self.vida=vida
        self.vidamax=vidamax

    def addclass(self,cls):
        return self.cls.add(cls)

    def removeclass(self,cls):
        return self.cls.remove(cls)

class classes:

    def __init__(self):
        self.cls=[]

    def add(self,cls):
        if (self.cls.count(cls) == 1):
            pass
        else:
            self.cls.append(cls)
        return 0

    def remove(self,cls):
        for i in range(len(self.cls)):
            if (self.cls[i]==cls):
                self.cls.pop(i)
                return 0
        return -1
        