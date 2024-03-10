import random

def vhadai_chyslo():
    print("Ласкаво просимо до гри 'Вгадай число'!")
    print("Я загадав число від 1 до 100. Спробуй вгадати його!")

    tayemne_chyslo = random.randint(1, 100)
    spriyannya = 0

    while True:
        vhid = int(input("Введіть свою догадку: "))

        spriyannya += 1

        if vhid < tayemne_chyslo:
            print("Моє число більше.")
        elif vhid > tayemne_chyslo:
            print("Моє число менше.")
        else:
            print(f"Вітаю! Ти вгадав число {tayemne_chyslo} за {spriyannya} спроб!")
            break

if __name__ == "__main__":
    vhadai_chyslo()
