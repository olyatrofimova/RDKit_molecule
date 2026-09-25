import os
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import Draw

smiles = [
    'CCO',  # этанол
    'CC(=O)Oc1ccccc1C(=O)O',    # аспирин
    'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'  # кофеин
]

os.makedirs('outputs', exist_ok=True)

for s in smiles:
    print(f"\n=== {s} ===")

    # чтение SMILES
    mol = Chem.MolFromSmiles(s)
    if mol is None:
        print('Invalid SMILES')
        continue

    # построение молекулярного графа
    for atom in mol.GetAtoms():
        print(atom.GetIdx(), atom.GetSymbol(), atom.GetDegree())
    for bond in mol.GetBonds():
        print(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx(), bond.GetBondType())

    # расчет дескрипторов
    mw = Descriptors.MolWt(mol)    # Molecular weight - молекулярная масса
    logp = Descriptors.MolLogP(mol)    # LogP - коэфф. распределения октанол/вода (липофильность)
    tpsa = Descriptors.TPSA(mol)    # Topological Polar Surface Area - топологическая полярная площадь поверхности

    print(f"MW={mw:.2f}, LogP={logp:.2f}, TPSA={tpsa:.2f}")

    # генерация ECFP-фингерпринта
    morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    fp = morgan_gen.GetFingerprint(mol)
    print("Длина фингерпринта:", fp.GetNumBits())
    print("Число единичных битов:", fp.GetNumOnBits())

    # визуализация молекулы
    name = s.replace('=', '').replace('(', '').replace(')', '')
    name = name.replace('#', '').replace('1', '').replace('2', '').replace('3', '')

    img = Draw.MolToImage(mol, size=(400, 300))
    img.save(f"outputs/{name}.png")

    svg = Draw.MolToSVG(mol, size=(400, 300))
    with open(f"outputs/{name}.svg", "w") as f:
        f.write(svg)
