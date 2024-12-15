def h5_to_dict(group):
    """Recursively convert HDF5 group to dictionary."""
    result = {}
    for key, item in group.items():
        if isinstance(item, h5py.Group):  # if the item is a group, recursively convert it
            result[key] = h5_to_dict(item)
        else:  # if the item is a dataset, get the data
            result[key] = item[()]
    return result

# Open the H5 file in read mode and convert it to a dictionary
with h5py.File(file_path, 'r') as f:
    data = h5_to_dict(f)
