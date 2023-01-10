# VideoPlaylistGenerator

This is a python script that generates a VLC-compatible XML playlist from all the video files present in the current working directory and its subdirectories.

## Features

-   The script checks for files with the following extensions: `.mp4`, `.mkv`, `.avi`, `.flv`, `.mov`, `.wmv`, `.vob`, '.mpg','.3gp', '.m4v'
-   If set to true, the script checks for files in the current working directory and all its subdirectories.
-   The script can edit the file paths to be compatible with VLC player.

## Requirements

-   python 3
-   xml.etree.ElementTree
-   os
-   re

## Usage

1. Clone the repository

```bash
git clone https://github.com/ElhabibTOUAOUA/VideoPlaylistGenerator.git
```

2. Make sure the required python modules are installed.
   pip install xml.etree.ElementTree os re

3. Navigate to the folder where the script is located in your computer
4. Run the script

```python
VideoPlaylistGenerator.py
```

5. The generated playlist.xml file will be located in the same directory as the script

## Customization

The script contains a variable check_subdirectories which is set to False by default. Set it to True to check for files in the current working directory and all its subdirectories.

```python
check_subdirectories = True
```

You can also change the default folder name where the .xml file should be exported by modifying the last line of the script

```python
self.tree.write('playlist.xml')
```

to the desired path

```python
self.tree.write('[your_folder_path]/playlist.xml')
```

Also the default title of the generated xml file can be changed by modifying the line

```python
self.title.text = 'Playlist'
```

to any desired value

The script also contains a list VIDEOS_EXTENSIONS to specify which video file types should be included in the playlist, you can add or remove from this list as you prefer.

You can also modify the script to allow user input the path to the directory they want the script to search for videos and the location they want the generated xml file to be written to.
