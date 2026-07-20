import os
from unittest import result

from docx import Document
from engine.recurs import frecurs
from engine import colors

def fcomments(folder):
    files = frecurs(folder)
    for filepath in files:
        try:
            doc = Document(filepath)
            if doc.comments:
                print(colors.green(f"✅ Have comments here {filepath}"))
            else:
                print(f"❌ No comments {filepath}")
        except Exception as e:
            print(f" Error {filepath}: {e}")

    return result


