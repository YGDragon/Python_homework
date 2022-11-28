from random import randint
import model
import view
# алгоритм - задача Баше
user = {1: 'BOT',
        2: 'USER'}
all_candies = 220
low_candy, high_candy = [1, 28]
step = 1
move = 0
u_gamer = 0
rand = randint(1, 2)
gamer = [rand, 1 if rand == 2 else 2]
view.begin()
while move < all_candies:
    for u in gamer:
        if u == 1:
            if step == 1:
                bot = all_candies % (low_candy + high_candy)
            elif step == 2:
                bot = (all_candies - u_gamer) % (low_candy + high_candy)
            else:
                bot = (low_candy + high_candy - u_gamer)
            move += bot
            view.message_bot(
                step, user[1], bot
            )
        elif u == 2:
            view.message_user(step, user[u])
            user_data = model.check(input())
            u_gamer = model.min_max(
                user_data, low_candy, high_candy
            )
            move += u_gamer
        step += 1
        remainder = all_candies - move
        view.message1(remainder)
        if remainder <= high_candy:
            view.message2(user, u)
            move = all_candies
            break
