def main():
    while True:
        try:
            S = int(input())
            A = int(input())
            B = int(input())

            if (S >= 1 and S <= 36) and (A >= 1 and A <= 10000) and (B >= 1 and B <= 10000) and A <= B:
                soma = 0
                for i in range(A, (1 + B)):
                    if i == S:
                        soma += 1
                    num = str(i)
                    lista_de_digitos = list(map(int, num.strip()))
                    somatorio = sum(lista_de_digitos)
                    if somatorio == S:
                        soma += 1
                print(soma)
                break
            else:
                raise Exception
        except Exception:
            print("Valores digitados não atendem as restrições.")
            break

if __name__ == "__main__":
    main()