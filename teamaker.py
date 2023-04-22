import pandas as pd
import numpy as np
import itertools
import random

# Fetching teams from the csv files
left_team = pd.read_csv('left_gang.csv')
right_team = pd.read_csv('right_gang.csv')

# Dividing groups
t1 = left_team.iloc[:2].reset_index(drop=True)
t2 = right_team.iloc[:2].reset_index(drop=True)
m1 = left_team.iloc[2:4].reset_index(drop=True)
m2 = right_team.iloc[2:4].reset_index(drop=True)
l1 = left_team.iloc[4:6].reset_index(drop=True)
l2 = right_team.iloc[4:6].reset_index(drop=True)
b1 = left_team.iloc[6:].reset_index(drop=True)
b2 = right_team.iloc[6:].reset_index(drop=True)

# left gang
t1m1 = pd.concat([t1, m1], axis=0, ignore_index=True)
t1l1 = pd.concat([t1, l1], axis=0, ignore_index=True)
m1l1 = pd.concat([m1, l1], axis=0, ignore_index=True)

# right gang
t2m2 = pd.concat([t2, m2], axis=0, ignore_index=True)
t2l2 = pd.concat([t2, l2], axis=0, ignore_index=True)
m2l2 = pd.concat([m2, l2], axis=0, ignore_index=True)

# definig name to random generated combos of team


def randomTeams(dfs, combo):
    data = []
    for i in combo:
        df = dfs.iloc[list(i)]
        data.append(df)
    return data


def team_maker(team_type=None):

    # left gang combos
    combo_1_1 = list(itertools.combinations(t1m1.index, 1))
    combo_1_2 = list(itertools.combinations(t1l1.index, 1))
    combo_1_3 = list(itertools.combinations(m1l1.index, 1))

    # left gang combos
    combo_2_1 = list(itertools.combinations(t2m2.index, 1))
    combo_2_2 = list(itertools.combinations(t2l2.index, 1))
    combo_2_3 = list(itertools.combinations(m2l2.index, 1))

    # left gang bowler combos
    bowler_1_1 = list(itertools.combinations(b1.index, 1))
    bowler_1_2 = list(itertools.combinations(b1.index, 2))
    bowler_1_3 = list(itertools.combinations(b1.index, 3))
    bowler_1_4 = list(itertools.combinations(b1.index, 4))

    # right gang bowler combos
    bowler_2_1 = list(itertools.combinations(b2.index, 1))
    bowler_2_2 = list(itertools.combinations(b2.index, 2))
    bowler_2_3 = list(itertools.combinations(b2.index, 3))
    bowler_2_4 = list(itertools.combinations(b2.index, 4))

    # left gang team names genrated by the function
    teams = [
        randomTeams(t1m1,  combo_1_1),
        randomTeams(t1l1,  combo_1_2),
        randomTeams(m1l1,  combo_1_3),
    ]

    # right gang team names genrated by the function
    teams2 = [
        randomTeams(t2m2,  combo_2_1),
        randomTeams(t2l2,  combo_2_2),
        randomTeams(m2l2,  combo_2_3),
    ]

    # left gang team bowler names genrated by the function
    bowler_1 = [
        randomTeams(b1, bowler_1_1),
        randomTeams(b1, bowler_1_2),
        randomTeams(b1, bowler_1_3),
        randomTeams(b1, bowler_1_4),
    ]

    # right gang team bowler names genrated by the function
    bowler_2 = [
        randomTeams(b2, bowler_2_1),
        randomTeams(b2, bowler_2_2),
        randomTeams(b2, bowler_2_3),
        randomTeams(b2, bowler_2_4),
    ]

    # 1-4
    bowler_combo_1 = []
    # 2-3
    bowler_combo_2 = []
    # 3-2
    bowler_combo_3 = []
    # 4-1
    bowler_combo_4 = []

    # making all random bowler combos and appending them to the lists
    for i in bowler_1[0]:
        for j in bowler_2[3]:
            temp = pd.concat([i, j], ignore_index=True)
            bowler_combo_1.append(temp)

    for i in bowler_1[1]:
        for j in bowler_2[2]:
            temp = pd.concat([i, j], ignore_index=True)
            bowler_combo_2.append(temp)

    for i in bowler_1[2]:
        for j in bowler_2[1]:
            temp = pd.concat([i, j], ignore_index=True)
            bowler_combo_3.append(temp)

    for i in bowler_1[3]:
        for j in bowler_2[0]:
            temp = pd.concat([i, j], ignore_index=True)
            bowler_combo_4.append(temp)

    # suffling the lists

    for i in range(50):
        random.shuffle(bowler_combo_1)
        random.shuffle(bowler_combo_2)
        random.shuffle(bowler_combo_3)
        random.shuffle(bowler_combo_4)

    t1t2_bowlers = bowler_combo_1[:2]+bowler_combo_2[:6] + \
        bowler_combo_3[:6] + bowler_combo_4[:2]

    t1m2_bowlers = bowler_combo_1[2:4]+bowler_combo_2[6:12] + \
        bowler_combo_3[6:12] + bowler_combo_4[2:4]

    t1l2_bowlers = bowler_combo_1[4:6]+bowler_combo_2[12:18] + \
        bowler_combo_3[12:18] + bowler_combo_4[4:6]

    m1t2_bowlers = bowler_combo_1[6:8]+bowler_combo_2[18:24] + \
        bowler_combo_3[18:24] + bowler_combo_4[6:8]

    m1m2_bowlers = bowler_combo_1[8:10]+bowler_combo_2[24:30] + \
        bowler_combo_3[24:30] + bowler_combo_4[8:10]

    m1l2_bowlers = bowler_combo_1[10:12]+bowler_combo_2[30:36] + \
        bowler_combo_3[30:36] + bowler_combo_4[10:12]

    l1t2_bowlers = bowler_combo_1[12:14]+bowler_combo_2[36:42] + \
        bowler_combo_3[36:42] + bowler_combo_4[12:14]

    l1m2_bowlers = bowler_combo_1[14:16]+bowler_combo_2[42:48] + \
        bowler_combo_3[42:48] + bowler_combo_4[14:16]

    l1l2_bowlers = bowler_combo_1[16:18]+bowler_combo_2[48:54] + \
        bowler_combo_3[48:54] + bowler_combo_4[16:18]

    for i in range(50):
        random.shuffle(t1t2_bowlers)
        random.shuffle(t1m2_bowlers)
        random.shuffle(t1l2_bowlers)

        random.shuffle(m1t2_bowlers)
        random.shuffle(m1m2_bowlers)
        random.shuffle(m1l2_bowlers)

        random.shuffle(l1t2_bowlers)
        random.shuffle(l1m2_bowlers)
        random.shuffle(l1l2_bowlers)

    if team_type == "t1t2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[2]:
            temp = pd.concat([t1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[2]:
            temp = pd.concat([t2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, t1t2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "t1m2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[2]:
            temp = pd.concat([t1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[1]:
            temp = pd.concat([m2, i], ignore_index=True)
            team_2_combo.append(temp)
        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, t1m2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "t1l2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[2]:
            temp = pd.concat([t1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[0]:
            temp = pd.concat([l2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, t1l2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "m1t2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[1]:
            temp = pd.concat([m1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[2]:
            temp = pd.concat([t2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, m1t2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "m1m2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[1]:
            temp = pd.concat([m1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[1]:
            temp = pd.concat([m2, i], ignore_index=True)
            team_2_combo.append(temp)
        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, m1m2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "m1l2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[1]:
            temp = pd.concat([m1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[0]:
            temp = pd.concat([l2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, m1l2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "l1t2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[0]:
            temp = pd.concat([l1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[2]:
            temp = pd.concat([t2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, l1t2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "l1m2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[0]:
            temp = pd.concat([l1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[1]:
            temp = pd.concat([m2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, l1m2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)

    if team_type == "l1l2":
        team_1_combo = []
        team_2_combo = []
        for i in teams[0]:
            temp = pd.concat([l1, i], ignore_index=True)
            team_1_combo.append(temp)
        for i in teams2[0]:
            temp = pd.concat([l2, i], ignore_index=True)
            team_2_combo.append(temp)

        n = 0
        final_team = []
        for i in team_1_combo:
            for j in team_2_combo:
                temp = pd.concat([i, j, l1l2_bowlers[n]], ignore_index=True)
                final_team.append(temp)
                n += 1

        return pd.concat(final_team, axis=1)


team = ["t1t2", "t1m2", "t1l2",
        "m1t2", "m1m2", "m1l2",
        "l1t2", "l1m2", "l1l2",]


for i in range(len(team)):
    team_maker(team[i]).to_csv(
        f"teams/{team[i]}.csv", index=False, header=False)
