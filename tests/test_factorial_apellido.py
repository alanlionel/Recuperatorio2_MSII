from funciones.factorial_apellido import factorial_apellido

def test_factorial_apellido():
    assert factorial_apellido(5) == 120
    assert factorial_apellido(-3) is None
