from chamador import Chamador
from elevador import Elevador

e = Elevador()
c0 = Chamador(e, 0)
c1 = Chamador(e, 1)
c2 = Chamador(e, 2)
c3 = Chamador(e, 3)

c0.enviar_chamado("cima")
c2.enviar_chamado("baixo")
c2.enviar_chamado("baixo")
c1.enviar_chamado("baixo")
c3.enviar_chamado("baixo")