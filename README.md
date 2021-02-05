# cpcc-tool
Some method for Software copyright application in China, including the generation of source code Word documents, source code statistics, etc.

```
pip install cpcctool
```

**Example: Generate documentation for the first and last 40 pages of source code**

```python
  import uuid
  import os
  from cpcctool import gen_code_docx, docx_first_n_pages, docx_last_n_pages
  src_dirs = [
    r"F:\workspace\xxx\code1\",
    r"F:\workspace\xxx\code2\"
  ]
  dst_file = str(uuid.uuid4()) + ".docx"
  gen_code_docx(src_dirs, dst_file)
  dst_file = os.path.abspath(dst_file)
  docx_first_n_pages(dst_file, r"xxxSystem XXX V2.0.0 Source Code first 40 pages.docx", 40)
  docx_last_n_pages(dst_file, r"xxxSystem XXX V2.0.0 Source Code last 40 pages.docx", 40)
```

**Example: Statistics source code total lines**

```python
from cpcctool import count_code_lines
src_dirs = [
    r"F:\workspace\xxx\code1\",
    r"F:\workspace\xxx\code2\"
]
cloc_exe = r"F:\workspace\l2m2\cpcc-tool\cloc-1.84.exe"
count = count_code_lines(cloc_exe, src_dirs)
print(count)
```

## Publish to PyPI

```
pip install --user --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

## Reference

- [CLOC](https://github.com/AlDanial/cloc)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)
- [How do I delete a range (pages) in a document using VBA.](https://social.msdn.microsoft.com/Forums/office/en-US/b5b34fd3-e36b-432c-94d2-9c687e273440/how-do-i-delete-a-range-pages-in-a-document-using-vba?forum=worddev)