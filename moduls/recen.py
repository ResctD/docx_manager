import zipfile
import xml.etree.ElementTree as ET


def recenzirovanie(docx_path):
    try:
        with zipfile.ZipFile(docx_path, 'r') as docx_zip:
            with docx_zip.open('word/settings.xml') as settings_file:
                tree =ET.parse(settings_file)
                root_xml = tree.getroot()

                ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                # Поиск режима резензирования:
                if root_xml.find('.//w:trackRevisions', ns) is not None:
                    print(f"✅ Режим резенирования включён")
                    return True
                else:
                    print(f"❌ Режим выключен")
                    return False

    except KeyError:
        print("Нет файла setting.xml - печально")
    except Exception as e:
        print(f" Error {docx_path}: {e}")
        return False
