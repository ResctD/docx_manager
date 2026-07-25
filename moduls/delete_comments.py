import zipfile
import shutil
import os
import re

from engine.recurs import frecurs

# Части документа, отвечающие за комментарии
COMMENT_PARTS = {
    'word/comments.xml',
    'word/commentsExtended.xml',
    'word/commentsIds.xml',
    'word/commentsExtensible.xml',
}

# Теги-ссылки на комментарии внутри document.xml (самозакрывающиеся)
COMMENT_TAG_PATTERN = re.compile(
    r'<w:comment(RangeStart|RangeEnd|Reference)\b[^>]*/>'
)


def _clean_document_xml(xml_bytes):
    text = xml_bytes.decode('utf-8')
    text = COMMENT_TAG_PATTERN.sub('', text)
    return text.encode('utf-8')


def _clean_content_types(xml_bytes):
    text = xml_bytes.decode('utf-8')
    text = re.sub(
        r'<Override[^>]+PartName="/word/comments[^"]*"[^>]*/>',
        '',
        text
    )
    return text.encode('utf-8')


def _clean_rels(xml_bytes):
    text = xml_bytes.decode('utf-8')
    text = re.sub(
        r'<Relationship[^>]+Target="comments[^"]*\.xml"[^>]*/>',
        '',
        text
    )
    return text.encode('utf-8')


def _remove_comments_from_file(docx_path):
    tmp_path = docx_path + '.tmp'

    try:
        with zipfile.ZipFile(docx_path, 'r') as zin:
            with zipfile.ZipFile(tmp_path, 'w', zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    name = item.filename

                    # Полностью выкидываем части с комментариями
                    if name in COMMENT_PARTS:
                        continue

                    data = zin.read(name)

                    if name == 'word/document.xml':
                        data = _clean_document_xml(data)
                    elif name == '[Content_Types].xml':
                        data = _clean_content_types(data)
                    elif name == 'word/_rels/document.xml.rels':
                        data = _clean_rels(data)

                    zout.writestr(item, data)

        shutil.move(tmp_path, docx_path)
        return True

    except Exception as e:
        print(f"  ⚠ Ошибка при обработке {docx_path}: {e}")
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        return False


def remove_comments(path):
    files = frecurs(path)

    if not files:
        print("Файлы .docx не найдены.")
        return

    success = 0
    for f in files:
        print(f"  → {f}")
        if _remove_comments_from_file(f):
            success += 1

    print(f"✅ Готово. Обработано файлов: {success}/{len(files)}")