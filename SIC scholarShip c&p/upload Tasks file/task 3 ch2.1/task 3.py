

def find_shortest_words():
    words = []
    for i in range(5):
        word = input(f"Enter word {i+1} of 5: ")
        words.append(word)

    if not words:
        print("No words entered.")
        return

    min_length = float('inf')
    for word in words:
        if len(word) < min_length:
            min_length = len(word)

    shortest_words = []
    for word in words:
        if len(word) == min_length:
            shortest_words.append(word)

    print(f"The shortest word(s) is/are: {', '.join(shortest_words)}")


if __name__ == "__main__":
    find_shortest_words()

#### task 2 ####


def count_frequencies(input_list):
    frequency_dict = {}
    for item in input_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    return frequency_dict


if __name__ == "__main__":
    list = [1, 1, 5, 5, 3, 1, 3, 1, 4, 4, 2, 2, 2]
    frequencies = count_frequencies(example_list)
    print(f"Example input list: {example_list}")
    print(f"Example output: {frequencies}")