from documento_fiscal import DocumentoFiscal

class ValidaCNPJ(DocumentoFiscal):
    def __init__(self):
        self._NUM_DV1 = list(range(5, 1, -1)) + list(range(9, 1, -1))
        # DV1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 3, 2]
        self._NUM_DV2 = list(range(6, 1, -1)) + list(range(9, 1, -1))
        #DV2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 3, 2]

    def calcula_digito_verificador(self, validaCNPJ, digito = 1):
        pesos = self._NUM_DV1 if digito == 1 else self._NUM_DV2
        resultado = sum(int(digito) * peso for digito,peso in zip(validaCNPJ, pesos)) % 11
        return 0 if resultado < 2 else 11 - resultado

validando = ValidaCNPJ()

print(validando.valido('80.248.466/0001'))



