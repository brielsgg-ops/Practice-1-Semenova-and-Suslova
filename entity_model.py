import json 
from typing import Any 

n=28+30

def build_well_passport() -> dict[str, Any]: 
    return { 
        "well_id": f"W-{100+n}", 
        "depth_m": 1500+50*(n%40), 
        "q_liq": 45+3.5*(n%30), 
        "w_pct": 12+2*(n%35), 
        "is_active": True, 
        "field_name": "Приобское",
        "pump": { 
            "model": "ЭЦН5-80-1800", 
            "power_kw": 40+5*(n%20), 
        }, 
    } 

def save_to_json(data: dict[str, Any], filename: str = "data.json") -> None: 

    with open(filename, "w", encoding="utf-8") as file: 
        json.dump(data, file, ensure_ascii=False, indent=4) 

def load_from_json(filename: str = "data.json") -> dict[str, Any]: 

    with open(filename, "r", encoding="utf-8") as file: 
        return json.load(file) 

def print_passport_summary(passport: dict[str, Any]) -> None: 

    q_oil = passport["q_liq"] * (1.0 - passport["w_pct"] / 100.0) 
    pump_info = passport["pump"] 
    print("=" * 56) 
    print(f"ПАСПОРТ СКВАЖИНЫ ИЗ JSON: {passport['well_id']}") 
    print("=" * 56) 
    print(f"Месторождение: {passport['field_name']}")
    print(f"Глубина: {passport['depth_m']} м") 
    print(f"Дебит жидкости: {passport['q_liq']:.2f} м3/сут (обводнённость {passport['w_pct']:.1f}%)") 
    print(f"Расчёт чистой нефти: {q_oil:.2f} м3/сут")
    print(f"Насосная установка: {pump_info['model']} (мощность {pump_info['power_kw']} кВт)") 
    print("=" * 56) 

if __name__ == "__main__": 
    my_passport = build_well_passport() 

    save_to_json(my_passport, "data.json") 
    print("[OK] Файл 'data.json' успешно записан на диск!") 

    loaded_passport = load_from_json("data.json") 
    assert loaded_passport == my_passport, "Ошибка: прочитанный словарь не совпадает с исходным!" 
    print("[OK] Обратное чтение через json.load() прошло без потерь!") 

    print_passport_summary(loaded_passport)