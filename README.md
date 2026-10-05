# Document Section Parser

A small Python utility for extracting the text of one section from a DOCX file by matching a start heading and stopping before the next heading.

## What it does

This project reads a Microsoft Word document using `python-docx` and returns the text between two section names, such as:

- Start heading: `Section 1`
- End heading: `Section 2`

It is useful when you want to pull a specific section from a document without manually copying content.

## Usage

1. Install the dependency:

```bash
pip install python-docx
```

2. Run the script or call the function from Python:

```python
from extract_section import extract_section_from_docx

section = extract_section_from_docx(
    "input/section_test.docx",
    "Section 1",
    "Section 2",
)

print(section)
```

The example in `extract_section.py` uses a sample document at `input/section_test.docx` and extracts text between `Section 1` and `Section 2`.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.