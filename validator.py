import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator

BASE_DIR = Path(__file__).parent
SCHEMA_FILE = BASE_DIR / "schema.json"
DEFAULT_DATA = BASE_DIR / "data.json"

def validate(data_path: Path, schema_path: Path) -> bool:
    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
        with open(data_path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"[ERROR] Файл не найден: {e.filename}")
        return False
    except json.JSONDecodeError as e:
        print(f"[ERROR] Некорректный JSON в {data_path.name}: {e}")
        return False

    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))

    if not errors:
        print(f"[OK] {data_path.name}: валидно")
        return True

    print(f"[FAIL] {data_path.name}: найдено ошибок — {len(errors)}")
    for err in errors:
        path = ".".join(map(str, err.path)) or "<root>"
        print(f" • поле '{path}': {err.message}")
    return False


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DATA
    
    ok = validate(target, SCHEMA_FILE)
    sys.exit(0 if ok else 1)