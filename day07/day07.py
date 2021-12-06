if __name__ == "__main__":
    with open('day07/input') as input_file:
        input = [
            line.strip().split() for line in input_file.readlines()
        ]

    first_solution = 0
    second_solution = 0

    print(
        f"""Day 7:
        first solution: {first_solution}
        second solution: {second_solution}"""
    )
