# zmag2pdf
Python Tool to convert [zmags.com](https://zmags.com) magazines into a local PDF copy

## Why?
I wanted to read a magazine from zmags but I prefer to read it locally, offline in PDF format. Since I got it to work I decided that to might as well share it with others.

If there is demand for it, I will compile the Python code into an executable file for easy usage. [open an issue and let me know]

If by doing this I am infringing on any terms on zmags.com do let me know and I will take this repo down.

## Requirements
- Python 3
- The following Python libraries
  - requests
  - img2pdf
  - os (Included in Python)
  - shutil (Included in Python)

## Usage
First install the required libraries using the command

`pip3 install requests img2pdf`

Edit `zmag2pdf.py` to include the publicationID and resolution desired.
```
# This ID is the string at the end of the publication URL
# For example, for the URL, http://viewer.zmags.com/publication/abcd1234
publicationID = "abcd1234"

# Set desired resolution
# For best resolution, try an arbitrarily high number like 4000x4000
# and the URL will return the highest resolution avaliable.
resolution = "1200x1705"
```

To run the file,

`python3 zmag2pdf.py`

## License
MIT License Copyright (c) 2019
