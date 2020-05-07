import bpy
from mathutils import *
from random import randint
D = bpy.data
C = bpy.context

number = 1

for i in range(number):
    x: float = randint(-30, 30)
    y: float = randint(-30, 30)
    z: float = randint(-30, 30)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))


