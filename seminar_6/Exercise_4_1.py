def pazzle(pazzle_str:str, answer: list,  counter: int):
    print(pazzle_str)
    temp_counter = 1
    answer = list(map(lambda x: x.lower(), answer))
    while temp_counter <= counter:
        use_answer = input(f'{pazzle_str}: ').lower()
        if use_answer in answer:
            return temp_counter
        temp_counter += 1
    return 0
