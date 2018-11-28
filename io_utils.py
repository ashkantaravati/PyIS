from config import DATA_DIR

def get_absolute_path(entity_name):
    return DATA_DIR + f'{entity_name}.json'


def write_to_file(buffer,entity_name):
    abs_path = get_absolute_path(entity_name)
    f = open(abs_path, "w")
    result = f.write(buffer)
    return result

def read_from_file(entity_name):
    abs_path = get_absolute_path(entity_name)
    f = open(abs_path, 'r')
    result = f.read()
    return result