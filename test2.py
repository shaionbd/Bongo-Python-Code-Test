"""
2) Write a new function with same functionality from Question 1, but it should be able to handle a Python object
in addition to a dictionary from Question 1.

person_a = Person("User", "1", none) person_b = Person("User", "2", person_a)

a = {
"key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b, } },
}

Sample Output:

key1 1
key2 1
key3 2
key4 2
key5 3
user: 3
first_name: 4
last_name: 4
father: 4
first_name: 5
last_name: 5
father: 5

def print_depth(data): # Write function body

You may write additional function.
"""


def isclass(obj):
    """
    Return true if the object is a Person class.
    """
    return isinstance(obj, object)

def depth(data, depth_count, output):
   if not data:
       return output
   for key in data:
       output.append((key, depth_count))
       if type(data[key]) == dict:
           depth(data[key], depth_count + 1, output)
       elif isclass(data[key]):
           try:
               new_data = data[key].__dict__
               depth(new_data, depth_count + 1, output)
           except:
               pass
   return output

def print_depth(data):
    if not data:
        print("data not found")
        print(data)
    else:
        depth_data = depth(data, 1, [])
        sort_data = sorted(depth_data, key=lambda data: data[1])
        for datam in sort_data:
            print(datam[0], datam[1])


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


if __name__ == '__main__':
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
            }
        },
    }
    print_depth(a)