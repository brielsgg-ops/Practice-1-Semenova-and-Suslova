```mermaid 
flowchart TD 
Start([Начало работы]) --> InputQ[/Ввод Qж и W с валидацией границ/] 
InputQ --> CheckValid{Значения в пределах\nQж: 0..1000, W: 0..100?} 
CheckValid -- Нет --> ErrMsg[/Вывод ошибки диапазона/] 
ErrMsg --> InputQ 
CheckValid -- Да --> CalcVol[Расчёт объёма нефти:\nQн = Qж * 1 - W/100] 
CalcVol --> CalcMass[Расчёт массы нефти:\nMн = Qн * 850 / 1000] 
CalcMass --> Cond1{Mн < M_min?} 
Cond1 -- Да --> Status1[Статус: Убыточна - стоп] 
    Cond1 -- Нет --> Cond2{Mн < 3 * M_min?} 
    Cond2 -- Да --> Status2[Статус: Рентабельна - база] 
    Cond2 -- Нет --> Status3[Статус: Высокодебитная - приоритет] 
    Status1 --> Output[/Вывод сводки: Qн, Mн, Статус/] 
    Status2 --> Output 
    Status3 --> Output 
    Output --> End([Конец работы])
