# import pytest
import pandas as pd
from csv_arm_fpgrowth import hello, csv_to_arm

def test_hello():
    assert "csv-arm-fpgrowth" in hello()

def test_csv_to_arm():
    """Test FP-Growth pipeline."""
    rules, itemsets = csv_to_arm("tests/data/test.csv", min_support=0.1)
    
    assert isinstance(rules, pd.DataFrame)
    assert isinstance(itemsets, pd.DataFrame)
    assert len(itemsets) > 0, "Should find itemsets"
    assert 'support' in itemsets.columns
