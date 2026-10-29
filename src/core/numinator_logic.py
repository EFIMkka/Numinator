def numinator(mas: list[int], num: int) -> int | None:
    low_cap = 0
    high_cap = len(mas) - 1

    while low_cap <= high_cap:
        mid = (low_cap + high_cap) // 2
        guess = mas[mid]

        print(f'I think, that your number is: {guess}')

        user_judge = int(input('Is Numinator right?\n'))

        match user_judge:
            case 1:
                return guess
            case 2:
                low_cap = mid + 1
            case 3:
                high_cap = mid - 1

    return None