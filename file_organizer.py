# Cleans up the desktop and download folder by putting everything in a folder named "files" in the Documents directory organised 
# by the file extention.
import os

username = os.getlogin()

paths = ["C:\\Users\\" + username + "\\Desktop\\", 
         "C:\\Users\\" + username + "\\Downloads\\"]

new_path = "C:\\Users\\" + username + "\\Documents\\files\\"

for path in paths:
    for file_name in os.listdir(path):

        init_path = path + file_name
        file_type = os.path.splitext(init_path)[-1]

        # delete shortcuts
        if file_type == ".lnk":
            os.remove(init_path)
        
        else:
            final_root = new_path + file_type + "\\"
            final_path = final_root + file_name

            # Create path if it doesn't exist
            if not os.path.exists(final_root):
                os.makedirs(final_root)         

            else: 
                # Index to rename if already exists in the final path.
                n = 0
                while os.path.exists(final_path):
                    file_path = os.path.splitext(final_root + file_name)
                    n += 1
                    num = " (" + str(n) + ")"
                    final_path = file_path[0] + num + file_path[1]

            try:
                os.rename(init_path, final_path)
            except PermissionError:
                print("\n-> File " + file_name + " is open. Cannot move file.")