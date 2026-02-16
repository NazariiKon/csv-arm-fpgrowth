# csv-arm-fpgrowth

Python library for converting CSV files to association rules format and running FPGrowth.
### !!!!Now its just a Hello World library!!!
## Install

```bash
pip install --index-url https://test.pypi.org/simple/ csv-arm-fpgrowth
```

## Quick Start

```python
from csv_arm_fpgrowth import hello, csv_to_arm

print(hello())  # "csv-arm-fpgrowth ready!"
```

## Development

### Setup

```bash
# with uv (recommended)
uv sync

# with pip
pip install -e .
```

### Run

```bash
python main.py
```

### Tests

```bash
python -m pytest tests/
```

### Build & Publish

```bash
python -m build
twine upload --repository testpypi dist/*
```