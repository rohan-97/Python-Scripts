import os
from pathlib import Path
import notify2

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif",".ico", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx", ".sql"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip", ".tgz"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "ARDUINO-FILES": [".ino"],
    "EXE": [".exe"],
    "SCRIPTS": [".js"],
    "SHELL": [".sh"]
}

my_dirs = [
           "/home/rohan/Documents/",
           "/home/rohan/Downloads/",
           "/home/rohan/Downloads/Kachra"
           ]

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


def organize_junk(dd):
    fatherpath = Path(dd)
    # print("fatherpath:" + str(fatherpath.absolute()))

    for entry in os.scandir(dd):
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        file_name = file_path.stem.title()  # os.path.splitext(os.path.basename(dd+file_path.name.title()))[0]
        # print("file_path:" + str(file_path))
        # print("filename:" + file_name)
        # print("fileformat:" + file_format)

        if file_format in FILE_FORMATS:
            # print("FolderName:" + FILE_FORMATS[file_format])
            directory_path = fatherpath.joinpath(Path(FILE_FORMATS[file_format]))
            # print("directorypath:" + str(directory_path.absolute()))

            # directory_path = dd + str(directory_path)
            if "bill" in file_name.lower():
                directory_path = fatherpath.joinpath(Path("BILLS"))
            directory_path.mkdir(exist_ok=True)
            # print("comparison:" + str(directory_path.joinpath(file_path).absolute()))
            if os.path.exists(str(directory_path.joinpath(file_path).absolute())):
                dirs = str(directory_path.joinpath(file_path).absolute())
                ver = 0
                while os.path.exists(dirs):
                    dirs = str(directory_path.absolute()) + "/" + file_name + "(" + str(ver) + ")" + file_format
                    # print("dir is: " + dirs)
                    ver = ver + 1
                # print("os rename arguments: " + str(fatherpath.absolute()) + "/" + str(file_path) + "," + dirs)
                os.rename(str(fatherpath.absolute()) + "/" + str(file_path), dirs)
                # file_path.rename(dirs)
            else:
                # print("os rename arguments: " + str(fatherpath.absolute()) + "/" + str(file_path) + " , " +
                #       str(directory_path.absolute()) + "/" + file_name)
                os.rename(str(fatherpath.absolute()) + "/" + str(file_path),
                          str(directory_path.absolute()) + "/" + file_name + file_format)
                # file_path.rename(directory_path.joinpath(file_path))
            notify2.init("foo")
            msg = notify2.Notification("Moving file '" + file_name + "'",str(fatherpath.absolute()) + "/" + str(file_path) + "\n to \n" +str(directory_path.absolute()) + "/" + file_name + file_format)
            msg.show()

    try:
        os.mkdir("OTHER-FILES")
    except:
        pass

    for dir in os.scandir(dd):
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/OTHER-FILES/' + str(Path(dir)))
        except:
            pass


if __name__ == "__main__":
    for dir in my_dirs:
        organize_junk(dir)
    print("zala kaam...")
