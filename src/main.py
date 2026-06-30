import sys
import os
import time
import threading
import json
import traceback
import subprocess
import tkinter as tk

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# __file__ é src/main.py → sobe dois níveis até a raiz do projeto
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

STATE_FILE = os.path.join(ROOT, ".window_state.json")

# pastas que não precisam ser observadas (evita reload por causa de cache/venv/git)
IGNORED_DIRS = {".git", "__pycache__", "venv", ".venv", "env", "node_modules"}

IS_MAC = sys.platform == "darwin"


def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"fullscreen": True}


def save_state(state):
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
    except Exception:
        pass


def get_frontmost_app():
    """
    No Mac, pergunta ao sistema qual app está em primeiro plano agora
    (provavelmente o VS Code) para devolver o foco a ele depois do restart.
    Na primeira execução o macOS vai pedir permissão de Automação para
    o Terminal/Python controlar 'System Events' — precisa autorizar em
    Ajustes do Sistema > Privacidade e Segurança > Automação.
    """
    if not IS_MAC:
        return None
    try:
        out = subprocess.run(
            ["osascript", "-e",
             'tell application "System Events" to name of first application process whose frontmost is true'],
            capture_output=True, text=True, timeout=1
        )
        return out.stdout.strip() or None
    except Exception:
        return None


def schedule_refocus(app_name, delay=0.6):
    """Agenda a reativação do app anterior pouco depois do novo processo abrir."""
    if not app_name or not IS_MAC:
        return
    subprocess.Popen([
        "bash", "-c",
        f'sleep {delay} && osascript -e \'tell application "{app_name}" to activate\''
    ])


state = load_state()

root = tk.Tk()
root.title("ProDraw")
root.attributes("-fullscreen", state.get("fullscreen", True))


def toggle_fullscreen(event=None):
    is_fullscreen = not root.attributes("-fullscreen")
    root.attributes("-fullscreen", is_fullscreen)


def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)


root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)


def restart_process(event=None):
    """
    Reinicia o processo Python inteiro, do zero.
    Único jeito de garantir 100% que classes/instâncias antigas presas em
    memória não causem comportamento inconsistente. Usado como fallback
    (quando o reload em memória falha) e também disponível via Cmd+R / F5
    para você forçar manualmente se perceber algo estranho sem erro no console.
    """
    save_state({"fullscreen": bool(root.attributes("-fullscreen"))})
    previous_app = get_frontmost_app()
    schedule_refocus(previous_app)  # devolve o foco ao editor após o restart
    python = sys.executable
    os.execv(python, [python] + sys.argv)


def reload_in_process():
    """
    Tenta primeiro um reload leve EM MEMÓRIA — não fecha/abre janela,
    não rouba foco. Resolve a maioria das mudanças do dia a dia.
    Só cai pro restart completo se o reimport falhar com exceção.

    Limitação importante: existe uma classe de bug (referência presa a uma
    classe antiga, sem erro nenhum) que isso NÃO detecta. Se uma mudança
    não parecer ter feito efeito mesmo sem erro no console, use Cmd+R / F5
    para forçar um restart completo manualmente.
    """
    for widget in root.winfo_children():
        widget.destroy()

    for key in list(sys.modules.keys()):
        if (key == "src" or key.startswith("src.")) and key != "src.main":
            del sys.modules[key]

    try:
        import src.setup as app
        app.setup(root)
        print("✓ Reload em memória OK")
    except Exception:
        print("✗ Reload em memória falhou — reiniciando processo inteiro")
        traceback.print_exc()
        restart_process()


def get_all_mtimes(path):
    mtimes = {}
    for dirpath, dirnames, filenames in os.walk(path):
        # poda diretórios irrelevantes para não gastar tempo nem disparar reload à toa
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for filename in filenames:
            if filename.endswith(".py") and filename != "main.py":
                filepath = os.path.join(dirpath, filename)
                try:
                    mtimes[filepath] = os.path.getmtime(filepath)
                except OSError:
                    pass
    return mtimes


def watch_files():
    # observa todo o pacote src/ — qualquer .py interno conta
    src_path = os.path.join(ROOT, "src")
    last_mtimes = get_all_mtimes(src_path)

    while True:
        time.sleep(0.5)
        current_mtimes = get_all_mtimes(src_path)
        # comparação direta de dicionários: pega criação, edição e remoção de arquivos,
        # sem o bug do "break" que engolia mudanças simultâneas
        if current_mtimes != last_mtimes:
            print("\nMudança detectada — tentando reload em memória...")
            root.after(0, reload_in_process)
            last_mtimes = current_mtimes


# Cmd+R no Mac, F5 em qualquer plataforma: força restart completo manualmente
root.bind("<Command-r>", restart_process)
root.bind("<F5>", restart_process)

watcher_thread = threading.Thread(target=watch_files, daemon=True)
watcher_thread.start()

reload_in_process()
root.mainloop()