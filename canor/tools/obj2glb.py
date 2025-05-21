import os
import trimesh


mesh_dir = 'canor/assets/meshes/example'
mesh_paths = sorted([os.path.join(mesh_dir, f) for f in os.listdir(mesh_dir)])

for mesh_path in mesh_paths:
    target_path = mesh_path.replace('.obj', '.glb')
    trimesh.load(mesh_path).export(target_path)

print('Done')
