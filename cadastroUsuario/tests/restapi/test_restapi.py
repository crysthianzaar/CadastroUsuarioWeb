from validate_docbr.PIS import PIS
from cadastroUsuario.helpers import ValidateCPF,ValidatePIS
from validate_docbr import CPF,PIS

def test_validador_cpf():
    testCPF = CPF()
    cpf = testCPF.generate(True)
    result = ValidateCPF(cpf)
    assert result == True

def test_validador_pis():
    testPIS = PIS()
    pis = testPIS.generate(True)
    result = ValidatePIS(pis)
    assert result == True
