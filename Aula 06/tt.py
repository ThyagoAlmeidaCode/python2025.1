def inverter_palavra(palavra):
  """Inverte uma dada palavra.

  Args:
    palavra: A palavra a ser invertida (string).

  Returns:
    A palavra invertida (string).
  """
  palavra_invertida = palavra[::-1]
  return palavra_invertida

# Pede ao usuário para digitar uma palavra
palavra_original = input("Digite uma palavra: ")

# Chama a função para inverter a palavra
palavra_invertida = inverter_palavra(palavra_original)

# Exibe a palavra original e a invertida
print(f"Palavra original: {palavra_original}")
print(f"Palavra invertida: {palavra_invertida}")