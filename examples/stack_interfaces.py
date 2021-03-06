"""Identify the interfaces of a stack.

1. Load a stack from a json file
2. Identify the interfaces
3. Export to json
4. Visualise

"""
from math import pi

import compas_assembly

from compas.geometry import Rotation

from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import assembly_transform
from compas_assembly.datastructures import assembly_interfaces_numpy

from compas_assembly.plotter import AssemblyPlotter


# load assembly

assembly = Assembly.from_json(compas_assembly.get('stack.json'))

# identify_interfaces

assembly_interfaces_numpy(assembly)

# export to json

assembly.to_json(compas_assembly.get('stack.json'))

# visualise

R = Rotation.from_axis_and_angle([1.0, 0, 0], -pi / 2)
assembly_transform(assembly, R)

plotter = AssemblyPlotter(assembly, tight=True)

plotter.draw_vertices(text={key: str(key) for key, attr in assembly.vertices(True)})
plotter.draw_edges()
plotter.draw_blocks(
    facecolor={key: '#ff0000' for key in assembly.vertices_where({'is_support': True})}
)
plotter.show()
