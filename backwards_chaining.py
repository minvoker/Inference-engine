
class BackwardChaining:
    def __init__(self, kb, query):
        self.kb = kb  # Knowledge base
        self.query = query  # Query to be proven

    def execute(self):
        known_facts = {conclusion for premises, conclusion in self.kb if not premises}  # Known facts (no premises)
        used_facts = set()  # Set to keep track of used facts
        result = self.backward_chain(self.query, known_facts, used_facts)  # Start backward chaining
        return result, used_facts  # Return if the query is proven and the used facts

    def backward_chain(self, query, known_facts, used_facts):
        if query in known_facts:  # If the query is a known fact
            used_facts.add(query)  # Add it to used facts
            return True  # Return True

        for premises, conclusion in self.kb:
            if conclusion == query:  # If the conclusion matches the query
                all_true = all(self.backward_chain(p, known_facts, used_facts) for p in premises)  # Check all premises
                if all_true:  # If all premises are true
                    known_facts.add(query)  # Add the query to known facts
                    used_facts.add(query)  # Add the query to used facts
                    return True  # Return True

        return False  # Return False if the query cannot be proven