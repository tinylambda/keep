import pathlib
import os
import shutil
import datetime
import hashlib
from PIL import Image, ExifTags
from filetype.helpers import is_video


class PhotoFlatter:
    TIME_NAME_FORMAT = '%Y%m%d%H%M%S'  # Time information format in filename

    def __init__(self, src_path, dest_path, deduplicate=True):
        self.src_path = pathlib.Path(src_path)
        self.dest_path = pathlib.Path(dest_path)
        self.dest_origin_path = self.dest_path / 'ORIGIN'
        self.dest_non_origin_path = self.dest_path / 'NON_ORIGIN'
        self.dest_video_path = self.dest_path / 'VIDEO'
        self.deduplicate = deduplicate
        self.deduplicate_cache = set()  # store md5 of photos

    def clear_dir(self, the_dir: pathlib.Path):
        for f in the_dir.iterdir():
            if f.is_file():
                f.unlink()
            elif f.is_dir():
                self.clear_dir(f)
                print(f'remove dir {f}')
                f.rmdir()

    def prepare(self):
        if not self.dest_path.exists():
            self.dest_path.mkdir()

        self.clear_dir(self.dest_path)

        self.dest_origin_path.mkdir()
        self.dest_non_origin_path.mkdir()
        self.dest_video_path.mkdir()

    def generate_video_filename(self, path: pathlib.Path):
        path_str = str(path)
        parts = path_str.split(str(self.src_path))
        important_part = parts[1]
        important_parts = important_part.split(os.sep)[1:]

        important_name = '_'.join(important_parts)

        mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
        t = mtime.strftime(self.TIME_NAME_FORMAT)
        filename = f'{t}_{important_name}'

        return filename

    def generate_filename(self, path: pathlib.Path, metadata: dict):
        path_str = str(path)
        parts = path_str.split(str(self.src_path))
        important_part = parts[1]
        important_parts = important_part.split(os.sep)[1:]

        important_name = '_'.join(important_parts)
        t = make = model = None

        origin = False
        if metadata:
            origin = True

        if origin:
            date_time_original = metadata.get('DateTimeOriginal')
            make = metadata.get('Make')
            model = metadata.get('Model')
            if make:
                make = make.strip()
                make = make.replace('\0', '')
            if model:
                model = model.strip()
                model = model.replace('\0', '')

            if date_time_original is None:
                mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
                t = mtime.strftime(self.TIME_NAME_FORMAT)
                print('continue: ', path, metadata)
            else:
                try:
                    _date_time_original = date_time_original[:19]
                    t = datetime.datetime.strptime(_date_time_original, '%Y:%m:%d %H:%M:%S')\
                        .strftime(self.TIME_NAME_FORMAT)
                except ValueError:
                    print('ValueError --->', date_time_original)
                    _date_time_original = date_time_original[:19]
                    t = _date_time_original
            filename = f'{t}_{make}_{model}_{important_name}'
        else:
            mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)
            t = mtime.strftime(self.TIME_NAME_FORMAT)
            filename = f'{t}_{important_name}'
        return filename, origin

    def process(self):
        self.prepare()
        c_ok, c_unidentified, c_permission = 0, 0, 0
        for f in self.src_path.rglob('*'):
            if f.is_dir():
                # will not process directory
                continue

            try:
                img = Image.open(f)
                md5sum = hashlib.md5(img.tobytes()).hexdigest()
                if md5sum not in self.deduplicate_cache:
                    self.deduplicate_cache.add(md5sum)
                else:
                    print('DEDUPLICATED!!!', f)
                    continue
                metadata = {ExifTags.TAGS[k]: v for k, v in img.getexif().items() if k in ExifTags.TAGS}
                filename, origin = self.generate_filename(f, metadata)
                print(f'copy {f} to {self.dest_path}')
                if origin:
                    shutil.copy2(f, self.dest_origin_path / filename)
                else:
                    shutil.copy2(f, self.dest_non_origin_path / filename)
                c_ok += 1
            except Image.UnidentifiedImageError:
                if is_video(str(f)):
                    print(f'copy {f} to {self.dest_video_path}, VIDEO!')
                    video_filename = self.generate_video_filename(f)
                    shutil.copy2(f, self.dest_video_path / video_filename)
                else:
                    c_unidentified += 1
            except Exception as err:
                with open('C:\\Downloads\\copy.log', 'at') as out:
                    out.write(f'ERROR ({err}) WHEN COPYING {str(f)}\n')
                continue


if __name__ == '__main__':
    photo_flatter = PhotoFlatter('C:\\Users\\tinyl\\Pictures\\live',
                                 'C:\\Users\\tinyl\\Pictures\\OLD_PHOTOS')
    photo_flatter.process()

