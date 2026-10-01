import urllib
import urllib.request

try:
    site = urllib.request.urlopen('wix68zGi5mXAxV-JrkGHUJcC1kQy_kOegoIAggACAAIBxAC&opi=89978449&cd&psig=AOvVaw2mGLgsY_uKKc609EEDCOd2&ust=1790953424328000')
except:
    print("O site pudim NÃO esta acecivel no momento.")
else:
    print("Consegui acessar o site pudim com sucesso!")
