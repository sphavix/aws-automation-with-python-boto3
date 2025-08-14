"""The create_shoe function takes a list of materials as input and determine the type of shoe created on those materials"""

def main():
    # Determine the shoe types based on the materials provided
    materials_1 = ['leather', 'rubber']
    materials_2 = ['canvas', 'rubber']
    materials_3 = ['gigig', 'fgfhr',12]

    # Use the create_shoe function and check the result
    shoe_1 = create_shoe(materials_1)
    shoe_2 = create_shoe(materials_2)
    shoe_3 = create_shoe(materials_3)

    shoes = [shoe_1, shoe_2, shoe_3]
    # iterate in the she dictionary and print out result
    for shoe in shoes:
        if shoe['type'] == 'unknown':
            print(f"Unknown shoe type for the given materials: {shoe['materials']}")
        else:
            print(f"Shoe of type {shoe['type']} has been created!")


def create_shoe(materials_list):
    shoe_type = ''

    if 'leather' in materials_list and 'rubber' in materials_list:
        shoe_type = 'Boots'
    elif 'canvas' in materials_list and 'rubber' in materials_list:
        shoe_type = 'Sneakers'
    else:
        shoe_type = 'unknown'

    return {'type': shoe_type, 'materials': materials_list}


if __name__ == '__main__':
    main()