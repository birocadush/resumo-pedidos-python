pedidos = [
    {"cliente": "Ana", "valor": 120.50, "status": "pago"},
    {"cliente": "Bruno", "valor": 75.00, "status": "pendente"},
    {"cliente": "Carla", "valor": 200.00, "status": "pago"},
    {"cliente": "Daniel", "valor": 50.00, "status": "pendente"},
]

def resumo_pedidos(pedidos):
    pago = 0
    pendente = 0
    total = 0
    diferenca = 0

    for pedido in pedidos:
        if pedido["status"] == "pago":
            pago += 1
            total += pedido["valor"]

        else:
            pendente += 1
            diferenca += pedido["valor"]

    return pago, pendente, total, diferenca
pago, pendente, total, diferenca = resumo_pedidos(pedidos)

print("pedidos pagos:", pago)
print("pedidos pendentes:", pendente)
print("total pago: R$", total)
print("total pendente: R$", diferenca)
