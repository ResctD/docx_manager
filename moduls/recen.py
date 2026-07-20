import zipfile
import xml.etree.ElementTree as ET

from unittest import result

from engine.recurs import frecurs
from engine import colors

def recenzirovanie(filepath):
    files = frecurs(filepath)
    for filepath in files:
        try:
            with zipfile.ZipFile(filepath, 'r') as docx_zip:
                with docx_zip.open('word/settings.xml') as settings_file:
                    tree = ET.parse(settings_file)
                    root_xml = tree.getroot()

                    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                    # Поиск режима резензирования:
                    if root_xml.find('.//w:trackRevisions', ns) is not None:
                        print(colors.green(f"✅ Режим рецензирования включён {filepath}"))

                    else:
                        print(f"❌ Режим рецензирования выключен {filepath}")


        except KeyError:
            print("Нет файла setting.xml - печально")
        except Exception as e:
            print(f" Error {filepath}: {e}")
            return False
    return result
