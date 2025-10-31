import ants
import os

# Pfade zu den Ordnern
t1_folder = "/Users/enke/Desktop/pix2pix_t1_t2/t1_new"
t2_folder = "/Users/enke/Desktop/pix2pix_t1_t2/t2_new"
output_folder = "/Users/enke/Desktop/pix2pix_t1_t2/registered"
os.makedirs(output_folder, exist_ok=True)

# Alle NIfTI Dateien laden und sortieren
t1_files = sorted([os.path.join(t1_folder, f) for f in os.listdir(t1_folder) if f.endswith(".nii") or f.endswith(".nii.gz")])
t2_files = sorted([os.path.join(t2_folder, f) for f in os.listdir(t2_folder) if f.endswith(".nii") or f.endswith(".nii.gz")])

# Registrierung: T1 -> T2 mit SyN
for t1_file, t2_file in zip(t1_files, t2_files):
    t1_img = ants.image_read(t1_file)
    t2_img = ants.image_read(t2_file)
    
    # SyN Registrierung
    reg = ants.registration(fixed=t2_img, moving=t1_img, type_of_transform='SyN')
    t1_registered = reg['warpedmovout']
    
    # Datei speichern
    filename = os.path.basename(t1_file).replace(".nii.gz", "_registered.nii.gz")
    t1_registered.to_file(os.path.join(output_folder, filename))
    
    print(f"{filename} gespeichert")



