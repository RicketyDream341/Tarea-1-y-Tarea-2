import sys

def fresh_nonterminal():
    
    for c in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
        yield c

def eliminate_left_recursion(nonterminals, productions):
   
    n = len(nonterminals)
    grammar = {nt: productions[nt][:] for nt in nonterminals}
    result = {}

    fresh = fresh_nonterminal()
    for i in range(n):
        Ai = nonterminals[i]
        for j in range(i):
            Aj = nonterminals[j]
            new_prods = []
            for prod in grammar[Ai]:
                if prod.startswith(Aj):
                    rest = prod[len(Aj):]
                    for beta in result[Aj]:
                        new_prods.append(beta + rest)
                else:
                    new_prods.append(prod)
            grammar[Ai] = new_prods
        alphas = []
        betas = []
        for prod in grammar[Ai]:
            if prod.startswith(Ai):
                alphas.append(prod[len(Ai):])
            else:
                betas.append(prod)

        if alphas:
            while True:
                new_nt = next(fresh)
                if new_nt not in grammar and new_nt not in result:
                    break
            result[Ai] = [b + new_nt for b in betas]
            result[new_nt] = [a + new_nt for a in alphas] + ['e']
        else:
            result[Ai] = grammar[Ai]

    return result


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    idx = 0
    n = int(lines[idx]); idx += 1 

    for _ in range(n):
        k = int(lines[idx]); idx += 1
        nonterminals = []
        productions = {}
        for _ in range(k):
            left, right = lines[idx].split("->")
            idx += 1
            left = left.strip()
            rights = right.strip().split()
            nonterminals.append(left)
            productions[left] = rights

        result = eliminate_left_recursion(nonterminals, productions)

        for nt in nonterminals:
            if nt in result:
                print(f"{nt} -> {' '.join(result[nt])}")
        for nt in result:
            if nt not in nonterminals:
                print(f"{nt} -> {' '.join(result[nt])}")
        print()


if __name__ == "__main__":
    main()

