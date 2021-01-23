# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


#TODOS:
#changed the register method to 2.8 style
#


import bpy

bl_info = {
    "name": "Blender Demo Scenes",
    "author": "Markus Bawidamann",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "Info -> Help",
    "description": "Demo scene loader for easy access and benchmarking. It includes 3 scenes: BMW (simple), Pavillon Barcelone (medium) and Classroom (complex). They can easily loaded with just a push of a button, making this ideal for newbie Blender users that just want give Blender a spin and see what it can do with their new shiny GPU or CPU. This can also be used for benchmarking, as these scenes are standardized and do not change. My original intention is that his functionality will become part of Blender Master and be available for all Blender users via the help menu. This addon is a proof of concept and prototype for this. Credits go to: Classroom scene: Christophe Seux, BMW27 Scene: Mike Pan, Pavillon Barcelone: Hamza Cheggour, Claudio Andres and Ludwig Mies van der Rohe",
    "warning": "",
    "wiki_url": "nourlyet.com",
    "tracker_url": "",
    "category": "System"
}

addon_file_path = bpy.utils.user_resource('SCRIPTS', "addons") + "/Blender Demo Scenes/demo_scenes/"


#
# Operators
#

class LOAD_OT_bmw27_scene(bpy.types.Operator):
    bl_idname = "load.bmw27_scene"
    bl_label = "Load BMW Scene (simple)"

    def execute(self, context):
        filename1 = addon_file_path + "BMW27.blend"
        bpy.ops.wm.open_mainfile(filepath=filename1)
        return {'FINISHED'}


class LOAD_OT_pavillon_scene(bpy.types.Operator):
    bl_idname = "load.pavillon_scene"
    bl_label = "Load Pavillon Barcelone Scene (medium)"

    def execute(self, context):
        filename1 = addon_file_path + "pavillon_barcelone_v1.2.blend"
        bpy.ops.wm.open_mainfile(filepath=filename1)
        return {'FINISHED'}


class LOAD_OT_classroom(bpy.types.Operator):
    bl_idname = "load.classroom_scene"
    bl_label = "Load Classroom Scene (complex)"

    def execute(self, context):
        filename1 = addon_file_path + "classroom.blend"
        bpy.ops.wm.open_mainfile(filepath=filename1)
        return {'FINISHED'}


#
# Interface
#

def helpDemoScenes(self, context):
    layout = self.layout

    layout.separator()
    layout.menu("info.help_demoscenes")


class helpDemoScenesMenu(bpy.types.Menu):
    bl_label = 'Demo Scenes'
    bl_idname = 'info.help_demoscenes'

    def draw(self, context):
        layout = self.layout

        layout.operator("load.bmw27_scene")
        layout.operator("load.pavillon_scene")
        layout.operator("load.classroom_scene")


#
#   Registration
#

classes = (LOAD_OT_bmw27_scene,LOAD_OT_classroom, LOAD_OT_pavillon_scene, helpDemoScenesMenu)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
   from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)



if __name__ == "__main__":
    register()

