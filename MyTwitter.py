
#Precisamos utilizar o método "atualizar" para atualiza as informações do perfil
#Classes que faltam finalizar:
    # - seguidores, seguidos, numero de seguidores, tweetar
#Todas as classes precisam de ajustes e revisões 
#Precisamos adicionar os argumentos exigidos nas exceções

class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
    
    def criar_perfil(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is not None:
            raise PEException()
        self.__repositorio.cadastrar(perfil)

    def cancelar_perfil(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else:
            perfil.set_ativo(False)

    def tweetar(self, usuario, mensagem):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None or perfil.is_ativo() == False:
            raise PIException()
        elif len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException() 
        else:
            #Tem alguma coisa faltando aqui e errada
            perfil.add_tweet(mensagem)

    def timeline(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None: 
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else: 
            perfil.get_timeline()

    def tweets(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else:
            perfil.get_tweets()

    def seguir(self, usuario_seguido, usuario_seguidor):
        perfil_seguido = self.__repositorio.buscar(usuario_seguido)
        perfil_seguidor = self.__repositorio.buscar(usuario_seguidor)

        if perfil_seguido is None or perfil_seguidor is None:
            raise PIException()
        elif perfil_seguido.is_ativo() == False or perfil_seguidor.is_ativo() == False:
            raise PDException()
        else:
            perfil_seguido.add_seguidor(perfil_seguidor)
            perfil_seguidor.add_seguidos(perfil_seguido)


    def numero_seguidores(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else:
            #Precisamos de:
                # - um for para verificar por seguidor se ele existe e é ativo
                # - uma variável count para contabilizar o n° de seguidores 

    def seguidores(self):
        perfil = self.__repositorio.buscar()

        if perfil is None: 
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else:
            #Aqui falta levar em consideração somente os perfis_seguidores
            #que estiverem ativos
            perfil.__seguidores()

    def seguidos(self):
        perfil = self.__repositorio.buscar()
        
        if perfil is None: 
            raise PIException()
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException()
        else:
            #Aqui falta levar em consideração somente os perfis_seguidores
            #que estiverem ativos
            perfil.__seguidos()