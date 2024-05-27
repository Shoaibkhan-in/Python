import bpy

# Create a new scene
scene = bpy.context.scene

# Create a new object
lamp = bpy.ops.object.lamp_add(type='POINT', location=(0, 0, 0))

# Create a new material
material = bpy.data.materials.new(name="Lamp Material")
material.diffuse_color = (1, 1, 1)
lamp.data.materials.append(material)

# Create a new animation
animation = bpy.ops.object.animation_add(type='ROTATE', axis=(0, 1, 0), location=(0, 0, 0))

# Set the animation keyframes
animation.keyframes[0].value = 0
animation.keyframes[1].value = 360
animation.keyframes[1].time = 100

# Play the animation
bpy.ops.screen.animation_play()
