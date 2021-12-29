from validate_docbr import CPF, PIS

def ValidateCPF(cpf: str) -> bool:

    cpfVerificador = CPF()
    cpf_me = cpf
    cpfVerificador.mask(cpf_me)
    
    resultValidate = cpfVerificador.validate(cpf_me)
    return resultValidate

def ValidatePIS(pis: str) -> bool:
    pisVerificador = PIS()
    pis_me = pis
    pisVerificador.mask(pis_me)
    
    resultValidate = pisVerificador.validate(pis_me)
    return resultValidate