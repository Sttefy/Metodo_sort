
numeros_favoritos = [
    ["Fernando", ("28", "36", "15")],
    ["Juan", ("68", "12", "90")],
    ["Matha", ("52", "46", "4")]
]


for nombre, numeros in numeros_favoritos:
    numeros = list(numeros)
    numeros.sort()
    print(f"{nombre}'s números favoritos ordenados:", ", ".join(numeros))
