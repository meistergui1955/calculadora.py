def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return None
    return x / y

print("=== Calculadora Simples ===")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

while True:
    escolha = input("\nDigite a sua escolha (1/2/3/4): ").strip()

    # Bloco principal de verificação da opção
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Digite apenas números válidos!")
            continue

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            if resultado is None:
                print("Erro: Não é possível dividir por zero!")
            else:
                print(f"Resultado: {num1} / {num2} = {resultado}")

        # Pergunta de continuidade (dentro do 'if' principal)
        proxima = input("\nDeseja fazer outra conta? (s/n): ").strip().lower()
        if proxima != 's':
            print("Encerrando a calculadora...")
            break
