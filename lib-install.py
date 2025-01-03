import json
import os
from pathlib import Path

def installer():
    print('Welcome to Wofi Beats installer!')

    # Define the path to the config directory
    config_dir = Path(__file__).parent / 'config'

    # Ensure the config directory exists
    os.makedirs(config_dir, exist_ok=True)

    # Define path to stations.json
    stations_file = config_dir / 'stations.json'

    # Check if stations.json exists
    if not stations_file.exists():
        try:
            # Create the stations.json file if it doesn't exist
            with open(stations_file, 'w') as f:
                json.dump({}, f, indent=4)  # Initialize it as an empty dictionary
            print('Radio stations file has been created successfully.')
        except Exception as e:
            print(f"Error creating stations.json: {e}")
            return
    else:
        print('Radio stations file already exists.')

    # Automatically set the launcher (wofi by default, but you can use rofi by typing `rofi` in
    # ./config/launcher_config.txt if you want)
    launcher_config_path = config_dir / 'launcher_config.txt'

    if os.path.exists(launcher_config_path):
        with open(launcher_config_path, 'r') as f:
            launcher = f.read().strip().lower()
        if launcher in ['wofi', 'rofi']:
            print(f'Launcher already set to {launcher}.')
        else:
            print('Invalid or empty value in launcher_config.txt. Setting to default (wofi).')
            launcher = 'wofi'
            with open(launcher_config_path, 'w') as f:
                f.write(launcher)
            print(f'You selected {launcher}.')
    else:
        # If the file does not exist, simply set it to default
        launcher = 'wofi'
        with open(launcher_config_path, 'w') as f:
            f.write(launcher)
        print(f'Launcher config file created with default value: {launcher}')

    # Automatically install all libraries
    for filename in os.listdir(config_dir / 'stations'):
        if filename.endswith('.json'):
            lib_name = filename.replace('.json', '').capitalize()

            try:
                with open(config_dir / 'stations' / filename) as f:
                    library_radios = json.load(f)
                with open(stations_file, 'r+') as f:
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
