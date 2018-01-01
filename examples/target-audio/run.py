import shutil
import sys
from os.path import join


if __name__ == '__main__':
    target_folder = sys.argv[1]
    path = join(target_folder, 'horse.ogg')
    shutil.copy('horse.ogg', path)
    print('h_audio_path = %s' % path)
