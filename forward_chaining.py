from collections import defaultdict, deque

class ForwardChaining:
    def __init__(self, kb, query):
        self.kb = kb  # Knowledge base (a list of premises and conclusions)
        self.query = query  # The query to be proven

    def run(self):
        # Dictionary to keep track of which symbols have been inferred
        inferred = defaultdict(bool)
        
        # Dictionary to count how many premises are needed to infer each conclusion
        count = {c: len(premises) for premises, c in self.kb}
        
        # Queue to hold symbols that have no premises (i.e., known facts)
        agenda = deque([c for premises, c in self.kb if not premises])
        
        # List to keep track of the inferred symbols in order
        inferred_symbols = []

        # Process the agenda until it is empty
        while agenda:
            p = agenda.popleft()  # Get the next symbol from the agenda
            if not inferred[p]:  # If this symbol has not already been inferred
                inferred[p] = True  # Mark it as inferred
                inferred_symbols.append(p)  # Add it to the list of inferred symbols
                
                # Iterate through the knowledge base to find rules where this symbol is a premise
                for premises, c in self.kb:
                    if p in premises:  # If the symbol is a premise in this rule
                        count[c] -= 1  # Decrease the count of needed premises for the conclusion
                        if count[c] == 0:  # If all premises for the conclusion are inferred
                            agenda.append(c)  # Add the conclusion to the agenda

        # Return whether the query has been inferred and the list of inferred symbols
        return inferred[self.query], inferred_symbols