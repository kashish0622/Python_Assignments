def second_maximum(score):
    single_value = list(set(score))
    single_value.sort()
    runner_up = (score(score.index(max(score)))-1)
    return runner_up