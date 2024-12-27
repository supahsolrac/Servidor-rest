import obj
import cherrypy
from crud import Personagens

def main():

    desp= cherrypy.dispatch.RoutesDispatcher()

    f= Personagens()

    desp.connect(name='criar', route='/recurso',controller=f,action='inserir', conditions=dict(method=['POST']))
    desp.connect(name='buscar', route='/recurso',controller=f,action='buscar', conditions=dict(method=['GET']))
    desp.connect(name='atualizar', route='/recurso',controller=f,action='atualizar', conditions=dict(method=['PATCH']))
    desp.connect(name='deletar', route='/recurso',controller=f,action='deletar', conditions=dict(method=['DELETE']))
    desp.connect(name='atualizarclasses', route='/recurso/classes',controller=f,action='attclass', conditions=dict(method=['PATCH']))
    conf={'/':{'request.dispatch':desp}}
    cherrypy.tree.mount(root= None, config= conf)
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
    

if __name__ == "__main__":
    main()
