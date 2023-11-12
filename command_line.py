from argparse import ArgumentParser
from pathlib import Path
from src.sr_cad_walls.utils import convert_file


def main(inputs):
    json_output = convert_file(inputs.file, inputs.bpm, lenght=inputs.l)

    file_path = Path(inputs.file)
    folder = file_path.parent
    file_name = file_path.stem

    json_file = folder / f"{file_name}.json"

    with open(json_file, "w") as f:
        f.write(json_output)

    print(json_output)


if __name__ == "__main__":
    parser = ArgumentParser(
        description='''Converts dxf files made with Marinus's template into Synth Riders compatible wall art.
        Json file will be stored in the same directory as your dxf file.
        See https://github.com/ayychap/CAD-Wall-Art-Converter for full code and a Colab option that you can run in a browser.'''
    )
    parser.add_argument("file", type=str,
                        help="Path to your .dxf file, your json output will also be saved to this directory")
    parser.add_argument("bpm", type=float, help="BPM setting in the beatmap editor")
    parser.add_argument("-l", metavar="--lenght", type=int, nargs='?', const=10000,
                        help="optional 'lenght' value from your beatmap json, probably not necessary except for extremely large files")

    args = parser.parse_args()

    main(args)
