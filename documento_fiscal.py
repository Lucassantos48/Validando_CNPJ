
class DocumentoFiscal:

    def __init__(self):
        self._NUM_DV1 =[]
        self._NUM_DV2 = []

    def calcula_digito_verificador(self, documento, digito=1):
        pass

    def valido (self, documento):

        documento = documento.replace('.','').replace('/', '').replace('-', '')

        if(not documento.isnumeric()):
            return False

        digitos = None

        if(len(documento) == 14):
           digitos = documento[:12]
        else:
            return "CNPJ do emitente inválido."

        dv1 = self.calcula_digito_verificador(digitos, 1)
        dv2 = self.calcula_digito_verificador(digitos + str(dv1), 2)

        return documento == digitos + str(dv1) + str(dv2)

    def invalido (self, documento):

        documento = documento.replace('.','').replace('/', '').replace('-', '')

        if(not documento.isnumeric()):
            return False

        digitos = None

        if(len(documento) == 00000000000000 ):
           digitos = documento[:12]
        else:
            return "CNPJ do emitente inválido."

        dv1 = self.calcula_digito_verificador(digitos, 1)
        dv2 = self.calcula_digito_verificador(digitos + str(dv1), 2)

        return documento == digitos + str(dv1) + str(dv2)

