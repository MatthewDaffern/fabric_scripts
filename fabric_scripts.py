import fabric
# ========================================
# you know that boring list of items you have on your docket and you have to manually configure all of them, well here's your chance for automation!

def config_file_dict_generator(config_options_input):
    """ takes options as suggestions to build the config dict.
    """
    switch = True
    config = dict()
    while switch == True:
        key_name = input('what are you configuring? What will this script temporarily store?' + 
                         'Please select from the list of options' +
                         config_options_input + 
                         '\n')
        config[key_name] = input('what value should be stored?')
        end_prompt = input('are you done with configuration? Y/N\n')
        if end_prompt == 'Y':
            return config


def get_item_range(config_input):
    """obtains the list of items to configure from a file as a list object
       good for commands and servers/routers"""
    file = open(config_input, 'r+')
    return file.readlines()

from fabric.api import *

def env_config(local_user, load_key):
    """using local user for environment instead. more secure due to the reduced shared password."""
    env.local_user=local_user
    env.key_filename=load_key
    return 'environment loaded for your default key and your local_user'


def task_loader():
    # https://docs.fabfile.org/en/1.12.1/usage/env.html
    # I'm currently mixed as to whether or not I should perform declarative and just use it as a fab-file, or run it in python.