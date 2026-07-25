import zipfile
import xml.etree.ElementTree as ET
from engine import colors


from engine.recurs import frecurs

def comments_out(filepath):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    files = frecurs(filepath)
    result = {}

    for filepath in files:
        try:
            with zipfile.ZipFile(filepath, 'r') as docx_zip:
                if 'word/comments.xml' not in docx_zip.namelist():
                    continue

                comments_xml = docx_zip.read('word/comments.xml')
                root = ET.fromstring(comments_xml)
                comments = root.findall('.//w:comment', ns)

                if not comments:
                    continue

                found_any = True
                print(f"\n📄 {filepath}")


                for comment in comments:
#                    comment_id = comment.get('id') # Оставить вариант для других ns
                    comment_id = comment.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id')
                    text_part = []
                    for t in comment.findall('.//w:t', ns):
                        if t.text:
                            text_part.append(t.text)
                    text = ''.join(text_part)
                    print(colors.green(f"[{comment_id}] {text}"))

        except KeyError as e:
            print(colors.red(f" Файл {filepath} повреждён: {e}"))
        except Exception as e:
            print(colors.red(f" Ошибка при обработке {filepath}: {e}"))

    if not found_any:
        print(colors.yellow("ℹ️  Комментарии не найдены ни в одном документе."))

    return result





