import bpy


class UiPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Track Me"
    bl_idname = "OBJECT_PT_Annotation"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"
    bl_options = {'HIDE_HEADER'}

    def draw(self, context):
        layout = self.layout
        props = context.scene.custom_properties

        total_seconds = props.total_time
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        row = layout.row()
        row.label(text=f"Total Time Spent: {hours:02d}:{minutes:02d}:{seconds:02d}")
