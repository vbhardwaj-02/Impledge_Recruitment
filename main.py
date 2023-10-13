import time


def is_compound_word(word, word_set):
    if word in word_set:
        return True
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set and is_compound_word(suffix, word_set):
            return True
    return False


def find_longest_and_second_longest_compound_words(filename):
    try:
        with open(filename, 'r') as file:
            word_list = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None, None

    if not word_list:
        print(f"File '{filename}' is empty.")
        return None, None, None

    start_time = time.time()

    word_set = set(word_list)
    word_list.sort(key=len, reverse=True)

    longest_word = ""
    second_longest_word = ""

    for word in word_list:
        word_set.remove(word)
        if is_compound_word(word, word_set):
            if not longest_word:
                longest_word = word
            elif not second_longest_word:
                second_longest_word = word
                break
        word_set.add(word)

    end_time = time.time()

    return longest_word, second_longest_word, end_time - start_time


# Example usage
file_path = 'Input_02.txt'
longest_compound, second_longest_compound, processing_time = find_longest_and_second_longest_compound_words(file_path)

if longest_compound:
    print("Longest compound word:", longest_compound)
if second_longest_compound:
    print("Second longest compound word:", second_longest_compound)
if processing_time:
    print("Processing time:", processing_time, "seconds")
