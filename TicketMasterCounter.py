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

def get_blocked():
    blocked = input("Enter blocked sections seperated by spaces: ")
    return blocked.split(" ")

def get_block_name(block: str):
    data_index = block.find('data-section-name="')
    data_index += len('data-section-name="')

    data = ''

    while block[data_index] != '"':
        data += block[data_index]
        data_index += 1

    return data

def main():
    data = get_data()
    blocked = get_blocked()

    data = data[data.find('<g class="seats">') + len('<g class="seats">'): data.find('<g class="polygons">')]
    blocks = re.split(r'data-component="svg__block"', data)[1:]

    is_unavailable = 0
    is_available = 0
    is_resale = 0

    for block in blocks:
        if get_block_name(block) in blocked:
            continue
        seats = re.findall(r'data-component="svg__seat"[^(class)]*class="[^"]*"', block)

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