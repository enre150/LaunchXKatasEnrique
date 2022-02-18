def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("no se encuentra el archivo config.txt !")
    except IsADirectoryError:
        print("el  config.txt se encontro pero es un directorio, no se puede leet")
    except (BlockingIOError, TimeoutError):
        print("sistema de archivos bajo mucha carga, no se puede leer archivo")
if __name__ == '__main__':
    main()