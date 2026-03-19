# Principais métodos do tipo texto

nome = "Gabriel"
sobrenome = "Casemiro"
nome_completo = "Gabriel Casemiro"

print(nome)
print(sobrenome)
print(nome_completo)

print(nome.upper())

print(nome.lower())

print(nome[0])

print(nome_completo.count())
print(nome_completo.count("a"))

print(nome_completo.find("a"))
print(nome.find("a"))

print(nome.encode())

print(nome.encode().decode())

print(nome_completo.replace("b", "a"))
print(nome_completo.replace("a", "123"))

telefone = "(19)97325-0502"
print(telefone)
print(telefone.replace("(", ""))
print(telefone)
print(telefone.replace(")", ""))
print(telefone)
print(telefone.replace("-", ""))
print(telefone)

telefone = "(19)97325-0502"
print(telefone.replace("(", "").replace(")", "").replace("-", ""))

print("-".join("Gabriel"))

print(nome_completo.split(" "))
print(nome_completo.split())

nome = "xGabriel Casemirox"
print(nome.strip("x"))
print(nome.strip("a"))

print(nome.rstrip("x"))

print(nome_completo.startswith("Ga"))
print(nome_completo.startswith("Be"))

print("el" in nome_completo)
print("abc" in nome_completo)
print("abc" not in nome_completo)