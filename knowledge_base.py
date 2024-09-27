import sys
from collections import defaultdict, deque
import re
from forward_chaining import ForwardChaining
from backwards_chaining import BackwardChaining
from truth_table import TruthTable

class KnowledgeBase:
    def __init__(self, filename):
        self.kb, self.query = self.parse_file(filename)

    def parse_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.read().splitlines()
                tell_index = lines.index("TELL")
                ask_index = lines.index("ASK")
                kb_str = "".join(lines[tell_index + 1:ask_index]).strip()
                query = lines[ask_index + 1].strip()
                return self.parse_kb(kb_str), query
        except (FileNotFoundError, ValueError):
            print("Usage: python iengine.py <input_file> <method>")
            sys.exit(1)

    @staticmethod
    def parse_kb(kb_str):
        clauses = kb_str.strip().split(";")
        kb = []
        for clause in clauses:
            clause = clause.strip()
            if not clause:
                continue
            if "=>" in clause:
                premise, conclusion = clause.split("=>")
                premises = tuple(p.strip() for p in premise.split("&"))
                kb.append((premises, conclusion.strip()))
            else:
                kb.append(((), clause.strip()))
        return kb

    def forward_chaining(self):
        fc = ForwardChaining(self.kb, self.query)
        return fc.run()

    def backward_chaining(self):
        bc = BackwardChaining(self.kb, self.query)
        return bc.execute()  # Change from run() to execute()

    def truth_table(self):
        tt = TruthTable(self.kb, self.query)
        tt.generate_table()
        return tt.result
