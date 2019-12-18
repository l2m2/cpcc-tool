# cpcc-tool
申请软件著作权用到的一些工具，包括生成源代码Word文档，统计源码量等。

**生成源代码前40页和后40页的文档示例**

```python
  import uuid
  import os
  from cpcctool import gen_code_docx, docx_first_40_pages, docx_last_40_pages
  src_dirs = [
    r"F:\workspace\xxx\code1\",
    r"F:\workspace\xxx\code2\"
  ]
  dst_file = str(uuid.uuid4()) + ".docx"
  gen_code_docx(src_dirs, dst_file)
  dst_file = os.path.abspath(dst_file)
  docx_first_40_pages(dst_file, r"xxx系统 XXX V2.0.0 源代码 前40页.docx")
  docx_last_40_pages(dst_file, r"xxx系统 XXX V2.0.0 源代码 后40页.docx")
```

**统计源代码总量示例**

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

## Reference

- [CLOC](https://github.com/AlDanial/cloc)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)
- [How do I delete a range (pages) in a document using VBA.](https://social.msdn.microsoft.com/Forums/office/en-US/b5b34fd3-e36b-432c-94d2-9c687e273440/how-do-i-delete-a-range-pages-in-a-document-using-vba?forum=worddev)