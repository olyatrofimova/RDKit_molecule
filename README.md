# RDKit_molecule
SMILES → молекулярный граф → дескрипторы (MW, LogP, TPSA) → ECFP-фингерпринт → визуализация.

## Установка

pip install -r requirements.txt

## Запуск

python rdkit_molecule.py

## Вход

Список SMILES в rdkit_molecule.py:

    smiles = [
        'CCO',                          # этанол
        'CC(=O)Oc1ccccc1C(=O)O',        # аспирин
        'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', # кофеин
    ]

## Выход

В консоль печатаются атомы, связи, дескрипторы и размер фингерпринта.
В папке outputs/ сохраняются png и svg с изображениями молекул.

Пример:

    === CCO ===
    0 C 1
    1 C 2
    2 O 1
    MW=46.07, LogP=-0.00, TPSA=20.23
    Длина фингерпринта: 2048
    Число единичных битов: 3
<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/350041e9-8b97-4c86-86d6-fdd3b34b25d4" />
