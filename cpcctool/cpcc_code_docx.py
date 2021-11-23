'''
@File: cpcc_code_docx.py
@Description: Generate source code word document
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2019-12-17 15:29:51
'''

import os
import uuid
import tempfile
import win32com.client as win32
from .source_tie import tie
from .txt2docx import txt2docx

def docx_first_n_pages(docx_file, dst_file, n):
  app = win32.DispatchEx("Word.Application")
  app.Visible = 0
  app.DisplayAlerts = 0
  app.Documents.Open(docx_file)
  try:
    doc = app.ActiveDocument
    doc.Repaginate()
    page_count = doc.ComputeStatistics(2)
    app.Selection.GoTo(1, 1, n)
    r = doc.Bookmarks("\\Page").Range
    app.Selection.GoTo(1, 1, page_count)
    r.End = doc.Bookmarks("\\Page").Range.End
    r.Delete()
    doc.SaveAs(dst_file, 16)
    doc.Close(SaveChanges=0)
  finally:
    app.Quit()

def docx_last_n_pages(docx_file, dst_file, n):
  app = win32.DispatchEx("Word.Application")
  app.Visible = 0
  app.DisplayAlerts = 0
  app.Documents.Open(docx_file)
  try:
    doc = app.ActiveDocument
    doc.Repaginate()
    page_count = doc.ComputeStatistics(2)
    app.Selection.GoTo(1, 1, 1)
    r = doc.Bookmarks("\\Page").Range
    app.Selection.GoTo(1, 1, page_count - n)
    r.End = doc.Bookmarks("\\Page").Range.End
    r.Delete()
    doc.SaveAs(dst_file, 16)
    doc.Close(SaveChanges=0)
  finally:
    app.Quit()

def docx_sandwich(docx_file, dst_file, first_n, last_n):
  app = win32.DispatchEx("Word.Application")
  app.Visible = 0
  app.DisplayAlerts = 0
  app.Documents.Open(docx_file)
  try:
    doc = app.ActiveDocument
    doc.Repaginate()
    page_count = doc.ComputeStatistics(2)
    app.Selection.GoTo(1, 1, first_n + 1)
    r = doc.Bookmarks("\\Page").Range
    app.Selection.GoTo(1, 1, page_count - last_n)
    r.End = doc.Bookmarks("\\Page").Range.End
    r.Delete()
    doc.SaveAs(dst_file, 16)
    doc.Close(SaveChanges=0)
  finally:
    app.Quit()

def gen_code_docx(src_dirs, dst_file):
  tmp_txt_file = tempfile.gettempdir() + os.sep + str(uuid.uuid4())
  tie(src_dirs, tmp_txt_file)
  txt2docx(tmp_txt_file, dst_file)