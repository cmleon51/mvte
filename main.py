# Description: Simple python script to move files
# using 'glob' for matching files

import fnmatch
import os
import shutil
import yaml
import time

HOME_FOLDER = os.path.expanduser("~")
CONFIG_FOLDER = HOME_FOLDER + "/.config/mvte"
CONFIG_FILE = CONFIG_FOLDER + "/mvte.yml"
SLEEP = 1


def main():
    if not os.path.exists(CONFIG_FOLDER):
        os.makedirs(CONFIG_FOLDER)
        open(CONFIG_FILE, 'w').close()

    last_config_mtime = None

    while True:
        config_time = os.path.getmtime(CONFIG_FILE)

        if last_config_mtime != config_time:
            last_config_mtime = config_time
            with open(CONFIG_FILE) as file:
                config = yaml.safe_load(file)

            if not config:
                print("config file has no content")

        for key, show in config.items():
            file_pattern = show.get("pattern")
            folder_src = (show.get("src"))
            folder_destination = (
                show.get("destination"))

            missing_keys = []
            if (folder_src is None):
                missing_keys += ["src"]
            if (folder_destination is None):
                missing_keys += ["destination"]
            if (file_pattern is None):
                missing_keys += ["pattern"]

            if missing_keys:
                print("The show ", key, " misses keys:", missing_keys)
                continue
            else:
                folder_src = os.path.expanduser(folder_src)
                folder_destination = os.path.expanduser(folder_destination)

            if os.path.exists(folder_src):
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)

                files_in_src = os.listdir(folder_src)

                files_with_starter = [
                    file for file in files_in_src
                    if fnmatch.fnmatch(file, file_pattern)
                ]

                for file in files_with_starter:
                    source = os.path.join(folder_src, file)
                    destination = os.path.join(
                        folder_destination, file)
                    shutil.move(source, destination)
                    print("Moved:", file)
            else:
                print("Cannot take files from a src folder that doesn't exist")
        time.sleep(SLEEP)


if __name__ == "__main__":
    main()
