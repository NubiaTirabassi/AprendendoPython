'''
Finalidade: Sistema para Cálculo de Custo de Viagem e Preço de Frete
Autor: Núbia G. dos Santos Tirabassi.
Data: 03-04-2023
'''

#função distancia
def calculaDistancia(tempo, velocidade):
    distancia = tempo*velocidade
    return (distancia)

#função gasto combustivel
def calculaCombustivel (distancia, rendimento):
    litrosGastos = distancia/rendimento
    return(litrosGastos)

#função gerar relatório
def gerarRelatorio(velocidadeMedia, tempo, distancia, combustivel, rendimento, precoLitro, custoTotal):
    print()
    print("Relatorio de custo de viagem")
    print()
    print("tempo de viagem:", tempo)
    print("velocidadeMedia: ", velocidadeMedia)
    print("Distancia Percorrida: ", distancia)
    print("Quantidade combustivel gasto: ", combustivel)
    print("Rendimento do veiculo: ", rendimento)
    print("Preço litro do combustivel: ", precoLitro)
    print("Custo total da viagem:", custoTotal)
    print("Margem de lucro:", custoTotal * 0.3)

    print("Fim do relatório")
    return ()

def custoViagem(litrosCombustivel, valorLitro):
    custoTotal = litrosCombustivel*valorLitro
    return(custoTotal)

#programa principal

print("sistema para calculo de  custo de viagem")

velocidadeMedia = float(input("digite a velocidade  media:"))
tempo = float(input("digite o tempo da viagem:"))
rendimentoVeiculo = float(input("Rendimento do veiculo:"))
precoLitro = float(input("preço litro do combustivel:"))

distanciaPercorrida = calculaDistancia(tempo, velocidadeMedia)
gastoCombustivel = calculaCombustivel(distanciaPercorrida, rendimentoVeiculo)
custoTotal = custoViagem(gastoCombustivel, precoLitro)
gerarRelatorio(velocidadeMedia, tempo, distanciaPercorrida, gastoCombustivel, rendimentoVeiculo,precoLitro, custoTotal)

