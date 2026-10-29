def show_game_result(res: int | None) -> str:
    if isinstance(res, int):
        return f'I won! Your number is: {res}'
    else:
        return 'Hey, it is unfair playing! I mentioned correct number, but you lied to me! >:('