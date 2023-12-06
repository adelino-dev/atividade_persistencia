def cadastrar_usuario(informacoes):
  arquivo = open("formulario.txt", 'a', encoding='utf-8')
  arquivo.write(informacoes)
  arquivo.close()


def ler_usuarios():

  arquivo = open("formulario.txt", 'r', encoding='utf-8')
  usuarios = arquivo.read().split("\n")

  print("\nUSUÁRIOS CADASTRADOS:\n")
  for usuario in usuarios[0:-1]:
    nome, idade, sexo, telefone = usuario.split("|")
    if sexo == "M":
      sexo = "Masculino"
    else:
      sexo = "Feminino"

    print("Nome:", nome)
    print("Sexo", sexo)
    print("Idade:", idade)
    print("Telefone", telefone + "\n")

  arquivo.close()


def main():
  while True:
    nome = input("Nome:")
    if nome == '0':
      break
    idade = input("Idade:")
    sexo = input("Sexo (M ou F):")
    telefone = input("Telefone:")
    informacoes = nome + '|' + idade + "|" + sexo + "|" + telefone + "\n"
    cadastrar_usuario(informacoes)

  ler_usuarios()


if __name__ == "__main__":
  main()
