import sys
import os
import difflib

def comp(file1,file2):
    with open(file1,'r') as f:
        lines = f.readlines()
        lines1 = [x.strip() for x in lines]
    with open(file2,'r') as f:
        lines = f.readlines()
        lines2 = [x.strip() for x in lines]
    equal_item = [x for x in lines1 if x in lines2]
    unqual_item = [y for y in (lines1+lines2) if y not in equal_item]
    file1_diff = [x for x in unqual_item if x in lines1]
    file2_diff = [y for y in unqual_item if y in lines2]

    return(file1_diff,file2_diff)


if __name__ == '__main__':
    print(comp('d:\\修订31\\serverinfo','d:\发布\V9.3.1_190826_修订31发布包\监控终端\\serverinfo'))