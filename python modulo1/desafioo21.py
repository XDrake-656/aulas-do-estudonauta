import os
import winsound

input("Pressione ENTER para tocar Megalovania...")

# Localiza a pasta do seu arquivo de código
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(pasta_atual, "megalovania.wav")

print("Tentando tocar diretamente pela placa de som do Windows...")

try:
    # O parâmetro SND_FILENAME diz que é um arquivo.
    # O Python entrega o áudio direto para o driver do Windows.
    winsound.PlaySound(caminho_musica, winsound.SND_FILENAME)
    print("Música finalizada!")

except Exception as e:
    print(f"Erro inesperado: {e}")

input("Pressione ENTER para fechar o programa.")
