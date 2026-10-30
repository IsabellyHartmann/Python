products = []

def add_product(nome, preco,iva):
    product = {
        'product': nome,
        'price': preco,
        'tax': iva
    }
    products.append(product)

    dicionario = {"product": product, "price": preco, "tax": iva}

def update_final_price(produto):