class Verificadores:
    def verifica_bool(txt):
        while True:
            label = input(txt).strip().lower()

            if not label in 'sn' or not label:
                continue
            else:
                label = label[0]

            if label == 's':
                return True
            
            return False

