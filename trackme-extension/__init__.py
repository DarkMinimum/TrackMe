import bpy

from .handlers import on_file_save, on_scene_open
from .context_properties import ContextProperties
from .ui_panel import UiPanel


def register():
    bpy.app.handlers.save_post.append(on_file_save)
    bpy.app.handlers.load_post.append(on_scene_open)
    bpy.utils.register_class(ContextProperties)
    bpy.types.Scene.custom_properties = bpy.props.PointerProperty(type=ContextProperties)
    bpy.utils.register_class(UiPanel)

    print("🔧 File Save Handler Registered — it will print a message every time you save.")


def unregister():
    bpy.utils.unregister_class(UiPanel)
    del bpy.types.Scene.custom_properties
    bpy.utils.unregister_class(ContextProperties)
    bpy.app.handlers.load_post.clear()
    bpy.app.handlers.save_post.clear()
    print("❌ File Save Handler Unregistered.")


if __name__ == "__main__":
    register()
