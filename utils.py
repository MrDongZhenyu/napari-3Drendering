import napari_bbox
import numpy as np
import matplotlib.cm as cm

# Plot cross sections (X-Y,X-Z,Y-Z views)
def add_crosssection_layer(viewer,vol,vol_scale,axis,pos,color,width):
    # pos is in pixels
    if axis == 0:
        pos = pos*vol_scale[0]
        bbox = [pos, 0, 0, pos, vol.shape[1]*vol_scale[1]-1, vol.shape[2]*vol_scale[2]-1] # xy plane
        layer_name = 'XY plane'
    elif axis == 1:
        pos = pos*vol_scale[1]
        bbox = [0, pos, 0, vol.shape[0]*vol_scale[0]-1, pos, vol.shape[2]*vol_scale[2]-1]
        layer_name = 'XZ plane'
    elif axis == 2:
        pos = pos*vol_scale[2]
        bbox = [0, 0, pos, vol.shape[0]*vol_scale[0]-1, vol.shape[1]*vol_scale[1]-1, pos]
        layer_name = 'YZ plane'

    # Get vertices from bounding box
    all_vertices = np.array([
        [bbox[0], bbox[1], bbox[2]],
        [bbox[0], bbox[1], bbox[5]],
        [bbox[0], bbox[4], bbox[5]],
        [bbox[0], bbox[4], bbox[2]],
        [bbox[3], bbox[1], bbox[2]],
        [bbox[3], bbox[1], bbox[5]],
        [bbox[3], bbox[4], bbox[5]],
        [bbox[3], bbox[4], bbox[2]]
    ]).squeeze()

    bb_layer = napari_bbox.BoundingBoxLayer(ndim=3, edge_color=color,edge_width=width,name=layer_name)
    bb_layer.add(all_vertices)
    viewer.add_layer(bb_layer)

# Add alpha (transparancy) function to matplotlib default colormaps
# You can design your alpha function inside, for example linear, or other shapes
def Selectcolormap(name):
    # get default colormap from matplotlib
    # name can be 'jet', 'inferno' etc.
    cmap = cm.get_cmap(name, 256)  # get the colormap values
    colormap_array = cmap(np.linspace(0, 1, 256))[:, :3]  # Shape (256, 3)

    alpha_cmp = (np.arange(256)/255).reshape(256,1)
    colormap_array = np.hstack((colormap_array, alpha_cmp))

    color_map = {
        'colors': colormap_array,
        'name': name +'_customize',
        'interpolation': 'linear'
    }

    return color_map
