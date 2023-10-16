import yaml

filename = 'sachin.yaml'

with open(filename) as f:
    data = yaml.load(f, loader=yaml.FullLoader)

    for keys, values in data.items():
        print(keys, "---->", values, "---->", type(values))