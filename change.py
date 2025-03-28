def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("Vuelto")
    print("Pesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    print(pesos)
    print("Decimal:")
    decimal = vuelto - pesos
    decimal_entero = int(decimal * 100)
    print(decimal_entero)

change()
