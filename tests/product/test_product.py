from inventory_report.inventory.product import Product


def test_cria_produto():
    create_product = Product(
        1,
        "Borracha",
        "Papelaria Solar",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "Ao abrigo de luz solar",
    )
    assert create_product.id == 1
    assert create_product.nome_do_produto == "Borracha"
    assert create_product.nome_da_empresa == "Papelaria Solar"
    assert create_product.data_de_fabricacao == "2021-07-04"
    assert create_product.data_de_validade == "2029-02-09"
    assert create_product.numero_de_serie == "FR48"
    assert (
        create_product.instrucoes_de_armazenamento == "Ao abrigo de luz solar"
    )


# informações retirada do readme.
