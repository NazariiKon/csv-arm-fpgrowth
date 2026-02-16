#!/usr/bin/env python3
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Imports
import pandas as pd  # Для типов
import logging

from csv_arm_fpgrowth import csv_to_arm, hello

def main():
    logging.basicConfig(level=logging.INFO)
    
    print("=== csv-arm-fpgrowth Production Demo ===")
    print(hello())
    
    csv_path = Path(__file__).parent / "tests" / "data" / "test.csv"
    
    print(f"\nProcessing: {csv_path}")
    rules, itemsets = csv_to_arm(
        str(csv_path),
        min_support=0.1,
        min_confidence=0.3,
        debug=True
    )
    
    print("\n=== ASSOCIATION RULES ===")
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].round(3))
    
    print("\n=== FREQUENT ITEMSETS ===")
    print(itemsets.round(3))

if __name__ == "__main__":
    main()
