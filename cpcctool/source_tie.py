'''
@File: tie.py
@Author: leon.li(l2m2lq@gmail.com)
@Date: 2018-09-11 09:23:44
@Last Modified By: leon.li(l2m2lq@gmail.com>)
@Last Modified Time: 2018-09-11 09:29:44
'''

import os
import argparse
import fnmatch
import re
import ntpath

def tie(src_dirs, dst_file):
  dirs = []
  if not src_dirs:
    dirs.append(os.getcwd())
  else:
    dirs = [i for i in src_dirs if os.path.isdir(i)]
  output = dst_file
  if not output:
    output = 'output.txt'
  includes = ['*.h', '*.cpp', '*.pro', '*.pri', '*.js', '*.ts', '*.css', '*.less', '*.html']
  excludes = ['*\\tags\\*', '*\\thirdparty\\*', '*\\party3\\*', '*\\demo\\*']
  # transform glob patterns to regular expressions
  includes = r'|'.join([fnmatch.translate(x) for x in includes])
  excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
  fd = open(output, 'w+', encoding='utf-8')
  for d in dirs:
    for root, _, files in os.walk(d):
      files = [os.path.join(root, f) for f in files]
      files = [f for f in files if not re.match(excludes, f)]
      files = [f for f in files if re.match(includes, f)]
      for f in files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fd2:
          print(f)
          fd.write('----{name}----'.format(name=ntpath.basename(f)))
          fd.write('\n')
          fd.write(fd2.read())
          fd.write('\n')
          fd.write('----end-of-{name}----\n\n'.format(name=ntpath.basename(f)))
  fd.close()

if __name__ == "__main__":
  # python3 source_tie.py -i source_dir1 source_dir2 -o output.txt
  parser = argparse.ArgumentParser(description='Source Tie Tool')
  parser.add_argument('-i', '--input', nargs='*',  help='Input Source Directory', required=False)
  parser.add_argument('-o', '--output', help='Output Filename', required=False)
  args = parser.parse_args()
  args = vars(args)
  tie(args['input'], args['output'])