def password_():
    import random

    def get_cipher():
        num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        numbers = list(range(3, 21))
        cipher = random.choice(numbers)
        return cipher

    def get_password(n):
        passcode = {}
        passcode.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
        passcode.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
        passcode.update({14: 1611325212343114105968, 15: 1214114232133124115106978, 16: 1317115262143531341251161079})
        passcode.update({17: 11621531441351261171089, 18: 12151811724272163631545414513612711810})
        passcode.update({19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
        password = passcode.get(n)
        return password

    n = get_cipher
    print('Шифр:', n)

    pair_of_numbers1 = list(range(1, n))
    pair_of_numbers2 = list(range(1, n))
    pairs = []
    result = ''

    for i in pair_of_numbers1:
        for j in pair_of_numbers2:
            pair_of_numbers1 = i
            pair_of_numbers2 = j
            if pair_of_numbers1 >= pair_of_numbers2:
                continue
            else:
                multiple = n%(pair_of_numbers1 + pair_of_numbers2)
                if multiple == 0:
                    pairs.append([pair_of_numbers1, pair_of_numbers2])
                    result = result + str(pair_of_numbers1) + str(pair_of_numbers2)
    print('Пары чисел', *pairs)
    print('Введите пароль', result, 'во вторую вставку')
    if int(result) == get_password(n):
        print('Шифр найден')

