from argparse import ArgumentParser
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
import mutagen


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder',
        metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--audio',
        required=True)

    args = argument_parser.parse_args()
    a = mutagen.File(args.audio)
    length = a.info.length
    print('length of audio file is: %f' % length)
