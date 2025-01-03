import json
import os

def installer():
    print('Welcome to Rofe/Wofi Beats installer!')
    os.makedirs('./config/stations', exist_ok=True)
    open('./config/stations.json', 'a').close()
    print('Radio stations file has been created successfully.')

    while True:
        choice = input('Do you want to use wofi or rofi? (Default is wofi)\n')
        if choice == '' or choice.lower() == 'wofi':
            with open('./config/launcher_config.txt', 'w') as f:
                f.write("wofi")
            print('You selected wofi.')
            break
        elif choice.lower() == 'rofi':
            with open('./config/launcher_config.txt', 'w') as f:
                f.write("rofi")
            print('You selected rofi.')
            break
        else:
            print('Invalid input. Please choose either "wofi" or "rofi".')

    # Inherit stations from Rofi-Beats-Linux
    while True:
        choice = input('Do you want to install default stations (inherited from Rofi-Beats-Linux by pfitzn)? (y/n)\n')
        if choice.lower() == 'y':
            try:
                with open('./config/stations/default-stations.json') as f:
                    radios = json.load(f)
                with open('./config/stations.json', 'w') as f:
                    json.dump(radios, f, indent=4)
                print('Default stations have been installed successfully.')
            except FileNotFoundError:
                print('Default stations file not found!')
            break
        elif choice.lower() == 'n':
            print('You chose not to install default stations.')
            break
        else:
            print('Invalid input. Please choose "y" or "n".')

    # Additional libraries
    for filename in os.listdir('./config/stations'):
        if filename.endswith('.json') and filename != 'default-stations.json':
            lib_name = filename.replace('.json', '').capitalize()
            while True:
                choice = input(f'Do you want to install the "{lib_name}" library? (y/n)\n')
                if choice.lower() == 'y':
                    try:
                        with open(f'./config/stations/{filename}') as f:
                            library_radios = json.load(f)
                        with open('./config/stations.json', 'r+') as f:
                            try:
                                existing_stations = json.load(f)
                            except json.JSONDecodeError:
                                existing_stations = {}
                            existing_stations.update(library_radios)
                            f.seek(0)
                            json.dump(existing_stations, f, indent=4)
                        print(f'The "{lib_name}" library has been added successfully.')
                    except FileNotFoundError:
                        print(f'The file {filename} was not found!')
                    break
                elif choice.lower() == 'n':
                    print(f'You chose not to install the "{lib_name}" library.')
                    break
                else:
                    print('Invalid input. Please choose "y" or "n".')

if __name__ == "__main__":
    installer()
