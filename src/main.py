import sys
import time
import os
import traceback
import threading
import tkinter as tk

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# __file__ is src/main.py → go up two levels to reach project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# ✅ window created ONCE — never closed or restarted
root = tk.Tk()
root.title("ProDraw")
root.attributes("-fullscreen", True)


def toggle_fullscreen(event=None):
    # Invert the current fullscreen status
    is_fullscreen = not root.attributes("-fullscreen")
    root.attributes("-fullscreen", is_fullscreen)


def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)


root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)


def reload_app():
    for widget in root.winfo_children():
        widget.destroy()

    # ✅ reset all src modules EXCEPT src.main (the runner itself)
    for key in list(sys.modules.keys()):
        if (key == "src" or key.startswith("src.")) and key != "src.main":
            del sys.modules[key]

    try:
        import src.setup as app
        app.setup(root)
        print("✓ Reloaded successfully")
    except Exception:
        traceback.print_exc()
        tk.Label(root, text="⚠ Error — check terminal", bg="red", fg="white",
                 font=("monospace", 14)).pack(expand=True)


def get_all_mtimes(path):
    mtimes = {}
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            # ✅ exclude main.py itself — no need to watch the runner
            if filename.endswith(".py") and filename != "main.py":
                filepath = os.path.join(dirpath, filename)
                mtimes[filepath] = os.path.getmtime(filepath)
    return mtimes


def watch_files():
    src_path = os.path.join(ROOT, "src")
    last_mtimes = get_all_mtimes(src_path)
    last_event = 0

    while True:
        time.sleep(1)
        current_mtimes = get_all_mtimes(src_path)
        now = time.time()

        for filepath, mtime in current_mtimes.items():
            old_mtime = last_mtimes.get(filepath)
            if old_mtime is None or old_mtime != mtime:
                if now - last_event > 1:
                    print(f"\nChange detected: {filepath}")
                    last_event = now
                    last_mtimes = current_mtimes
                    root.after(0, reload_app)
                    break


watcher_thread = threading.Thread(target=watch_files, daemon=True)
watcher_thread.start()

reload_app()
root.mainloop()
