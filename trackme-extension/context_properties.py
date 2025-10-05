import bpy


class ContextProperties(bpy.types.PropertyGroup):
    """
    Context of the extension, allows to share data
    """

    prev_timestamp: bpy.props.IntProperty(
        name="Previous timestamp",
        description="The timestemp of the previous project save, stored as String",
        default=0
    )

    total_time: bpy.props.IntProperty(
        name="Total Time (sec)",
        description="Total accumulated time in seconds, calculated on file save",
        default=0
    )
