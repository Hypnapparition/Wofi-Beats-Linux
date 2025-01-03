import json

def installer():
    print('Welcome to Rofe/Wofi Beats installer!')
    open('./config/stations.json', 'a')
    print('Radio stations file have been created successfully.')

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

    while True:
        choice = input('Do you want to install default stations (inherited from Rofi-Beats-Linux by pfitzn)? (y/n)\n')
        if choice.lower() == 'y':
            try:
                with open('./config/default-stations.json') as f:
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

if __name__ == "__main__":
    installer()
