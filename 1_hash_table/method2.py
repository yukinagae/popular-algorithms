
pile = [1, 2, 3, 3, 2, 1]
pile_length = len(pile)

if __name__ == '__main__':

    pair_hash = {}

    while len(pile) > 0:
        print(f"{pile}")
        # pop first one from the pile, and the pile is getting shorter.
        sock = pile.pop(0)
        print(f"sock: {sock}")

        if sock in pair_hash:
            another = pair_hash[sock][0]
            pair_hash[sock] = (another, sock)
            print(f"[Matched sock] sock: {sock}, another: {another}")
        else:
            pair_hash[sock] = (sock, )
            print(f"[New sock] sock: {sock}")

    print(pair_hash)

    pairs = list(pair_hash.values())

    print(pairs)
    # the number of pairs should be equal to half the pile.
    assert(len(pairs) == (pile_length/2))
