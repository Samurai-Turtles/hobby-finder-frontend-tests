# Este arquivo é só para um template de tests

import pytest

@pytest.fixture
def ambiente_necessario_para_rodar():
    return (
        1, 2, 3, 4, 5, 6
    )

class TestCriaUsuario:

    def test_cria_usuario_test(self, ambiente_necessario_para_rodar):
        n_1, n_2, n_3, n_4, n_5, n_6 = ambiente_necessario_para_rodar
        assert n_1 == 1
        assert n_2 == 2
        assert n_3 == 3
        assert n_4 == 4
        assert n_5 == 5
        assert n_6 == 6