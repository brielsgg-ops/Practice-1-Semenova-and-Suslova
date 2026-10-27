"""Спецификации функций модуля оценки рентабельности скважины (Вариант А). 
 
Практическое занятие № 1. Выполнено в паре. 
""" 
 
OIL_DENSITY: float=850.0 # кг/м³ 
M_MIN_THRESHOLD: float=8.0+0.5*((28+30)%10)

def read_valid_param(prompt: str, min_val: float, max_val: float) -> float: 
    pass 
 
 
def calc_oil_volume(q_liq: float, w_pct: float) -> float: 
    return q_liq*(1-w_pct/100.0)
 
 
def calc_oil_mass(q_oil: float, density: float = OIL_DENSITY) -> float: 
    return q_oil*density/1000.0
 
def evaluate_profitability(m_oil: float, m_min: float=M_MIN_THRESHOLD, w_pct: float=0.0) -> str: 
    """Определяет категорию рентабельности скважины по массовому дебиту нефти. 
    """ 
    if w_pct==100.0:
        return "Чистая вода (авария)"
    if m_oil<m_min: 
        return "Убыточна (стоп)" 
    elif m_oil<3*m_min: 
        return "Рентабельна (база)" 
    else: 
        return "Высокодебитная (приоритет)" 
 
 
if __name__ == "__main__": 
    print("ПРОВЕРКА СПЕЦИФИКАЦИЙ МОДУЛЯ (Вариант А)") 
    print("=" * 45) 

    test_q_liq=50+3*((28+30)%25)
    test_w=15+2*((28+30)%35)

    q_oil=calc_oil_volume(test_q_liq, test_w)
    m_oil=calc_oil_mass(q_oil)

    print(f"Входные данные Qж = {test_q_liq} м^3/сут, W = {test_w}%, M_min = {M_MIN_THRESHOLD} т/сут")
    print(f"Расчётный объёмный дебит Qн = {q_oil:.2f} т/сут")
    print(f"Расчётный массовый дебит Мн = {m_oil:.2f} т/сут")

    status = evaluate_profitability(m_oil, w_pct=test_w) 

    print(f"Статус: {status}")
    print("-" * 45)
    print("Прогноз аналитика: Рентабельна (база)")
    print(f"Факт программы: {status}")

