from collections import Counter


def MassVote(N: int, Votes: list[int]) -> str:

    percent_vote = sum(Votes)
    max_vote = [0, 0, 0]
    counter_vote = Counter(Votes)

    for candidate, vote in enumerate(Votes):
        if vote > max_vote[1] and counter_vote[vote] == 1:
            max_vote[0], max_vote[1], max_vote[1] = candidate + 1, round((Votes[candidate] / percent_vote) * 100, 2), vote

    if max_vote[1] > 50:
        return f"majority winner {max_vote[0]}"
    elif 0 < max_vote[1] <= 50:
        return f"minority winner {max_vote[0]}"
    elif max_vote[1] == 0:
        return "no winner"

