from forward_chaining import ForwardChaining
from backwards_chaining import BackwardChaining
from truth_table import TruthTable

def run_fc_tests():
    print("Forward Chaining Tests:")
    test_cases = [
        ([([], 'A')], 'A', True, ['A']),  # Testing if the query is a known fact in the KB
        ([(['A'], 'B'), ([], 'A')], 'B', True, ['A', 'B']),  # Testing forward chaining with one rule
        ([(['A', 'B'], 'C'), ([], 'A'), ([], 'B')], 'C', True, ['A', 'B', 'C']),  # Testing multiple rules leading to the query
        ([(['A'], 'B'), ([], 'C')], 'B', False, ['C']),  # Testing when the query cannot be inferred
        ([(['A'], 'B'), (['B'], 'C'), ([], 'A')], 'C', True, ['A', 'B', 'C']),  # Testing complex inference with multiple rules
        ([(['B'], 'A'), (['A'], 'B'), ([], 'A')], 'B', True, ['A', 'B']),  # Testing cycle in the knowledge base
    ]
    
    for i, (kb, query, expected_result, expected_symbols) in enumerate(test_cases):
        fc = ForwardChaining(kb, query)
        result, symbols = fc.run()
        print(f"Test Case {i+1}: {'Passed' if (result == expected_result and symbols == expected_symbols) else 'Failed'}")

def run_bc_tests():
    print("Backward Chaining Tests:")
    test_cases = [
        ([([], 'A')], 'A', True, {'A'}),  # Testing if the query is a known fact in the KB
        ([(['A'], 'B'), ([], 'A')], 'B', True, {'A', 'B'}),  # Testing backward chaining with one rule
        ([(['A', 'B'], 'C'), ([], 'A'), ([], 'B')], 'C', True, {'A', 'B', 'C'}),  # Testing multiple rules leading to the query
        ([(['A'], 'B'), ([], 'C')], 'B', False, set()),  # Testing when the query cannot be inferred
        ([(['A'], 'B'), (['B'], 'C'), ([], 'A')], 'C', True, {'A', 'B', 'C'}),  # Testing complex inference with multiple rules
    ]
    
    for i, (kb, query, expected_result, expected_used_facts) in enumerate(test_cases):
        bc = BackwardChaining(kb, query)
        result, used_facts = bc.execute()
        print(f"Test Case {i+1}: {'Passed' if (result == expected_result and used_facts == expected_used_facts) else 'Failed'}")

def run_tt_tests():
    # Using truth table expected structure (Format after parsed by KB class):
    print("Truth Table Tests:")
    test_cases = []
    
    # Test Case 1: Test truth table generation with expected "YES: 3"
    test_1, query_1 = ([(('p2',), 'p3'), (('p3',), 'p1'), (('c',), 'e'), (('b', 'e'), 'f'), (('f', 'g'), 'h'), 
                        (('p2', 'p1', 'p3'), 'd'), (('p1', 'p3'), 'c'), ((), 'a'), ((), 'b'), ((), 'p2')], 'd')
    test_cases.append((test_1, query_1, "YES: 3"))
    
    # Test Case 2: Test truth table generation with expected "NO"
    test_2, query_2 = ([(('p2',), 'p3'), (('p3',), 'p1'), (('c',), 'e'), (('b', 'e'), 'f'), (('f', 'g'), 'h'), 
                        (('p2', 'p1', 'p3'), 'd'), (('p1', 'p3'), 'c'), ((), 'a'), ((), 'b'), ((), 'p2')], 'z')
    test_cases.append((test_2, query_2, "NO"))
    
    # Test Case 3: Test get_variables method
    test_3_kb = [(('p2',), 'p3'), (('p3',), 'p1'), (('c',), 'e'), (('b', 'e'), 'f'), (('f', 'g'), 'h'), 
                 (('p2', 'p1', 'p3'), 'd'), (('p1', 'p3'), 'c'), ((), 'a'), ((), 'b'), ((), 'p2')]
    expected_variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'p1', 'p2', 'p3']
    test_cases.append((test_3_kb, None, expected_variables))  # None for query as it's not needed for this test
    
    # Test Case 4: Test get_facts method
    test_4_kb = [(('p2',), 'p3'), (('p3',), 'p1'), (('c',), 'e'), (('b', 'e'), 'f'), (('f', 'g'), 'h'), 
                 (('p2', 'p1', 'p3'), 'd'), (('p1', 'p3'), 'c'), ((), 'a'), ((), 'b'), ((), 'p2')]
    expected_facts = ['a', 'b', 'p2']
    test_cases.append((test_4_kb, None, expected_facts))  # None for query as it's not needed for this test
    
    # Test Case 5: Test handling multiple independent queries
    test_5_kb = [(('p1',), 'p2'), (('p3',), 'p4'), ((), 'p1'), ((), 'p3')]
    query_5 = 'p4'
    expected_result_5 = "YES: 1"
    test_cases.append((test_5_kb, query_5, expected_result_5))
    
    for i, (kb, query, expected_result) in enumerate(test_cases):
        tt = TruthTable(kb, query if query else "")  # Initialize with an empty query if None
        if i == 2:  # Test get_variables method
            result = sorted(tt.get_variables())  # Sort the result for comparison
            expected_result = sorted(expected_result)
        elif i == 3:  # Test get_facts method
            result = tt.get_facts()
        else:
            tt.generate_table()
            result = tt.result
        
        print(f"Test Case {i+1}: {'Passed' if result == expected_result else 'Failed'}")


if __name__ == "__main__":
    run_fc_tests()
    run_bc_tests()
    run_tt_tests()
