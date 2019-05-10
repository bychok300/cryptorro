import os


class FileUtils(object):

    @staticmethod
    def recursiv_list_files_in(root_folder):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(root_folder):
            for file in f:
                files.append(os.path.join(r, file))

        for f in files:
            print(f)
        return files

    @staticmethod
    def replace_file_content(file, text):
        f = open(file, 'w+')
        f.write(text)

    @staticmethod
    def read_file(file):
        f = open(file)
        return f.read()
