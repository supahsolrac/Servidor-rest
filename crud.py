from obj import chara
import Pyro5
import cherrypy

@cherrypy.expose
class Personagens(object):

    def __init__(self):
        self.pers=[]

    def inserir(self,**args):
        if('nome' in args.keys() and 'classe' in args.keys() and 'nivel' in args.keys() and 'exp' in args.keys() and 'vida' in args.keys() and 'vidamax' in args.keys()):
            nome= args['nome']
            classe= args['classe']
            nivel= int(args['nivel'])
            exp= int(args['exp'])
            vida= int(args['vida'])
            vidamax= int(args['vidamax'])
            if(nivel>0 and (exp>=0 and exp<10) and vida>=0 and vidamax>=vida):
                cherrypy.response.status="201"
                persona=chara(nome,classe,nivel,exp,vida,vidamax)
                for i in range(len(self.pers)):
                    if (self.pers[i].nome==nome):
                        raise cherrypy.HTTPError(400,"O personagem ja existe")
                self.pers.append(persona)
            else:
                raise cherrypy.HTTPError(400,"Valor de um ou mais parâmetros invalidos")

        else:
            raise cherrypy.HTTPError(400,"Parâmetro(s) não informados")
    @cherrypy.tools.json_out()    
    def buscar(self,**args):
        if('nome' in args.keys()):
            nome= args['nome']
            x=-1
            for i in range(len(self.pers)):
                if (self.pers[i].nome==nome):
                    x=i
                    break
            if(x==-1):
                raise cherrypy.HTTPError(404,"Personagem não encontrado")
            else:
                persona=self.pers[x]
                return {'nome': persona.nome,
                        'classes': persona.cls.cls,
                        'nivel': persona.nivel,
                        'exp': persona.exp,
                        'vida': persona.vida,
                        'vidamax': persona.vidamax
                        }

        else:
            raise cherrypy.HTTPError(400,"Parâmetro(s) não informados")


    def atualizar(self,**args):
        if('nome' in args.keys() and 'nivel' in args.keys() and 'exp' in args.keys() and 'vida' in args.keys() and 'vidamax' in args.keys()):
            nome= args['nome']
            nivel= int(args['nivel'])
            exp= int(args['exp'])
            vida= int(args['vida'])
            vidamax= int(args['vidamax'])
            if(nivel>0 and (exp>=0 and exp<10) and vida>=0 and vidamax>=vida):
                cherrypy.response.status="200"
                for i in range(len(self.pers)):
                    if (self.pers[i].nome==nome):
                        self.pers[i].att(nivel,exp,vida,vidamax)
                        return
                raise cherrypy.HTTPError(404,"O personagem não existe")
            else:
                raise cherrypy.HTTPError(400,"Valor de um ou mais parâmetros invalidos")

        else:
            raise cherrypy.HTTPError(400,"Parâmetro(s) não informados")

    def attclass(self,**args):
        if('op' in args.keys() and 'nome' in args.keys() and 'cls' in args.keys()):
            op= args['op']
            nome= args['nome']
            cls= args['cls']
            if(op=='a'):
                for i in range(len(self.pers)):
                    if (self.pers[i].nome==nome):
                        self.pers[i].addclass(cls)
                        return
                raise cherrypy.HTTPError(404,"O personagem não existe")
            elif(op=='d'):
                for i in range(len(self.pers)):
                    if (self.pers[i].nome==nome):
                        if(self.pers[i].removeclass(cls)==-1):
                            raise cherrypy.HTTPError(404,"O personagem não possui esta classe")
                        return 
                raise cherrypy.HTTPError(404,"O personagem não existe")
            else:
                raise cherrypy.HTTPError(400,"Operação invalida")   
        else:
            raise cherrypy.HTTPError(400,"Parâmetro(s) não informados")

    def deletar(self,**args):
        if('nome' in args.keys()):
            nome= args['nome']
            for i in range(len(self.pers)):
                if (self.pers[i].nome==nome):
                    self.pers.pop(i)
                    return
            raise cherrypy.HTTPError(404,"O personagem não existe")
        else:
            raise cherrypy.HTTPError(400,"Parâmetro(s) não informados")
        


