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

=== CN1C=NC2=C1C(=O)N(C(=O)N2C)C ===
0 C 1
1 N 3
2 C 2
3 N 2
4 C 3
5 C 3
6 C 3
7 O 1
8 N 3
9 C 3
10 O 1
11 N 3
12 C 1
13 C 1
0 1 SINGLE
1 2 AROMATIC
2 3 AROMATIC
3 4 AROMATIC
4 5 AROMATIC
5 6 AROMATIC
6 7 DOUBLE
6 8 AROMATIC
8 9 AROMATIC
9 10 DOUBLE
9 11 AROMATIC
11 12 SINGLE
8 13 SINGLE
5 1 AROMATIC
11 4 AROMATIC
MW=194.19, LogP=-1.03, TPSA=61.82
Длина фингерпринта: 2048
Число единичных битов: 25

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/9ee79210-f252-42e7-b576-9f5a8d051343" />
