# Json to table view

Convert json file into tables with data models, saves refs betweeen models.

## Installation

#### Prerequisites

Need to install uv package:
`pip install uv`

#### How to start
```
pip install uv
uv sync
source .venv/bin/activate
```

Now you can start using `uv run main.py [file_name]` or `bash main.sh` (contains same comand)

## Usage
1. Place files .json in /jsons, 2 examples already ther
2. Run `uv run main.py [file_name]`
3. After processing will be created folder /converted_table, wich will contain converted json`s file in .md format

