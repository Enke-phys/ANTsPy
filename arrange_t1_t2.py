import os
import shutil
from pathlib import Path

# Base directories
base_dir = "/Users/enke/Desktop/pix2pix_t1_t2"
t1_dir = os.path.join(base_dir, "t1")
t2_dir = os.path.join(base_dir, "t2")

# Output directories
output_t1_dir = os.path.join(base_dir, "t1_new")
output_t2_dir = os.path.join(base_dir, "t2_new")

# Create output directories if they don't exist
os.makedirs(output_t1_dir, exist_ok=True)
os.makedirs(output_t2_dir, exist_ok=True)

def find_nifti_files(root_dir):
    """Find all NIfTI files in subdirectories of root_dir."""
    nifti_files = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.nii') or filename.endswith('.nii.gz'):
                # Extract the folder name (e.g., '3698063' from the path)
                folder_name = os.path.basename(os.path.dirname(dirpath))
                if folder_name not in nifti_files:
                    nifti_files[folder_name] = []
                nifti_files[folder_name].append(os.path.join(dirpath, filename))
    return nifti_files

# Find all NIfTI files in both T1 and T2 directories
t1_files = find_nifti_files(t1_dir)
t2_files = find_nifti_files(t2_dir)

# Find common folder names that exist in both T1 and T2
common_folders = set(t1_files.keys()) & set(t2_files.keys())

# Process each pair
for folder in common_folders:
    # Get the first NIfTI file from each folder (assuming one per folder)
    if t1_files[folder] and t2_files[folder]:
        t1_path = t1_files[folder][0]  # Take first file if multiple
        t2_path = t2_files[folder][0]  # Take first file if multiple
        
        # Create new filenames
        t1_new_name = f"t1_{folder}.nii.gz"
        t2_new_name = f"t2_{folder}.nii.gz"
        
        # Copy files to new directories with consistent naming
        shutil.copy2(t1_path, os.path.join(output_t1_dir, t1_new_name))
        shutil.copy2(t2_path, os.path.join(output_t2_dir, t2_new_name))
        
        print(f"Processed pair: {t1_new_name} <-> {t2_new_name}")

print("\nProcessing complete!")
print(f"Found {len(common_folders)} matching T1-T2 pairs.")
print(f"T1 files saved to: {output_t1_dir}")
print(f"T2 files saved to: {output_t2_dir}")



