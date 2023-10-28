import re
s='girl fr   ien  d'
def dashrepl(match_obj):
    if match_obj.group()==' ':
        return ' '
    else:
        return ''
if __name__ == '__main__':#当模块直接运行时，以下代码块将被运行；当模块被导入时，以下代码块不被运行
    print(re.sub(r' +',dashrepl,s))
    print(re.subn(r' +',dashrepl,s))
