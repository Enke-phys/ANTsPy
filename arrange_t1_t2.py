import os
import shutil

t1_folder = "/Users/enke/Desktop/pix2pix_t1_t2/t1"
t2_folder = "/Users/enke/Desktop/pix2pix_t1_t2/t2"

t1_new = "/Users/enke/Desktop/pix2pix_t1_t2/t1_new"
t2_new = "/Users/enke/Desktop/pix2pix_t1_t2/t2_new"
os.makedirs(t1_new, exist_ok=True)
os.makedirs(t2_new, exist_ok=True)

# Unterordner beider Ordner
t1_subfolders = set([f for f in os.listdir(t1_folder) if os.path.isdir(os.path.join(t1_folder, f))])
t2_subfolders = set([f for f in os.listdir(t2_folder) if os.path.isdir(os.path.join(t2_folder, f))])

# Gemeinsame Unterordner
common_subfolders = t1_subfolders & t2_subfolders
print(f"Gemeinsame Unterordner: {common_subfolders}")

def copy_nii_recursive(src_folder, dst_folder, allowed_subfolders):
    copied_files = []
    for subfolder_name in os.listdir(src_folder):
        if subfolder_name not in allowed_subfolders:
            continue
        full_subfolder = os.path.join(src_folder, subfolder_name)
        # rekursiv alle Dateien durchgehen
        for root, dirs, files in os.walk(full_subfolder):
            for f in files:
                if f.endswith(".nii") or f.endswith(".nii.gz"):
                    src_path = os.path.join(root, f)
                    dst_path = os.path.join(dst_folder, f)
                    shutil.copy2(src_path, dst_path)
                    copied_files.append(f)
    return copied_files

t1_files = copy_nii_recursive(t1_folder, t1_new, common_subfolders)
t2_files = copy_nii_recursive(t2_folder, t2_new, common_subfolders)

print(f"T1 Dateien kopiert: {len(t1_files)}")
print(f"T2 Dateien kopiert: {len(t2_files)}")



