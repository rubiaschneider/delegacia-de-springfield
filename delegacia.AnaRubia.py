from enum import Enum

class TipoOcorrencia(Enum):
    DIRECAO_PERIGOSA = 1,
    BARULHO = 2,
    BEBEDEIRA = 3,
    HOMER = 4
    
 
class GravidadeOcorrencia(Enum):
    BAIXA = 1,
    MEDIA = 2,
    ALTA = 3    


class Policial:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.ocorrencias = []
        
    def qtd_ocorrencias(self):
        return len(self.ocorrencias)
    
        
class Ocorrencia:
    
    def __init__(self, tipo: TipoOcorrencia, gravidade: GravidadeOcorrencia = None) -> None:
        self.tipo = tipo
        self.gravidade = GravidadeOcorrencia.ALTA if tipo == TipoOcorrencia.HOMER else \
                         GravidadeOcorrencia.MEDIA if tipo == TipoOcorrencia.DIRECAO_PERIGOSA and gravidade == None else \
                         GravidadeOcorrencia.BAIXA if gravidade == None else gravidade
                         

class Delegacia:
    
    def __init__(self) -> None:
        self.policiais = [Policial('Clancy'), Policial('Eddie'), Policial('Lou')]
        self.chefe = self.policiais[0]
        self.ocorrencias = []
        
    def registrar_ocorrencia(self, ocorrencia: Ocorrencia):
        self.ocorrencias.append(ocorrencia)
        if ocorrencia.tipo == TipoOcorrencia.HOMER:
            self.chefe.ocorrencias.append(ocorrencia)
        else:
            menor_policial = self.policiais[0]
            for p in self.policiais:
               if len(p.ocorrencias) <= len(menor_policial.ocorrencias):
                   menor_policial = p
            menor_policial.ocorrencias.append(ocorrencia)
    
    def get_percentual(self, tipo: TipoOcorrencia) -> float:
        cont = 0
        for oc in self.ocorrencias:
            if oc.tipo == tipo:
                cont += 1
        return cont / len(self.ocorrencias) * 100
        
    def gerar_relatorio(self):
        mapa_ocorrencias = dict((p.nome, len(p.ocorrencias)) for p in self.policiais)
        # mapa_ocorrencias = {
        #     'Clancy': len(self.policiais[0].ocorrencias),
        #     'Eddie': len(self.policiais[1].ocorrencias),
        #     'Lou': len(self.policiais[2].ocorrencias)
        # }
        mapa_percentual = {
            TipoOcorrencia.DIRECAO_PERIGOSA: self.get_percentual(TipoOcorrencia.DIRECAO_PERIGOSA),
            TipoOcorrencia.BARULHO: self.get_percentual(TipoOcorrencia.BARULHO),
            TipoOcorrencia.BEBEDEIRA: self.get_percentual(TipoOcorrencia.BEBEDEIRA),
            TipoOcorrencia.HOMER: self.get_percentual(TipoOcorrencia.HOMER) 
        }
        return mapa_ocorrencias, mapa_percentual

    
def main():
    backend = Delegacia()        
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.HOMER))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.BARULHO, GravidadeOcorrencia.MEDIA))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.BARULHO))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.DIRECAO_PERIGOSA))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.DIRECAO_PERIGOSA, GravidadeOcorrencia.ALTA))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.BEBEDEIRA, GravidadeOcorrencia.ALTA))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.BEBEDEIRA))
    backend.registrar_ocorrencia(Ocorrencia(TipoOcorrencia.HOMER, GravidadeOcorrencia.BAIXA))
    
    mapa_ocorrencias, mapa_percentual = backend.gerar_relatorio()
    for k, v in mapa_ocorrencias.items():
        print(f'{k}: {v} ocorrência(s)')
    for k, v in mapa_percentual.items():
        print(f'{k.name}: {v}%')


if __name__ == '__main__':
    main()