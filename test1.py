"""
1) Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth.

Sample Input:

a = {
“key1”: 1, “”key2”: { “key3”: 1, “key4”: { “key5”: 4 } }
}

Sample Output:

key1 1 key2 1 key3 2 key4 2 key5 3

def print_depth(data): # Write function body
"""


def depth(data, depth_count, output):
   if not data:
       return output
   for key in data:
       output.append((key, depth_count))
       if type(data[key]) == dict:
           depth(data[key], depth_count + 1, output)
   return output

def print_depth(data):
    if not data:
        print("data not found")
        print(data)
    else:
        depth_data = depth(data, 1, [])
        sort_data = sorted(depth_data, key=lambda data: data[1])
        print(sort_data)
        for datam in sort_data:
            print(datam[0], datam[1])

if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 2,
            "key4": {
                "key5": 4,
                "key6": 4,
                "key7":{
                    "key8": 5
                }
            },
            "key9": 2
        }
    }
    print_depth(a)