"""
lanier4@illinois.edu
"""
import os
import json
from inspect import getmembers, isfunction, getsource, signature

conscientious_message = 'USER MISTAKE -- NOT AN ERROR'

def show_conscientious_message():
    """ avoid throwing an error: just show_conscientious_message() """
    print(conscientious_message)

def display_module_functions(imported_module, show_imported_functions=False):
    """ Usage: display_module_functions(any_module) 
    Args:
        imported_module:         an imported python module
        show_imported_functions: default is False - ignore imported functions
        
    """
    ignore_functions_list = ['getmembers', 'isfunction', 'getsource', 'signature']

    functions_list = [o for o in getmembers(imported_module) if isfunction(o[1])]
    source_list = [getsource(o[1]) for o in getmembers(imported_module) if isfunction(o[1])]
    
    if len(source_list) != len(functions_list): return  #       This should not be possible
    
    for list_number in range(len(functions_list)):
        function_tuple = functions_list[list_number]    
        if function_tuple[0] in ignore_functions_list:
            if show_imported_functions == True:
                print('using: %s%s'%(function_tuple[0], signature(function_tuple[1])))
        else:
            source_str = source_list[list_number]
            docs_string = None
            try:
                docs_string = source_str.split('"""')[1]
            except:
                pass

            print('def %s%s'%(function_tuple[0], signature(function_tuple[1])))
            if docs_string is None:
                print('doc_missing\n')
            else:
                print(docs_string,'\n')


def get_pip3_versions_dict():
    """ Usage: get_pip3_versions_dict()
         
    Returns:
        pip3_vd:                pip3 installed versions dictionary
    """
    file_name = 'pip_tst_list.txt'
    pip_str = 'pip3 list &> ' + file_name
    os.system(pip_str)

    pip3_vd = {}
    with open(file_name, 'r') as fh:
        for line in fh:
            n, N = line.split()
            if n[0] == '-' or n == 'Package':
                continue
            pip3_vd[n] = N

    os.remove(file_name)

    return pip3_vd

def read_version_dict_file(versions_file_full_path):
    """ get the installed versions from a version list 
    
    Args:
        versions_file_full_path:    valid path to a text file created with unix command: pip3 list &> ver.txt
        display_version_numbers:    print the output to the command line
        
    Returns:
        actual_version_dict:        python dict of form { package_name: installed_version_number }
    """
    try:
        with open(versions_file_full_path, 'r') as fd:
            package_names_lines = fd.read().splitlines()
    except:
        print(versions_file_full_path, '\nfailed to open\n')
        return None
    
    ignore_name_list = ['Package']
    ignore_version_list = ['-------']
    package_names_dict = {}    
    for line in package_names_lines:
        str_list = line.split()
        package_name = str_list[0]
        package_version = str_list[1]
        if package_name in ignore_name_list or package_version in ignore_version_list:
            continue
            print('skipp', package_name)
        else:
            package_names_dict[package_name] = package_version
            
    return package_names_dict

def get_version_dict(package_names_list, display_version_numbers=True):
    """ get the installed versions from a version list 
    
    Args:
        package_names_list:         a python list of pypi packages
        display_version_numbers:    print the output to the command line
        
    Returns:
        actual_version_dict:        python dict of form { package_name: installed_version_number }
    """
    actual_version_dict = {}
    for lib_in in package_names_list:
        IMPORTED_SUCCESSFULLY = False
        installed_version = '-.--.-'
        try:
            one_module = importlib.import_module(lib_in)
            IMPORTED_SUCCESSFULLY = True
            installed_version = one_module.__version__

        except:
            pass

        if IMPORTED_SUCCESSFULLY == True:
            actual_version_dict[lib_in] = installed_version
        else:
            actual_version_dict[lib_in] = 'Not Found'

        if display_version_numbers == True:
            if IMPORTED_SUCCESSFULLY == True:
                print('%20s:  %s'%(lib_in, installed_version))
            else:
                print('%20s:  %s'%(lib_in, 'Not Found'))

    return actual_version_dict


def display_dictionary(python_dict):
    """ std out formatted display of a python dictionary 
    Args:
        python_dict:    a python dictionary {'name1':'def1', 'name2':'def2',... }
    """
    if not isinstance(python_dict, dict):
        show_conscientious_message()
        print('Input variable is not a python "dict"')
        return
    L = max([len(o) for o in list(python_dict.keys())])
    format_string = '%s%i%s: %s'%('%', L, 's', '%s')
    for key_n, value_n in python_dict.items():
        print(format_string%(key_n, value_n))
        

def dict_file_read(file_name):
    """ read a text file into a python dict - intended for version installation data """
    output_dict = None
    try:
        with open(file_name, 'r') as file:
             output_dict = file.read(json.loads(input_dict))
    except:
        pass
    
    if output_dict is None:
        try:
            output_dict = read_version_dict_file(file_name)
        except:
            print(file_name,'failed to load')
            pass
    
    return output_dict

def dict_write_file(input_dict, file_name='dict_file.txt'):
    """ write a python dict to a text file - intended for version installation data """
    try:
        with open(file_name, 'w') as file:
             file.write(json.dumps(input_dict))
    except:
        print(file_name,'fails to write')
        pass

def read_version_dict_file(versions_file_full_path):
    """ get the installed versions from a version list 
    
    Args:
        versions_file_full_path:    valid path to a text file created with unix command: pip3 list &> ver.txt
        display_version_numbers:    print the output to the command line
        
    Returns:
        actual_version_dict:        python dict of form { package_name: installed_version_number }
    """
    try:
        with open(versions_file_full_path, 'r') as fd:
            package_names_lines = fd.read().splitlines()
    except:
        print(versions_file_full_path, '\nfailed to open\n')
        return None
    
    ignore_name_list = ['Package']
    ignore_version_list = ['-------']
    package_names_dict = {}    
    for line in package_names_lines:
        str_list = line.split()
        package_name = str_list[0]
        package_version = str_list[1]
        if package_name in ignore_name_list or package_version in ignore_version_list:
            continue
            print('skipp', package_name)
        else:
            package_names_dict[package_name] = package_version
            
    return package_names_dict

def get_versions_intallation_dict(required_versions_dict, installed_versions_dict=None):
    """ required versions compare installed versions """
    not_found_message = '--.--.--'
    if installed_versions_dict is None:
        installed_versions_dict = get_pip3_versions_dict()
        
    inst_keys = list(installed_versions_dict.keys())
    comparison_dict = {}
    for req_key, req_ver in required_versions_dict.items():
        if req_key in inst_keys:
            comparison_dict[req_key] = [req_ver, installed_versions_dict[req_key]]
        else:
            comparison_dict[req_key] = [req_ver, not_found_message]
            
    return comparison_dict

def get_installed_differences_dict(required_versions_dict):
    """ returns dict of versions required vs versions installed that are different """
    comparison_dict = get_versions_intallation_dict(required_versions_dict)
    differences_dict = {}
    for package_name, compare_list in comparison_dict.items():
        if compare_list[0] != compare_list[1]:
            differences_dict[package_name] = compare_list
            
    return differences_dict