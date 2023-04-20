import random

def guess(x):
    rand_number = random.randint(1, x)
    guess = 0
    while guess != rand_number:
        guess = int(input(f"Escolha um número entre 1 e {x}: "))
        if guess < rand_number:
            print("Tente novamente, número muito baixo.")
        elif guess > rand_number:
            print("Tente novamente, número muito alto.")
    print(f"Parabéns, você acertou! O número era {rand_number}")

guess(10)