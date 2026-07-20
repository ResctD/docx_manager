'''
Функция рекурсивного сбора файлов вместе с путями
'''

import os

def frecurs(folder):
    docx_files = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename in files:
                if filename.endswith(".docx"):
                    docx_files.append(os.path.join(root, filename))
    return docx_files

