import ezdxf
from synth_mapping_helper.synth_format import wall_to_synth
import numpy as np
import json


def wall_time(n, bpm):
    # unused, breaks at higher BPM. Looks like times need to be at least 1 apart.
    '''
    Generate a list of 1/64th spaced times for stacking a pile of walls.

    :n: int number of walls
    :bpm: song bpm
    :return: list of "time" positions for walls
    '''
    return [i * 93.75 / bpm for i in range(n)]


def synth_json_template(bpm, lenght):
    '''
    Base template for Synth Riders json copy/paste in the editor.
    Sets start measure to 0 and start time to 0.

    :bpm: song bpm
    :lenght: song length in milliseconds
    :return: json skeleton for map
    '''
    template = {
        "BPM": bpm,
        "startMeasure": 0,
        "startTime": 0,
        "lenght": lenght,
        "notes": {},
        "effects": [],
        "jumps": [],
        "crouchs": [],
        "squares": [],
        "triangles": [],
        "slides": [],
        "lights": [],
    }

    return template


def read_dxf_walls(file_path):
    '''
    Read in the dxf file and convert to a list of walls

    :param file_path: path to dxf file
    :return: list of dicts containing wall type and json details
    '''
    walls_labels = []

    try:
        # Read the DXF file
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()

        # Search for all block references in the modelspace
        block_refs = msp.query('INSERT')

        for block_ref in block_refs:
            # Get the name of the block
            name = block_ref.dxf.name
            # Get the insertion point (coordinates) of the block
            coord = list(block_ref.dxf.insert)
            # Get the rotation of the block
            rotation = block_ref.dxf.rotation

            match name:
                case "TRIANGLE":
                    slide_type = 102
                case "SQUARE":
                    slide_type = 101
                case "CENTER":
                    slide_type = 3
                case "ANGLE_RIGHT":
                    slide_type = 2
                case "ANGLE_LEFT":
                    slide_type = 4
                case "LEFT":
                    slide_type = 1
                case "RIGHT":
                    slide_type = 0
                case "CROUCH":
                    slide_type = 100

            wall_vector = np.array([[coord[0], coord[1], 0, slide_type, rotation]])

            # bpm doesn't matter here, we'll replace the timing later
            dest_list, wall_dict = wall_to_synth(100, wall_vector)

            # coord_s, rotation_s = dxf_to_synth(name, coord, rotation)
            walls_labels.append({"dest_list": dest_list, "wall": wall_dict})

        return walls_labels

    except IOError:
        print(f"Could not read {file_path}.")
    except ezdxf.DXFStructureError:
        print(f"Invalid or corrupted DXF file: {file_path}.")


def convert_file(file_path, bpm, lenght=10000):
    '''
    Create json output compatible with the editor

    :param file_path: path to dxf file
    :param bpm: bpm setting in the beatmap
    :param lenght: the lenght setting from your map json, probably optional
    :return: string of Synth Riders formatted json
    '''
    base_json = synth_json_template(bpm, lenght)

    walls_list = read_dxf_walls(file_path)

    num_walls = len(walls_list)

    for i in range(num_walls):
        dest_list = walls_list[i]["dest_list"]
        wall = walls_list[i]["wall"]
        # fix time for each wall, these were set to zero when they were created
        wall["time"] = i
        wall["position"][2] = i * 18.75 / bpm
        base_json[dest_list].append(wall)

    return json.dumps(base_json)
