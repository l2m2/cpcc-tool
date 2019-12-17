'''
@File: cpcc_code_docx.py
@Description: Generate source code word document
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2019-12-17 15:29:51
'''

import os
import uuid
import tempfile
import win32com.client
from .source_tie import tie
from .txt2docx import txt2docx

def first_40_pages(docx_file, dst_file):
  app = win32com.client.DispatchEx("Word.Application")
  app.Visible = 0
  app.DisplayAlerts = 0
  app.Documents.Open(docx_file)
  doc = app.ActiveDocument
  app.Quit()

def last_40_pages(docx_file, dst_file):
  pass

def gen_code_docx(src_dirs, dst_file):
  tmp_txt_file = tempfile.gettempdir() + os.sep + str(uuid.uuid4())
  tie(src_dirs, tmp_txt_file)
  txt2docx(tmp_txt_file, dst_file)