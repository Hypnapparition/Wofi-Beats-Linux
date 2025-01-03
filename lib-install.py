import json
import os

def installer():
    print('Welcome to Wofi Beats installer!')
    os.makedirs('./config/stations', exist_ok=True)
    open('./config/stations.json', 'a').close()
    print('Radio stations file has been created successfully.')

    # Automatically set the launcher (wofi by default, but you can use rofi by typing `rofi` in
    # ./config/launcher_config.txt if you want)
    launcher_config_path = './config/launcher_config.txt'

    if os.path.exists(launcher_config_path):
        with open(launcher_config_path, 'r') as f:
            launcher = f.read().strip().lower()
        if launcher in ['wofi', 'rofi']:
            print(f'Launcher already set to {launcher}.')
        else:
            print('Invalid or empty value in launcher_config.txt. Setting to default (wofi).')
            launcher = 'wofi'
            with open(launcher_config_path, 'w') as f:
                f.write(launcher_choice)
            print(f'You selected {launcher_choice}.')
    else:
        # If the file does not exist, simply set it to default
        launcher = 'wofi'
        with open(launcher_config_path, 'w') as f:
            f.write(launcher)

    # Automatically install all libraries
    for filename in os.listdir('./config/stations'):
        if filename.endswith('.json'):
            lib_name = filename.replace('.json', '').capitalize()

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

if __name__ == "__main__":
    installer()
