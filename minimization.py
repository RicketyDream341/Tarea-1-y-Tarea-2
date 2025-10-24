def dfa_minimization():
    
    c = int(input().strip())
    dfas = []
    for _ in range(c):
        n = int(input().strip())
        alphabet = input().strip().split()
        finals = set(map(int, input().strip().split()))
        transitions = {}
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            state = row[0]
            transitions[state] = {symbol: row[i + 1] for i, symbol in enumerate(alphabet)}
        dfas.append((n, alphabet, finals, transitions))
    return dfas


def all_pairs(n):
    
    pairs = []
    for p in range(n):
        for q in range(p + 1, n):
            pairs.append((p, q))
    return pairs


def minimize_dfa(n, alphabet, finals, transitions):
    
    table = {}
    for p, q in all_pairs(n):
        table[(p, q)] = (p in finals) != (q in finals)

    changed = True
    while changed:
        changed = False
        for p, q in all_pairs(n):
            if not table[(p, q)]:
                for a in alphabet:
                    p_next = transitions[p][a]
                    q_next = transitions[q][a]
                    if p_next != q_next:
                        key = (min(p_next, q_next), max(p_next, q_next))
                        if key in table and table[key]:
                            table[(p, q)] = True
                            changed = True
                            break

    
    equivalents = []
    for p, q in all_pairs(n):
        if not table[(p, q)]:
            equivalents.append((p, q))
    return equivalents


def main():
    dfas = dfa_minimization()
    for n, alphabet, finals, transitions in dfas:
        eq = minimize_dfa(n, alphabet, finals, transitions)
        print(" ".join(f"({p}, {q})" for p, q in eq))


if __name__ == "__main__":
    main()
