def second_maximum(score):
    single_value = list(set(score))
    single_value.sort()
    runner_up = single_value[-2]
    return runner_up