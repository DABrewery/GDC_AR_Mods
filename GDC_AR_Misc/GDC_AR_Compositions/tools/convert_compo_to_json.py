import re
import json
import argparse
import os
import sys

def parse_vector(coords):
    return [float(v) for v in coords.strip().split()]

def parse_rotation(props):
    rx = float(props.get('angleX', 0))
    ry = float(props.get('angleY', 0))
    rz = float(props.get('angleZ', 0))
    return [rx, ry, rz]

def extract_entities_from_block(block):
    entities = []
    entity_pattern = re.compile(
        r'(?P<type>GenericEntity|StaticModelEntity)\s*:\s*"(?P<prefab>[^"]+)"\s*\{', re.DOTALL
    )
    prop_pattern = re.compile(r'(\w+)\s+([^\{\}\n]+)')

    def parse_block(block):
        pos = 0
        while pos < len(block):
            match = entity_pattern.search(block, pos)
            if not match:
                break
            prefab = match.group('prefab')
            start = match.end()
            # Trouver la fin du bloc en équilibrant les accolades
            depth = 1
            i = start
            while i < len(block) and depth > 0:
                if block[i] == '{':
                    depth += 1
                elif block[i] == '}':
                    depth -= 1
                i += 1
            content = block[start:i-1]
            props = dict(prop_pattern.findall(content))
            if 'coords' in props:
                entity = {
                    "resource": prefab,
                    "position": parse_vector(props['coords']),
                    "rotation": parse_rotation(props)
                }
                entities.append(entity)
            # Récursif pour les sous-entités
            parse_block(content)
            pos = i
    parse_block(block)
    return entities

def extract_main_block(text):
    # Trouve le premier bloc principal (la composition)
    main_entity_pattern = re.compile(
        r'(GenericEntity|StaticModelEntity)\s*:\s*"[^"]+"\s*\{', re.DOTALL
    )
    match = main_entity_pattern.search(text)
    if not match:
        return None
    start = match.end()
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    # On extrait le contenu du bloc principal
    return text[start:i-1]

def process_file(filepath, output_dir=None):
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
    main_block = extract_main_block(text)
    if main_block is None:
        print(f"Bloc principal non trouvé dans {filepath}")
        return
    entities = extract_entities_from_block(main_block)
    base = os.path.splitext(os.path.basename(filepath))[0]
    output_name = base + ".json"
    if output_dir:
        output_path = os.path.join(output_dir, output_name)
    else:
        output_path = output_name

    # Vérification de l'existence du fichier
    if os.path.exists(output_path):
        resp = input(f"Le fichier {output_path} existe déjà. Voulez-vous l'écraser ? (o/N) : ")
        if resp.lower() not in ["o", "oui", "y", "yes"]:
            print("Écriture annulée.")
            return

    with open(output_path, "w", encoding="utf-8") as out:
        out.write('"campItems": ')
        json.dump(entities, out, indent=2, ensure_ascii=False)
    print(f"Fichier écrit : {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertit des fichiers de composition Enfusion en JSON.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Fichier unique à parser")
    group.add_argument("-d", "--dir", help="Répertoire contenant les fichiers à parser")
    args = parser.parse_args()

    if args.file:
        process_file(args.file)
    elif args.dir:
        for root, _, files in os.walk(args.dir):
            for file in files:
                if file.endswith(".et"):
                    process_file(os.path.join(root, file), output_dir=args.dir)