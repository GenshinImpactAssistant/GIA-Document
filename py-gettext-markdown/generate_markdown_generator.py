import gettext
import re
import os
from util import *

def is_number(s):
    """
    懒得写,抄的
    https://www.runoob.com/python3/python3-check-is-number.html
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

class GenerateMarkdownGenerator():
    def __init__(self, folder_path, LANG):
        self.folder_path = folder_path
        self.LANG = LANG

    def _write_file(self, file_path):
        origin_file = open(file_path, 'r', encoding='utf-8').read()
        text_list = re.split('  \n|\n{2,999}|<br>|\\\\\\n',origin_file)
        # if "README" in file_path:
        #     print(text_list) 
        text_list = [i.replace('\n', '\\n').replace('\"', '\\"') for i in text_list]
        with open(file_path.replace('.md','.pygettext'), 'w', encoding='utf-8') as f:
            f.write(f'# coding:utf-8\n')
            f.write(f'import gettext, sys\n')
            f.write(f"sys.argv.pop(0)\n")
            f.write(f"LANG = sys.argv[0]\n")
            local_dir_path = os.path.join(self.folder_path, "markdown_i18n", "locale")
            f.write(f'l10n = gettext.translation(LANG, localedir = rf"{local_dir_path}", languages=[LANG])\n')
            f.write('l10n.install()\n')
            f.write(f'_ = l10n.gettext\n')
            md_path = f'{file_path.replace("base",self.LANG)}'
            verify_path(os.path.dirname(md_path))
            f.write(f'f = open(r"{md_path}", "w", encoding="utf-8")\n')
            def write_gettext(x, add_n=True):
                if x == '':
                    print("ERR: WRONG STR: NONE")
                else:
                    if add_n:
                        f.write(f'f.write(_("{x}")+str(\'\\n\'))\n')
                    else:
                        f.write(f'f.write(_("{x}")+str(\'\\n\'))')
            def write_origin(x):
                f.write(f'f.write("{x}"+str(\'\\n\'))\n')
            def write_newline():
                f.write(f'f.write("\\n")\n')
            def write_table(x):
                for ii in x.split('\\n'):
                    if ("----|----" in ii) or ("---- | ----" in ii):
                        write_origin(ii)
                    else:
                        write_gettext(ii)
            def write_title(x):
                if x[0] == '#':
                    return True
                return False
                
            def write_point(x):
                start_i = 0
                for i in range(len(x)):
                    if x[i] != ' ':
                        start_i = i
                        break
                if x[start_i:start_i+2] == '- ':
                    return True
                return False
            
            def write_123(x):
                for ii in x.split('\\n'):
                    if '. ' in ii:
                        if is_number(ii[:ii.index('. ')]):
                            return True
                return False
            
            code_flag = False
            special_key = []
            for line in text_list:
                if "<!-- ignore gettext -->" in line:
                    write_origin(line)
                elif ("----|----" in line) or ("---- | ----" in line):
                    write_table(line)
                elif "```" in line:
                    if line.count("```")>=2:
                        write_origin(line)
                    else:
                        code_flag = not code_flag
                        write_origin(line)
                elif line == "":
                    pass
                elif line == "\\n":
                    write_newline()   
                elif line == "\n":
                    write_newline()    
                        
                else:
                    if not code_flag:
                        output_line = ''
                        output_flag = False
                        for single_line in line.split('\\n'):
                            if '- ' in single_line:
                                if write_point(single_line):
                                    output_line = single_line
                                    output_flag = True
                            if '#' in single_line:
                                if write_title(single_line):
                                    output_line = single_line
                                    output_flag = True
                            if '. ' in single_line:
                                if write_123(single_line):
                                    output_line = single_line
                                    output_flag = True
                            if '>' in single_line:
                                if '>' == single_line[:1]:
                                    output_line = single_line
                                    output_flag = True
                            if output_flag:
                                write_gettext(output_line)
                                output_line = ''
                                output_flag = False
                            else:
                                output_line+=single_line
                        if output_line != '':
                            write_gettext(output_line)
                    else:
                        write_origin(line)
                write_newline()

            f.write(f'f.close()')
    
    def run(self):
        for root, dirs, files in os.walk(os.path.join(self.folder_path,"base")):
            for f in files:
                if f.split('.')[-1] in ['md', 'markdown']:
                    filepath = os.path.join(root, f)
                    print(f"generate pygettext {filepath}")
                    self._write_file(filepath)

if __name__ == "__main__":
    gmg = GenerateMarkdownGenerator(os.path.abspath(r'./'), "zh_CN")
    gmg.run()