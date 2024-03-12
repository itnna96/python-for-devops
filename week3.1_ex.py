#!/usr/bin/env python
"""
Write a python script to call shell function `df -h`. Using `argv` to receive an
argument as 'file_system', if user not input, take the default as '/'.
Print the size and available spaces on that disk. If error, handle the error.
"""
import argparse
import subprocess,sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        disk_name = '/'
    else:
        disk_name = sys.argv[1]
    output = subprocess.run(['df','-h',disk_name],capture_output=True,text=True)
    if output.returncode != 0:
        print(f'Error: {output.stderr}')
        exit(1)
    line = output.stdout.split('\n')[1]
    total_size = line.split()[1]
    total_avail = line.split()[3]
    print(f'Size: {total_size}')
    print(f'Avail: {total_avail}')



