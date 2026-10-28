"""Pone en minúsculas los nombres de tabla de los modelos SQLAlchemy.
Uso (desde la raíz del repo):  python fix_tablas.py"""
import pathlib, re

carpeta = pathlib.Path("backend/app/models")
total = 0
for archivo in sorted(carpeta.glob("*.py")):
    texto = archivo.read_text(encoding="utf-8")
    nuevo = re.sub(r'(__tablename__ = ")([A-Z_]+)(")', lambda m: m.group(1) + m.group(2).lower() + m.group(3), texto)
    nuevo = re.sub(r'(ForeignKey\(")([A-Z_]+)(\.)', lambda m: m.group(1) + m.group(2).lower() + m.group(3), nuevo)
    if nuevo != texto:
        archivo.write_text(nuevo, encoding="utf-8")
        total += 1
        print("actualizado:", archivo)
print("archivos modificados:", total)