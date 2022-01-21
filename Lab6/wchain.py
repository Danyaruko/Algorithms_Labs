
def find_max_wchain(vocabulary):
    vocabulary.sort(key=len)
    word_wchain_idx_map = {word: 1 for word in vocabulary}
    for word in vocabulary:
        for i in range(len(word)):
            new_word = word[:i]+word[i+1:]
            if new_word in vocabulary:
                word_wchain_idx_map[word] = max(
                    word_wchain_idx_map[word], 1 + word_wchain_idx_map[new_word])
    return max(word_wchain_idx_map.values())


if __name__ == "__main__":
    input_file = open("wchain.in", "r")
    number_of_words = int(input_file.readline())
    vocabulary = input_file.read().splitlines()
    input_file.close()

    output_file = open("wchain.out", "w")
    output_file.write(
        str(find_max_wchain(vocabulary)))
