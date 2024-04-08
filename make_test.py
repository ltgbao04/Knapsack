import os
import shutil

if not os.path.exists('test_case'):
    os.makedirs('test_case')

def make_test_case(source_dir, dest_dir):
    for root, dirs, _ in os.walk(source_dir):
        for folder in dirs:
            source_folder_path = os.path.join(root, folder)
            dest_folder_path = source_folder_path.replace(source_dir, dest_dir)
            if not os.path.exists(dest_folder_path):
                os.makedirs(dest_folder_path)
            
            for sub_root, sub_dirs, _ in os.walk(source_folder_path):
                for sub_folder in sub_dirs:
                    source_sub_folder_path = os.path.join(sub_root, sub_folder)
                    dest_sub_folder_path = source_sub_folder_path.replace(source_dir, dest_dir)
                    if not os.path.exists(dest_sub_folder_path):
                        os.makedirs(dest_sub_folder_path)
                    
                    for _, sub2_dirs, _ in os.walk(source_sub_folder_path):
                        for folder in sub2_dirs:
                            folder_path = os.path.join(source_sub_folder_path, folder)
                            dest_folder_path = os.path.join(dest_sub_folder_path, folder)
                            if not os.path.exists(dest_folder_path):
                                os.makedirs(dest_folder_path)
                            for file in os.listdir(folder_path):
                                if file.startswith('s000'):
                                    source_file_path = os.path.join(folder_path, file)
                                    dest_file_path = source_file_path.replace(source_dir, dest_dir)
                                    shutil.copy(source_file_path, dest_file_path)

source_dir = r"./test_case/kplib" # đường dẫn đến các nhóm test case
dest_dir = "test_case"  # đường dẫn đến các test case được trích xuất từ các nhóm test case gốc để tiến hành thực nghiệm

make_test_case(source_dir, dest_dir) 