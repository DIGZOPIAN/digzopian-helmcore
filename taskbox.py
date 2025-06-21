# 🧠 TaskBox Router - Digzopian HelmCore

def route_task(command):
    responses = {
        "analyze": "🔍 TaskBox is analyzing...",
        "summarize": "📝 Summarizing data...",
        "interpret": "🔡 Running symbolic interpretation...",
        "reboot": "🔄 Restarting HelmCore subsystems...",
    }
    return responses.get(command.lower(), "⚠️ Unknown task command received.")
