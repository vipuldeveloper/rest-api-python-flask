from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
        
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "vipul", "age": 31},
    {"name": "vaibhav", "age": 29},
    {"name": "Kavar", "age": 32},
]

def get_friend_name(friend: str):
    return friend["name"]

try:
    #print(search(friends, "vipul", get_friend_name))
    #print(search(friends, "vipul", lambda friend: friend['name']))
    print(search(friends, "vipul", itemgetter("name")))
except RuntimeError as e:
    print(e)