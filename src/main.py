from core.numinator_logic import numinator
from core.define_game_nums import generate_list_for_game
from core.define_game_results import show_game_result
from utils.greetings_msg import greet
from user_io.user_input import user_input


def start():
    print(greet())

    user_num = user_input()
    list_for_game = generate_list_for_game()

    game_result = numinator(list_for_game, user_num)

    print(show_game_result(game_result))


if __name__ == '__main__':
    start()