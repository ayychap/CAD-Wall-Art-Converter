# CAD-Wall-Art-Converter
Conversion tool for Synth Riders wall art generated in .dxf CAD files

CAD template by Marinus

# Wall Art Creation
See [Synth_Riders_walls.dxf](/templates/Synth_Riders_Walls.dxf) for wall templates

You can use [nanoCAD](https://nanocad.com/) or other CAD software to create your own wall art and save as .dxf.

# Synth Riders Converter

Use one of the following to convert your file into json for the beatmap editor.

## Use in a browser
[Colab Notebook](https://colab.research.google.com/drive/1qQW4W1nLlRu8x-rEsvdQzzOKismIBz6t): run in a web browser, no installation required.

## Command line
Advanced users! 

You'll need to be a little comfortable running Python and pip (or another option like conda.) This isn't a nice friendly 
installer.

1. Make a local copy of this repository, you can download the zip file if you don't have Git installed.
2. You can make a virtual environment using `environment.yml` or `requirements.txt`, or install the required packages in your base environment if you don't use virtual environments.
3. Go to whatever directory you copied the repository into and run `python command_line.py your_file_path.dxf your_bpm`, where your_file_path is the path to your dxf file, and your_bpm is the bpm you have set in the beatmap editor.
4. You can copy the json output from the command line, or go to the folder containing your dxf file to open up the saved json file.

After you have it set up, you can repeat steps 3 and 4 to make more wall art!