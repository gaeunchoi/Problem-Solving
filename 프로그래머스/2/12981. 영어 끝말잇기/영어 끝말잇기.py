def solution(n, words):
    word_relay = [words[0]]

    for idx in range(1, len(words)):
        prev_word = word_relay[-1]
        curr_word = words[idx]

        if curr_word in word_relay or prev_word[-1] != curr_word[0] or len(curr_word) == 1:
            return [(idx % n) + 1, (idx // n) + 1]

        word_relay.append(curr_word)
    return [0, 0]