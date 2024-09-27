import re

class TruthTable:
    def __init__(self, kb, query):
        self.kb = [f"{' & '.join(premises)} => {conclusion}" if premises else conclusion for premises, conclusion in kb]
        self.query = query  
        self.variables = self.get_variables()  
        self.facts = self.get_facts()  
        self.cols = len(self.variables)  
        self.rows = 2 ** self.cols  
        self.table = []  
        self.formula_result = []  
        self.query_result = []  
        self.literal_index = []  
        self.fact_index = []  
        self.entailed = []  
        self.result = ""  
        self.count = 0  

    def get_variables(self):
        variables = set()
        for clause in self.kb:
            for token in re.findall(r'\b[a-z]\w*\b', clause):
                variables.add(token)
        return list(variables)

    def get_facts(self):
        facts = []
        for clause in self.kb:
            if '=>' not in clause and '&' not in clause and '|' not in clause:
                facts.append(clause.strip())
        return facts

    def generate_table(self):
        self.table = [[False] * self.cols for _ in range(self.rows)]
        self.formula_result = [True] * self.rows
        self.query_result = [False] * self.rows
        if not self.kb:
            max_literals = 0
        else:
            max_literals = max(len(clause.split('=>')[0].split('&')) for clause in self.kb)
        self.literal_index = [[-1] * max_literals for _ in range(len(self.kb))]
        self.fact_index = [-1] * len(self.facts)
        self.entailed = [-1] * len(self.kb)

        for row in range(self.rows):
            for col in range(self.cols):
                self.table[row][col] = (row >> (self.cols - 1 - col)) & 1 == 1

        self.populate_indices()

        if self.check_facts():
            self.result = f"YES: {self.count}"
        else:
            self.result = "NO"

    def populate_indices(self):
        for i, fact in enumerate(self.facts):
            if fact in self.variables:
                self.fact_index[i] = self.variables.index(fact)
        for i, clause in enumerate(self.kb):
            if '=>' in clause:
                lhs, rhs = clause.split('=>')
                lhs_parts = lhs.split('&')
                for j, part in enumerate(lhs_parts):
                    if part.strip() in self.variables:
                        self.literal_index[i][j] = self.variables.index(part.strip())
                if rhs.strip() in self.variables:
                    self.entailed[i] = self.variables.index(rhs.strip())

    def check_facts(self):
        for i in range(self.rows):
            if self.query in self.variables:
                if not self.table[i][self.variables.index(self.query)]:
                    self.formula_result[i] = False
                    self.query_result[i] = False
                else:
                    self.query_result[i] = True

            for j in range(len(self.fact_index)):
                if self.formula_result[i]:
                    if self.facts[j] in self.variables:
                        self.formula_result[i] = self.table[i][self.fact_index[j]]
                    else:
                        break
                else:
                    break

        for i in range(self.rows):
            if self.formula_result[i]:
                for j in range(len(self.literal_index)):
                    if len(self.kb[j].split('=>')[0].split('&')) == 2:
                        if (self.table[i][self.literal_index[j][0]] and
                            self.table[i][self.literal_index[j][1]] and
                            not self.table[i][self.entailed[j]]):
                            self.formula_result[i] = False
                    else:
                        if (self.table[i][self.literal_index[j][0]] and
                            not self.table[i][self.entailed[j]]):
                            self.formula_result[i] = False

        for i in range(self.rows):
            if self.formula_result[i]:
                self.count += 1
            if not self.query_result[i] and self.formula_result[i]:
                return False

        return True
