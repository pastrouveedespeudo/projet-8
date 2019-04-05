"""here we test"""

import mes_aliments.mes_aliments_user  as script

def test_controle_data_aliment():
    """test control data"""

    parameter = 'tete'
    out = ('nombre de produit suppérieur a 6', False)
    assert script.controle_data_aliment(parameter) == out
