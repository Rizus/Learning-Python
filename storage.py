import os
import json
import tempfile
import argparse


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def check():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        val_data = f.read()
        if val_data:
            return json.loads(val_data)
        return{}


def p_key_val(key, value):
    data = check()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = check()

    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help='key_name')
    parser.add_argument("-v", "--val", help='value')
    args = parser.parse_args()

if args.key and args.val:
    p_key_val(args.key, args.val)
elif args.key:
    print(get(args.key))
else:
    pass
