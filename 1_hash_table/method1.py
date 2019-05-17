
pile = [1, 2, 3, 3, 2, 1]
pile_length = len(pile)

if __name__ == '__main__':
    pairs = []

    while len(pile) > 0:
        print(f"{pile}")
        # pop first one from the pile, and the pile is getting shorter.
        sock = pile.pop(0)
        print(f"sock: {sock}")

        # look for its match in the pile one by one
        for j in range(len(pile)):
            another = pile[j]
            # if found the same sock, pick it and make a pair
            if sock == another:
                popped_another = pile.pop(j)
                pair = (sock, popped_another)
                pairs.append(pair)
                print(f"[Found] sock: {sock}, another: {another}")
                break
            else:
                print(f"[Not Found] sock: {sock}, another: {another}")

    print(pairs)
    # the number of pairs should be equal to half the pile.
    assert(len(pairs) == (pile_length/2))
