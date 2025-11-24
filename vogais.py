print("contar vogal")
palavra = input("digite uma palavra: ")
texto = "aeiouáéíóúàèìòùâêîôûãõ"
total = 0
for letra in palavra.lower():
    if letra in texto:
        total += 1
if total > 1:
    print(f"Sua palavra tem {total} vogais")
    
elif total == 1:
    print(f"Sua palavra tem {total} vogal")
    
else:
    print("Sua palavra nao tem vogais")
    
