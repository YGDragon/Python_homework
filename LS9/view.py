from emoji import emojize
from colorama import init
from colorama import Fore, Style, Back
init()


def begin():
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + Style.BRIGHT \
          + emojize(':star: НАЧАЛО ИГРЫ :star:') + Style.RESET_ALL)


def message_bot(step: int, user: str, bot: str):
    print(Style.BRIGHT + Fore.LIGHTRED_EX + f'Ход №{step} -> {user}: {bot}' + Style.RESET_ALL)


def message_user(step: int, user: str):
    print(Style.BRIGHT + Fore.BLUE + f'Ход №{step} -> {user}: ' + Style.RESET_ALL, end='')


def message1(res: int):
    print(f'Осталось конфет {res}')


def message2(user: dict, u: int, emojis=None):
    text = user[1] if u == 2 else user[2]
    print(Style.BRIGHT + emojize(f'Победил {text} :thumbs_up:'))
    print(Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX + 'КОНЕЦ ИГРЫ' + Style.RESET_ALL)
