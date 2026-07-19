import os
from unittest import result

from docx import Document


def fcomments(folder):
    for root, dirs, file in os.walk(folder):
        for filename in file:
            if filename.endswith('.docx'):
                filepath = os.path.join(root, filename)
                try:
                    doc = Document(filepath)
                    if doc.comments:
                        print(f"✅ Have comments here {filepath}")
                    else:
                        print(f"❌ No comments {filepath}")
                except Exception as e:
                    print(f" Error {filepath}: {e}")

    return result


