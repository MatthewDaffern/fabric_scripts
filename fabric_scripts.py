import fabric
# ========================================
# you know that boring list of items you have on your docket and you have to manually configure all of them, well here's your chance for automation!

def config_file_dict_generator():
    switch = True
    config = dict()
    while switch == True:
        key_name = input('what are you configuring? What will this script temporarily store?\n')
        config[key_name] = input('what value should be stored?')
        end_prompt = input('are you done with configuration? Y/N\n')
        if end_prompt == 'Y':
            return config


def get_item_range(config_input):
    """obtains the list of items to configure from a file as a list object
       good for commands and servers/routers"""
    file = open(config_input, 'r+')
    return file.readlines()

def login_operation(object_input, config_file):
    """
    # will use fabric to automate login operations.
    https://docs.fabfile.org/en/1.12.1/api/core/network.html
    """
    connection = fabric.Connection(object_input,config_file['port'], config_file['user'], connect_kwargs={'password': config_file['password']})

