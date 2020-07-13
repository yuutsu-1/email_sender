from msvcrt import getch
import getpass
import sys


def pyssword(prompt='Senha: '):
    if sys.stdin is not sys.__stdin__:  # Se mensagem promptada não a mesma inicial (echoada)
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        while True:
            key = ord(getch())
            if key == 13:
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8:
                if len(pwd) > 0:
                    sys.stdout.write('\b' + ' ' + '\b')
                    sys.stdout.flush()
                    pwd = pwd[:-1]
            else:
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()
                pwd = pwd + char
