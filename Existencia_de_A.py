
class StringConta:
    def __init__(self):
        None
    def contar_a(self,string):
        string = string.lower()
        count = string.count('a')
        if count == 0:
            return f"A letra 'a' existe na string."
        return f"A letra 'a' aparece {count} vezes na string."

# Exemplo de uso
stringConta=StringConta()
texto = input("Informe um texto: ")
if texto == "" : texto = "Um exemplo de string de A e a b B h r t i h aa aaa ."
resultado = stringConta.contar_a(texto)
print(resultado)
