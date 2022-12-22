pizzas = ['пеперонни', 'сырная', 'гавайская']
friend_pizzas = pizzas[:]
pizzas.append('четыре сыра')
friend_pizzas.append('яблочный пирог')
for pizza in pizzas:
    print(f'Моя любимая пицца это: {pizza}')
for friend_piz in friend_pizzas:
    print(f'Любимая пицца моих друзей это: {friend_piz}')
