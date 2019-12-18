'''
@File: cpcc_count_code_lines.py
@Description: Count source code lines
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2019-12-18 08:57:34
'''

import subprocess
import re

def count_code_lines(cloc_exe, src_dirs):
  run_args = [cloc_exe]
  run_args.extend(src_dirs)
  pinfo = subprocess.run(run_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  if pinfo.returncode != 0:
    print("run cloc failed.")
    return 0
  output = pinfo.stdout.decode()
  print(output)
  m = re.search(r'SUM:.*\s(\d+)', output)
  if not m:
    return False
  return m[1]