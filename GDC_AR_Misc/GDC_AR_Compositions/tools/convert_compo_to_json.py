import re
import json

def parse_vector(coords):
    # Convertit une chaîne "x y z" en liste de float
    return [float(v) for v in coords.strip().split()]

def parse_rotation(props):
    # Cherche angleX, angleY, angleZ dans les propriétés, retourne [x, y, z]
    rx = float(props.get('angleX', 0))
    ry = float(props.get('angleY', 0))
    rz = float(props.get('angleZ', 0))
    return [rx, ry, rz]

def extract_entities(text):
    entities = []
    # Regex pour matcher GenericEntity ou $grp GenericEntity ou $grp StaticModelEntity
    entity_pattern = re.compile(
        r'(?:\$grp\s+)?(?P<type>GenericEntity|StaticModelEntity)\s*:\s*"(?P<prefab>[^"]+)"\s*\{(.*?)\}',
        re.DOTALL
    )
    # Regex pour matcher les sous-blocs dans $grp
    subblock_pattern = re.compile(r'\{(.*?)\}', re.DOTALL)
    # Regex pour extraire les propriétés
    prop_pattern = re.compile(r'(\w+)\s+([^\{\}\n]+)')

    for match in entity_pattern.finditer(text):
        prefab = match.group('prefab')
        block = match.group(3)
        if match.group(0).startswith('$grp'):
            # Plusieurs entités dans le bloc
            for sub in subblock_pattern.finditer(block):
                props = dict(prop_pattern.findall(sub.group(1)))
                if 'coords' not in props:
                    continue
                entity = {
                    "m_Resource": prefab,
                    "m_Position": parse_vector(props['coords']),
                    "m_Rotation": parse_rotation(props)
                }
                entities.append(entity)
        else:
            props = dict(prop_pattern.findall(block))
            if 'coords' not in props:
                continue
            entity = {
                "m_Resource": prefab,
                "m_Position": parse_vector(props['coords']),
                "m_Rotation": parse_rotation(props)
            }
            entities.append(entity)
    return entities

if __name__ == "__main__":
    # Remplace ce chemin par le tien
    with open("GDC_TestCompo_S_USSR.et", encoding="utf-8") as f:
        text = f.read()

    entities = extract_entities(text)
    print(json.dumps(entities, indent=2))