
class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
    
    def criar_perfil(self, usuario):
        perfil = self.buscar(usuario)
        if perfil is not None:
            raise PEException()
        self.__repositorio.cadastrar(perfil)

    def cancelar_perfil(self, usuario):
        perfil = self.buscar(usuario)
        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.ativo() == False:
            raise PDException()
        else:
            perfil.set_ativo(False)

    def tweetar(self, usuario, mensagem):
        perfil = self.buscar(usuario)
        if perfil is None or perfil.ativo() == False:
            raise PIException()
        elif len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException() 
        else:
            #Tem alguma coisa faltando aqui e errada
            perfil.add_tweet(mensagem)

    def timeline(self):
        pass

    def tweets(self, usuario):
        perfil = self.buscar(usuario)
        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.ativo() == False:
            raise PDException()
        else:
            perfil.get_tweets()

    def seguir(self):
        pass

    def numero_seguidores(self, usuario):
        perfil = self.buscar(usuario)
        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.ativo() == False:
            raise PDException()
        else:
            ##terminamos depois
            continue
    def seguidores(self):
        pass

    def seguidos(self):
        pass