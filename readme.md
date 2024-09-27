# AI Inference Engine

## Description
This project implements an AI inference engine capable of performing logical reasoning using various algorithms including Truth Table, Backward Chaining, and Forward Chaining.

## Installation
Clone the repository and ensure you have Python installed on your system.
```
git clone <repository-url>
cd <project-directory>
```

## Usage

### Running Unit Tests
To run the unit tests:
```
python -m unittest codetest.py
```
### Running the Inference Engine
Use the following format to run the inference engine:
```
python iengine.py <knowledge_base_file> <algorithm>
```
Where:
- <knowledge_base_file> is the path to your Horn clause knowledge base file
- <algorithm> is one of the following:
  - TT for Truth Table
  - BC for Backward Chaining
  - FC for Forward Chaining

Examples:
```
python iengine.py test_HornKB.txt TT
python iengine.py test_HornKB.txt BC
python iengine.py test_HornKB.txt FC
```

## Future Improvements

* Truth Table Implementation
   * Issues with certain test cases

* Backward Chaining Implementation
   * Issues with certain test cases

* Expand Test Cases
   * Develop comprehensive test suite with edge cases

* Generalize Knowledge Base
   * Extend to handle general propositional logic
   * Implement parser for handling different formats


