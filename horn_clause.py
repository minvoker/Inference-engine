"""Horn Clause data type for use in Knowledge Base. If run as main will test the class"""


class HornClause:
    def __init__(self, clause):
        if "=>" in clause:  # If clause has '=>', then it is a definite clause
            body, head = clause.split("=>")
            # Strip leading and trailing whitespaces
            self.head = head.strip()

            # Split body into literals and strip leading and trailing whitespaces
            self.body = [literal.strip() for literal in body.split("&")]
        else:  # If does not have '=>', then it is a fact
            self.head = clause.strip()
            self.body = []

    def __str__(self):
        if not self.body:
            # If the body is empty, it is a fact, Return only the head of the clause
            return self.head
        else:
            # If the body is not empty, it is a definite clause
            # Join the body literals with ' & '
            body_str = " & ".join(self.body)
            return f"{body_str} => {self.head}"

    def is_fact(self):  # Check if fact (has empty body)
        return len(self.body) == 0

    def is_definite_clause(self):  # Check if definite (has non-empty body)
        return len(self.body) > 0


""" Test HornClause class"""
if __name__ == "__main__":
    print()
    # Test case 1: Definite clause
    hc1 = HornClause("p1 & p3 => c")
    print(hc1)
    print("Is definite clause?", hc1.is_definite_clause())
    print("Is fact?", hc1.is_fact())
    print()

    # Test case 2: Fact
    hc2 = HornClause("a")
    print(hc2)
    print("Is definite clause?", hc2.is_definite_clause())
    print("Is fact?", hc2.is_fact())
    print()

    # Test case 3: Definite clause with single literal in body
    hc3 = HornClause("p2 => p3")
    print(hc3)
    print("Is definite clause?", hc3.is_definite_clause())
    print("Is fact?", hc3.is_fact())
    print()

    # Test case 4: Definite clause with multiple literals in body
    hc4 = HornClause("p2 & p1 & p3 => d")
    print(hc4)
    print("Is definite clause?", hc4.is_definite_clause())
    print("Is fact?", hc4.is_fact())
