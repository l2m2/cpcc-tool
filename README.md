# cpcc-tool
申请软件著作权用到的一些工具，包括生成源代码Word文档，统计源码量等。

**生成源代码前40页和后40页的文档示例**

```py
  src_dirs = [
    r"F:\workspace\toplinker\svn\topweb\scm-b2b\09-code\trunk",
  ]
  dst_file = str(uuid.uuid4()) + ".docx"
  gen_code_docx(src_dirs, dst_file)
  dst_file = os.path.abspath(dst_file)
  docx_first_40_pages(dst_file, r"东领采购B2B系统 TopB2B V2.0.0 源代码 前40页.docx")
  docx_last_40_pages(dst_file, r"东领采购B2B系统 TopB2B V2.0.0 源代码 后40页.docx")
```

