import random


def get_card():
    return random.randint(2, 11)


def BlackJack():
    player = [get_card(), get_card()]
    dealer = [get_card()]

    player_sum = sum(player)
    dealer_sum = dealer[0]

    print(f"Ваши карты: {player} (Сумма: {player_sum})")
    print(f"Карта дилера: {dealer[0]}")

    while player_sum <= 21:
        action = input("Взять карту (да) или остановиться (стоп)? ").lower()
        if action == 'да':
            new_card = get_card()
            player.append(new_card)
            player_sum += new_card
            print(f"Новая карта: {new_card} | Сумма: {player_sum}")
        elif action == 'стоп':
            break
        else:
            print("Неправильный ввод")

    if player_sum > 21:
        print("Перебор! Вы проиграли")
        return

    dealer.append(get_card())
    dealer_sum = sum(dealer)
    print(f"\nДилер открывает карты: {dealer} (Сумма: {dealer_sum})")

    while dealer_sum < 17:
        new_card = get_card()
        dealer.append(new_card)
        dealer_sum += new_card
        print(f"Дилер берет карту: {new_card} | Сумма: {dealer_sum}")


    print("\nРезультаты:")
    print(f"Ваша сумма: {player_sum} | Сумма дилера: {dealer_sum}")

    if dealer_sum > 21:
        print("Дилер перебрал! Вы выиграли!")
    elif player_sum > dealer_sum:
        print("Вы выиграли!")
    elif player_sum < dealer_sum:
        print("Дилер выиграл!")
    else:
        print("Ничья!")

BlackJack()