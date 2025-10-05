import time

import bpy
from bpy.app.handlers import persistent


@persistent
def on_scene_open(dummy):
    scene = bpy.context.scene
    props = scene.custom_properties
    props.prev_timestamp = int(time.time())
    print(f"📂 Scene '{scene.name}' opened at {time.strftime('%Y-%m-%d %H:%M:%S')}")


@persistent
def on_file_save(dummy):
    props = bpy.context.scene.custom_properties
    now = int(time.time())
    diff = now - props.prev_timestamp
    props.total_time += diff
    props.prev_timestamp = now
    print(f"💾 File saved at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))}")
    print(f"⏱️ Total time so far: {props.total_time} seconds ({props.total_time / 60:.2f} minutes)")

    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'PROPERTIES':
                area.tag_redraw()
