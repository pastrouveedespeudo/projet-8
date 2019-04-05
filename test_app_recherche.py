"""test functions"""

import mes_aliments.algo_open  as script


def test_image():
    """we test function image"""

    parameter = 'Chocolat au lait'
    out = [('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/304/692/004/5711/front_fr.17.400.jpg', 'crêpes dentelle au chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait')]
    assert script.image_aliment(parameter) == out
    
def test_image2():
    """we test image fucntion with maj"""

    parameter = 'chocolat au lait'
    out = [('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait'), ('https://static.openfoodfacts.org/images/products/304/692/004/5711/front_fr.17.400.jpg', 'crêpes dentelle au chocolat au lait'), ('https://static.openfoodfacts.org/images/products/301/776/082/6174/front_fr.5.400.jpg', 'chocolat au lait')]
    assert script.image_aliment(parameter) == out

def test_titre_aliment():
    """we test title function"""

    parameter = 'chocolat au lait'
    out = [('chocolat au lait',), ('chocolat au lait',), ('crêpes dentelle au chocolat au lait',), ('chocolat au lait',)]
    assert script.titre_aliment(parameter) == out


    
def test_detail_aliment():
    """we test details function"""

    parameter = 'https://static.openfoodfacts.org/images/products/327/016/089/7087/front_fr.12.400.jpg'
    out = [(22, '15 Mini Quiches', '3270160897087', 'Farine de _blé_ (_gluten_), _beurre_ (_lait_) 12,3 %, _lait_ demi-écrémé épaissi (_lait_, amidon transformé de maïs), _œuf_ frais liquide pasteurisé 9,5 %, _crème_ liquide (_lait_) 6,5 %, eau, _fromage_ de chèvre (lait) 5,3%, oignon préfrit (oignon 4,5%, huile dolive, sel, acidifiant : acide citrique), compotée doignon au vinaigre de Xérès 4,7 % [oignon, eau, beurre (_lait_), sucre, caramel, vinaigre de vin de Xérès (contient conservateur : _anhydride sulfureux_), amidon transformé de maïs], emmental râpé (Danemark, Allemagne ; lait) 2,9%, lardon cuit fumé 2,3 % [poitrine de porc (France), eau, sel, dextrose de blé, acidifiant : acétate de sodium, antioxydant : érythorbate de sodium, conservateur : nitrite de sodium], _saumon_ cuit (_poissons_) 2 %, _bleu_ (_lait_) 1,8%, tomate 1,8 %, _fromage_ frais (_lait_), poireau 1,3 %, chair de _saumon_ fumé (_poissons_) 1,1 %, tomate semi-déshydratée 0,6 %, épinard, préparation au basilic 0,5 % (huile de colza, basilic, huile dolive vierge extra, _fromage_ (_lait_), ail, sel), basilic, _parmesan_ (_lait_), pignon de pin], sel, _moutarde_ à lancienne [vinaigre dalcool, graine de _moutarde_, eau, sel, acidifiant : acide citrique, épices (dont _céleri_)], fibre de _blé_ (_gluten_), jus de citron, ail, persil, agent de traitement de la farine : L-cystéine, thym, poivre noir, muscade.', 'd', 'https://static.openfoodfacts.org/images/products/327/016/089/7087/front_fr.12.400.jpg', 'Picard', 'Picard', 3), (62, '15 Mini Quiches', '3270160897087', 'Farine de _blé_ (_gluten_), _beurre_ (_lait_) 12,3 %, _lait_ demi-écrémé épaissi (_lait_, amidon transformé de maïs), _œuf_ frais liquide pasteurisé 9,5 %, _crème_ liquide (_lait_) 6,5 %, eau, _fromage_ de chèvre (lait) 5,3%, oignon préfrit (oignon 4,5%, huile dolive, sel, acidifiant : acide citrique), compotée doignon au vinaigre de Xérès 4,7 % [oignon, eau, beurre (_lait_), sucre, caramel, vinaigre de vin de Xérès (contient conservateur : _anhydride sulfureux_), amidon transformé de maïs], emmental râpé (Danemark, Allemagne ; lait) 2,9%, lardon cuit fumé 2,3 % [poitrine de porc (France), eau, sel, dextrose de blé, acidifiant : acétate de sodium, antioxydant : érythorbate de sodium, conservateur : nitrite de sodium], _saumon_ cuit (_poissons_) 2 %, _bleu_ (_lait_) 1,8%, tomate 1,8 %, _fromage_ frais (_lait_), poireau 1,3 %, chair de _saumon_ fumé (_poissons_) 1,1 %, tomate semi-déshydratée 0,6 %, épinard, préparation au basilic 0,5 % (huile de colza, basilic, huile dolive vierge extra, _fromage_ (_lait_), ail, sel), basilic, _parmesan_ (_lait_), pignon de pin], sel, _moutarde_ à lancienne [vinaigre dalcool, graine de _moutarde_, eau, sel, acidifiant : acide citrique, épices (dont _céleri_)], fibre de _blé_ (_gluten_), jus de citron, ail, persil, agent de traitement de la farine : L-cystéine, thym, poivre noir, muscade.', 'd', 'https://static.openfoodfacts.org/images/products/327/016/089/7087/front_fr.12.400.jpg', 'Picard', 'Picard', 3), (115, '15 Mini Quiches', '3270160897087', 'Farine de _blé_ (_gluten_), _beurre_ (_lait_) 12,3 %, _lait_ demi-écrémé épaissi (_lait_, amidon transformé de maïs), _œuf_ frais liquide pasteurisé 9,5 %, _crème_ liquide (_lait_) 6,5 %, eau, _fromage_ de chèvre (lait) 5,3%, oignon préfrit (oignon 4,5%, huile dolive, sel, acidifiant : acide citrique), compotée doignon au vinaigre de Xérès 4,7 % [oignon, eau, beurre (_lait_), sucre, caramel, vinaigre de vin de Xérès (contient conservateur : _anhydride sulfureux_), amidon transformé de maïs], emmental râpé (Danemark, Allemagne ; lait) 2,9%, lardon cuit fumé 2,3 % [poitrine de porc (France), eau, sel, dextrose de blé, acidifiant : acétate de sodium, antioxydant : érythorbate de sodium, conservateur : nitrite de sodium], _saumon_ cuit (_poissons_) 2 %, _bleu_ (_lait_) 1,8%, tomate 1,8 %, _fromage_ frais (_lait_), poireau 1,3 %, chair de _saumon_ fumé (_poissons_) 1,1 %, tomate semi-déshydratée 0,6 %, épinard, préparation au basilic 0,5 % (huile de colza, basilic, huile dolive vierge extra, _fromage_ (_lait_), ail, sel), basilic, _parmesan_ (_lait_), pignon de pin], sel, _moutarde_ à lancienne [vinaigre dalcool, graine de _moutarde_, eau, sel, acidifiant : acide citrique, épices (dont _céleri_)], fibre de _blé_ (_gluten_), jus de citron, ail, persil, agent de traitement de la farine : L-cystéine, thym, poivre noir, muscade.', 'd', 'https://static.openfoodfacts.org/images/products/327/016/089/7087/front_fr.12.400.jpg', 'Picard', 'Picard', 3)]
    assert script.food_details(parameter) == out



def test_verification_remplacement():
    """we test verification function"""

    sortie = False
    assert script.verification_remplacement('tete', 'chocolat au lait') == out














