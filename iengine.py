import sys
from knowledge_base import KnowledgeBase

def main():
    if len(sys.argv) != 3:
        print("Usage: python iengine.py <filename> <method>")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2]

    kb = KnowledgeBase(filename)

    if method == "FC":
        result, inferred_symbols = kb.forward_chaining()
        if result:
            print(f"YES: {', '.join(inferred_symbols)}")
        else:
            print("NO")
    elif method == "BC":
        result, used_facts = kb.backward_chaining()
        if result:
            print(f"YES: {', '.join(used_facts)}")
        else:
            print("NO")
    elif method == "TT":
        result = kb.truth_table()
        print(result)
    else:
        print("Unknown method. Use FC, BC, or TT.")

if __name__ == "__main__":
    main()
