from json_codec import object_list_to_json, map_json_to_obj
from io_utils import write_to_file,read_from_file

def save_data(model_class):

    jsonified = object_list_to_json(model_class.data)
    print(jsonified)
    result = write_to_file(jsonified,model_class.entity_verbose_name)
    # I could have passed the whole class
    return result

def load_data(model_class):
    
    jsonified = read_from_file(model_class.entity_verbose_name)

    result = map_json_to_obj(jsonified, model_class)

    return result

class Entity:
    # TODO: data is being shared by derived classes!
    # TODO: put in seperate module
    # base class for models
    # add data
    # remove data
    # put save/load here??
    data = []
    entity_verbose_name = ''
    @classmethod
    def add(cls, obj):
        if isinstance(obj,cls):
            print(isinstance(obj,cls))
            cls.data.append(obj)
    @classmethod
    def show(cls):
        return cls.data

    @classmethod
    def save(cls):
        save_data(cls) 
        # I could pass cls.data instead. what's right anyway?

