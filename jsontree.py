import os
import errno

def path_hierarchy(path):
    hierarchy = {
        'type': 'folder',
        'name': os.path.basename(path),
        'path': path,
    }

    try:
        hierarchy['children'] = [
            path_hierarchy(os.path.join(path, contents))
            for contents in os.listdir(path)
        ]
    except OSError as e:
        if e.errno != errno.ENOTDIR:
            raise
        hierarchy['type'] = 'file'

    return hierarchy

if __name__ == '__main__':
    import json
    import sys

    try:
        directory = sys.argv[1]
    except IndexError:
        directory = "./downloads/"

    print(json.dumps(path_hierarchy(directory), indent=2, sort_keys=True))

    with open('dir.json', 'w',encoding='utf-8') as outfile:
        json.dump(path_hierarchy(directory),outfile, indent=2, sort_keys=True,ensure_ascii = False)