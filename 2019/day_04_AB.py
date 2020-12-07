# https://adventofcode.com/2019/day/4


def is_valid_1(pwd):
    return (
        len(pwd) == 6
        and all(pwd[i - 1] <= pwd[i] for i in range(1, len(pwd)))
        and any(pwd[i - 1] == pwd[i] for i in range(1, len(pwd)))
    )


def is_valid_2(pwd):
    pwd_deco = "_" + pwd + "_"
    return (
        len(pwd) == 6
        and all(pwd[i - 1] <= pwd[i] for i in range(1, len(pwd)))
        and any(
            pwd_deco[i - 2] != pwd_deco[i]
            and pwd_deco[i - 1] == pwd_deco[i]
            and pwd_deco[i + 1] != pwd_deco[i]
            for i in range(2, len(pwd_deco))
        )
    )


pwd_from = 246540
pwd_to = 787419

# Part One
nb_ok = sum(is_valid_1(str(i)) for i in range(pwd_from, pwd_to))
print(f"Part One: {nb_ok}")


# Part Two
nb_ok = sum(is_valid_2(str(i)) for i in range(pwd_from, pwd_to))
print(f"Part Two: {nb_ok}")
