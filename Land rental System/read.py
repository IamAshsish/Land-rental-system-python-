
def available_land(file_path):
    lands = []
    with open(file_path, "r") as file:
        for line in file:
            land_info = line.strip().split(',')
            lands.append({
                'kitta_number': int(land_info[0]),
                'city': land_info[1],
                'direction': land_info[2],
                'area': int(land_info[3]),
                'price': int(land_info[4]),
                'status': land_info[5]
            })
    
        return lands
            
    