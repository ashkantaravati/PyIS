import json

def to_list_of_dicts(obj):
    new_list = []
    for item in obj:
        dict_obj = vars(item)
        new_list.append(dict_obj)
    return new_list

def object_list_to_json(object_list):

    friendly = to_list_of_dicts(object_list)
    jsonified = json.dumps(friendly)
    return jsonified


def map_json_to_obj(json_data, model_class, name=''):
    dict_list = json_to_object_list(name)
    object_list = []
    for item in dict_list:
        # Still Hardcoded
        fname = item['first_name']
        lname = item['last_name']
        p = model_class(fname, lname)
        object_list.append(p)

    return object_list

def json_to_object_list(buffer,name=''):
    pythonified = json.loads(buffer)
    
    return pythonified