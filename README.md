# Wofi-Beats-Linux
A Wofi/Rofi menu for playing radio stations on Linux with support of adding a custom stations.

## Dependencies
- wofi [or rofi](#using-rofi-instead-of-wofi)
- mpv
- notify-send
- python3

## Installation

To install `notify-send`, `wofi` and `mpv` enter the following:

For Ubuntu:
```
$ sudo apt install notify-osd mpv wofi
```
For Arch Linux:

```
sudo pacman -S otify-osd mpv wofi
```

[You can use rofi instead of wofi if you want](#using-rofi-instead-of-wofi)



Once you have the dependencies installed, simply execute the file 'wofi-beats-linux.py'.

```
$ git clone https://github.com/Hypnapparition/Wofi-Beats-Linux/
$ cd Wofi-Beats-Linux
$ chmod +x wofi-beats-linux.py
```
Now the script is ready to use
```
python3 wofi-beats-linux.py
```

If you want your launchers to find it, you may want to move it to your bin directory


```
$ mv rofi-beats-linux.py ~/.local/bin/
```


## How libraries work

JSON libraries for radio stations in **Wofi Beats** contain predefined station lists stored as separate `.json` files inside the `config/stations/` directory. These libraries allow users to import curated sets of stations conveniently.

When the script runs, it looks for these `.json` files in the `config/stations/` directory. Each library is structured as a JSON object, where station names are keys, and their values include the following attributes:

- `notification`: The message displayed as a notification when the station is selected.
- `URL`: The streaming URL for the station.

Example of a JSON library file:
```json
{
    "Classic Rock": {
        "notification": "classic Rock ☕️🎶",
        "URL": "https://streaming.live365.com/a06375"
    },
    "Progressive Rock": {
        "notification": "progressive Rock ☕️🎶",
        "URL": "http://eagle.streemlion.com:4040/stream"
    }
}
```

To update libraries after deleting some and updating new ones, delete stations.json in the config directory

By default, in the directory `config/stations/` there are three libraries:
- default (duplicates stations from [Rofi-Beats-Linux](https://github.com/pfitzn/Rofi-Beats-Linux))
- rock.json (some rock and metal stations)
- industrial.json (only dark electro station for now, more are planned to be added later on)

## Usage (Inherited from Rofi-Beats-Linux)

The script toggles the radio on and off depending on it's current state.

The script first checks to see if an instance of the radio is already playing.

If it finds the script is already playing music it kills the music. If the radio is not already playing it will launch the list of stations you can choose from.

The output of the player is piped to a text file that can be read by your applications (to get the title of the song being currently played, for example).

The player is also connected to a socket so that you can controll it externally. For example, you may want to bind a key (or allow your programs) to pause and resume the playing (tip: the command for that will be `echo '{ "command": ["cycle", "pause"] }' | socat - /tmp/mpvsocket` ).

## Using Rofi instead of Wofi

To use `Rofi` instead of `Wofi`, open config/launcher_config.txt in a text editor and replace "wofi" with "rofi".
