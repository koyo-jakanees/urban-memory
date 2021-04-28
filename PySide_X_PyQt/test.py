#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import pathlib
import glob
import fnmatch

print(f'dir name: {os.path.dirname(".")}')
print(f'abspath: {os.path.abspath(".")}')
print(f'basename: {os.path.basename(__file__)}')
print(f"common prefix: {os.path.commonprefix(['/usr/lib', '/usr/bin'])}")
print(f"real path: {os.path.realpath('.')}")
print(f"relative path: {os.path.relpath('/SSG-hugo/anotherdemo/content/about/')}")
print(f'os name: {os.name}')
print(f'os uname: {os.uname()}')
print(f'os env Home: {os.environ["HOME"]}')
print(f'current dir: {os.getcwd()}')
curr_dir = os.getcwd()
# new_dir = os.chdir(f'{curr_dir}/SSG-hugo/quickstart')
# print(os.listdir(new_dir))


print('+' * 10 ,'\n')
for name in sorted(glob.glob('PySide_X_PyQt/*/*.py')):
    # if fnmatch.fnmatch(name, '*.py'):
    print(f"location: {name}")
    print(f'file basename: {os.path.basename(name)}')
    print(f"real path: {os.path.realpath(name)}")
    print(f"absolute path: {os.path.abspath(name)}")

print('+' * 10)
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print(file)
        

# import os   
# import glob
# curr_dir = os.getcwd()
# data_folder = os.chdir(f'{curr_dir}/path/to/data')

# shp_files = []
# for file in sorted(glob.glob(f'{data_folder}/*.shp')):
#     string = os.path.basename(file)
#     string2 = string[len(string) - 5] #possible replace with generic match case?
#     if string2 == 'S':
#         shp_files.append(file)

# for item in shp_files:
#     clipped = gpd.clip(gpd.read_file(item), kenya)
#     clipped.to_file('path/to/save/data')