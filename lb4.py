
from itertools import combinations


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

items = [
    Item("r", 3, 25),  # Винтовка
    Item("p", 2, 15),  # Пистолет
    Item("a", 2, 15),  # Боекомплект
    Item("m", 2, 20),  # Аптечка
    Item("i", 1, 5),   # Ингалятор
    Item("k", 1, 15),  # Нож
    Item("x", 3, 20),  # Топор
    Item("t", 1, 25),  # Оберег
    Item("f", 1, 15),  # Фляжка
    Item("d", 1, 10),  # Антидот
    Item("s", 2, 20),  # Еда
    Item("c", 2, 20)   # Арбалет
]

CAPACITY = 8
START_POINTS = 20


def calculate_score(selected):
    score = START_POINTS

    for item in items:
        if item in selected:
            score += item.value
        else:
            score -= item.value

    return score


def calculate_weight(selected):
    return sum(item.weight for item in selected)


def print_inventory(selected):
    cells = []

    for item in selected:
        cells.extend([item.name] * item.weight)

    cells.extend(["-"] * (CAPACITY - len(cells)))

    for i in range(0, CAPACITY, 4):
        print(" ".join(f"[{cell}]" for cell in cells[i:i + 4]))


def main():
    valid_combinations = []
    for count in range(1, len(items) + 1):
        for combination in combinations(items, count):

            weight = calculate_weight(combination)

            if weight > CAPACITY:
                continue

            if not any(item.name == "i" for item in combination):
                continue

            score = calculate_score(combination)

            if score > 0:
                valid_combinations.append(
                    (score, weight, combination)
                )

    if not valid_combinations:
        print("Подходящих комбинаций нет.")
        return

    valid_combinations.sort(
        key=lambda x: x[0],
        reverse=True
    )

    best_score, best_weight, best_items = valid_combinations[0]

    print("ЛУЧШИЙ ВАРИАНТ:")
    print_inventory(best_items)
    print("Итоговые очки выживания:", best_score)
    print("Занято ячеек:", best_weight)

    print("\nВСЕ ПОДХОДЯЩИЕ КОМБИНАЦИИ:")

    for number, (score, weight, combination) in enumerate(
        valid_combinations, 1
    ):
        names = [item.name for item in combination]

        print(
            f"{number}. {names} | "
            f"Ячеек: {weight} | Очки: {score}"
        )

    print("\nВсего комбинаций:", len(valid_combinations))
