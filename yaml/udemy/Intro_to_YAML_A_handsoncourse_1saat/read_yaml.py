import yaml

yaml_file = 'car.yaml'

with open(yaml_file, encoding="utf-8") as file:
    data = yaml.load(file, loader=yaml.FullLoader)

    for keys, values in data.items():
        #key:keyname, value
        print("key: ", keys, "\t value:", values, "\t type:", values)