def find_the_mins(dictionary):
    '''
    Purpose: 
        Find the minumum value in the list of each key.
    Parameters: 
        dictionary: A dictionary with keys that are strings, and the values will be lists of numeric values. 
    Return Value: 
        A new dictionary with the same keys, but only the minimum value for each of the keys.
    '''
    new_dict = {}
    n = 0
    for key in dictionary:
        if dictionary[key] == []:
            continue
        else:
            new_dict[key] = min(dictionary[key])
            n += 1
    return new_dict

def find_the_contact(directory, name, field):
    '''
    Purpose:
        Find the specified field of the name in the directory, if it is not found then add a username for the person into the directory.
    Parameters:
        directory: A dictionary that has a name which is a string, and a field which is also a string.
        name: A string that may be in the directory.
        field: A field that may be in a dictionary associated with the name.
    Return Value:
        If the name and field are in the directory, then returns information. 
        If the name is present but the field is not included, then returns None.
        If the name is not present and the field is Username, then add the first three letters of the name to the directory and return the username.
        If the name is not present and the fieldis not Username, then  add the first three letters of the anem to the directory and return None.

    '''
    if name in directory:
        if field == "Phone" or field == "Email" or field == "Username":
            if field not in directory[name]:
                return None
            return directory[name][field]
    else:
        directory.update({name:{'Username':name[0:3]}})
        if field == 'Username':
            return name[0:3]
        else:
            return None

def create_lists(file_name):
    '''
    Purpose:
        Turn a CSV file into a shopping list.
    Parameters:
        file_name: A CSV file that contains the store, item, and number of items.
    Return Value:
        A dictionary with keys for each store, that contain a dictionary for each item listed for each store.
    '''
    list = {}
    with open(file_name) as fp:
        for line in fp:
            y = line.strip()
            row = y.split(',')
            store = row[0]
            item = row[1]
            num_items = int(row[2])
            if store not in list:
               list[store]  = {}
            if item not in list[store]:
                list[store][item] = 0
            list[store][item] += num_items  
    return list