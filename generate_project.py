import os
import json

# تحميل الهيكل من JSON
with open("soil_lab_structure.json", "r", encoding="utf-8") as f:
    structure = json.load(f)

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content or "")

# تنفيذ التوليد في المجلد الحالي
create_structure(".", structure)
print("✅ تم إنشاء كل الملفات والمجلدات بنجاح!")
