import re
import os

def get_data():
    path = input("Enter file path: ")
    
    while not (os.path.isfile(path) and path.endswith(".html")):
        print("Not a valid path!")
        path = input("Enter file path: ")
    
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

def main():
    data = get_data()
    seats = re.findall(r'data-component="svg__seat"[^(class)]*class="[^"]*"', data)
    
    is_unavailable = 0
    is_available = 0
    is_resale = 0

    for seat in seats:
        if "is-resale" in seat:
            is_resale += 1
        elif "is-available" in seat:
            is_available += 1
        else:
            is_unavailable += 1

    print("Unavailable:", is_unavailable)
    print("Available:", is_available)
    print("Resale:", is_resale)

if __name__ == "__main__":
    main()