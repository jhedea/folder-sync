import os
import shutil

# define the master and slave folder paths
master_folder = "/path/to/master/folder"
slave_folder = "/path/to/slave/folder"

# iterate over files and subdirectories in master folder
for root, dirs, files in os.walk(master_folder):
    # get the corresponding slave folder path
    slave_root = root.replace(master_folder, slave_folder, 1)
    # create the corresponding subdirectories in the slave folder if they don't exist
    for directory in dirs:
        slave_directory = os.path.join(slave_root, directory)
        if not os.path.exists(slave_directory):
            os.makedirs(slave_directory)
    # copy files from master to slave folder, overwriting if they already exist
    for file in files:
        master_file = os.path.join(root, file)
        slave_file = os.path.join(slave_root, file)
        shutil.copy2(master_file, slave_file)