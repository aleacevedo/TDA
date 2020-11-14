import sys
from password_checker import MultiChecker

USER_INFO_KEYS = ['username', 'nombre', 'apellido']


def __main__():
    if len(sys.argv) == 0:
        print("Argumentos insuficientes.\nIndique username nombre apellido y password.")
        return -1

    userInfo = dict(zip(USER_INFO_KEYS, sys.argv[1:-1]))
    password = sys.argv[-1]

    MultiChecker(userInfo, password).result()


__main__()
