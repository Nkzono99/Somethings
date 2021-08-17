"""TD(λ)法で最小コストを求める.
A -> Fへの最小コスト

40000      *---*---*---*
           |   |   |   |
32000      *---*---*---*
           |   |   |   |
24000      *---*---*---*
           |   |   |   |
16000      *---*---*---*
           |   |   |   |
 8000      *---*---*---*
           |   |   |   |
    0  *---*   *   *   *---*
       A   B   C   D   E   F

t=0 A0 -> B0 -> B?
t=1 B? -> C? -> C?
t=2 C? -> D? -> D?
t=3 D? -> E? -> E0
(t=4 E0 -> F0)
"""
import numpy as np

np.set_printoptions(precision=2, floatmode='fixed')

costs = np.array([
    [0, 4000, 4800, 5520, 6160, 6720],
    [800, 1600, 2680, 4000, 4720, 6080],
    [320, 480, 800, 2240, 3120, 4640],
    [0, 160, 320, 560, 1600, 3040],
    [0, 0, 80, 240, 480, 1600],
    [0, 0, 0, 0, 160, 240],
])

altitudes = [0, 8000, 16000, 24000, 32000, 40000]

nt = 5  # A0 => B => C => D => E0

s = [
    [0],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [0],
]

"""行動価値関数Q(s, x) (= Q[*(t, alt), alt])"""
Q = np.zeros((nt, len(altitudes), len(altitudes)))


def calc_delta(t, from_alt, to_alt, gamma=1.0):
    if from_alt == to_alt:
        cost = costs[from_alt, from_alt]
    else:
        cost = costs[from_alt, from_alt] + costs[from_alt, to_alt]
    return cost + gamma * Q[t+1, to_alt, s[t+1]].max() - Q[t, from_alt, to_alt]


# def greedy_search(t, from_alt, gamma):
#     to_alt = s[t+1][0]
#     min_delta: float = np.inf

#     for alt in s[t+1]:
#         delta = calc_delta(t, from_alt, alt, gamma)
#         print(t, alt, delta, min_delta)
#         if delta < min_delta:
#             to_alt = alt
#             min_delta = delta

#     return to_alt, min_delta


def greedy_search(t, from_alt, gamma):
    to_alt = s[t+1][0]
    min_q: float = np.inf

    for alt in s[t+1]:
        # q = Q[t, from_alt, alt]
        q = calc_delta(t, from_alt, alt, gamma)
        if q < min_q:
            to_alt = alt
            min_q = q

    delta = calc_delta(t, from_alt, to_alt, gamma)
    return to_alt, delta


def q(nstep=100, alpha=0.5, gamma=1.0):
    for k in range(nstep):
        cur_alt = 0
        for t in range(nt-1):
            to_alt, delta = greedy_search(t, cur_alt, gamma)
            # print(f'{t}: {altitudes[cur_alt]} -> {altitudes[to_alt]} = {delta}')

            Q[t, cur_alt, to_alt] += alpha * delta

            cur_alt = to_alt

        print('==' * 6, f'Q k={k} t={t}', '==' * 6)
        print(Q[0, 0, :])


q(100)

