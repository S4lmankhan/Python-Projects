
---

# PDF Merger Script

This Python script allows you to merge multiple PDF files into a single PDF using the PyPDF2 library. Simply update the names of your PDF files and run the script to combine them into one document.

## Prerequisites

- Python 3.x
- PyPDF2 library

## Installation

First, ensure you have Python installed. Then, install the PyPDF2 library using pip:

```bash
pip install PyPDF2
```

## Usage

1. **Update the PDF file names**: Modify the `pdfiles` list in the script to include the names of the PDF files you want to merge. For example:

    ```python
    pdfiles = ["file1.pdf", "file2.pdf", "file3.pdf"]
    ```

2. **Update the output file name**: Set the desired name for the merged PDF file in the `merger.write` function. For example:

    ```python
    merger.write("merged_document.pdf")
    ```

3. **Run the script**: Execute the script to merge the PDFs.

    ```python
    import PyPDF2

    # Update the name of your PDF files below
    pdfiles = ["file1.pdf", "file2.pdf", "file3.pdf"]

    merger = PyPDF2.PdfMerger()
    for name in pdfiles:
        file = open(name, 'rb')
        pdfReader = PyPDF2.PdfReader(file)
        merger.append(pdfReader)
        file.close()
    merger.write("merged_document.pdf")
    ```

4. The script will combine the specified PDF files into a single PDF named `merged_document.pdf` (or whatever name you specified).

## Example

Here is a complete example of the script:

```python
import PyPDF2

# Update the name of your PDF files below
pdfiles = ["file1.pdf", "file2.pdf", "file3.pdf"]

merger = PyPDF2.PdfMerger()
for name in pdfiles:
    file = open(name, 'rb')
    pdfReader = PyPDF2.PdfReader(file)
    merger.append(pdfReader)
    file.close()
merger.write("merged_document.pdf")
```

## Contact

If you encounter any issues or have any questions, feel free to reach out to me on Instagram: [CodeWithSalty](https://www.instagram.com/CodeWithSalty).

## Credits

This script is created and maintained by [Salman Khan](https://github.com/S4lmankhan). If you find it useful, please give credit where it's due.

## License

This script is provided under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

