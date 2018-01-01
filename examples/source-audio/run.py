import mutagen
import sys


if __name__ == '__main__':
    target_folder, source_audio_path = sys.argv[1:]
    a = mutagen.File(source_audio_path)
    print('length_in_seconds = %s' % a.info.length)
