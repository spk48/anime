import opencc
import os
import sys
from optparse import OptionParser

helpstr = ('\n'
           'help\n'
           '本python脚本用来处理字幕繁简转换问题\n'
           '使用示例：\n'
           'python3 transtosc.py \'放有字幕的path_1\' \'放有字幕的path_2\'\n'
           '本脚本只读取 srt ass 后缀文件\n'
           '转换完毕的文件会放置在下级目录的new之中\n'
           'PS:\n'
           '本脚本只读取一层目录 AND 只支持 UTF-8\n')


def t2s(i):
    ass_files = [name for name in os.listdir(i)
                 if (name.endswith('.ass') or name.endswith('.srt'))]
    for data in ass_files:
        old_data = i + '/' + data
        new = (i + '/new')
        isExists = os.path.exists(new)
        if not isExists:
            os.mkdir(new)
            print("目录不存在 创建新目录")
        f = open(old_data, 'rt')
        reader = f.read()
        tem = opencc.OpenCC('t2s')
        new_data = new + '/' + data
        nf = open(new_data, 'wt')
        nf.write(tem.convert(reader))
        print(old_data + "处理完毕")


if __name__ == "__main__":
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" :
        print(helpstr)
        exit()

    num = 0
    for i in sys.argv:
        if num != 0:
            t2s(i)
        num = num + 1
