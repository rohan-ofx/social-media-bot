from flask import Flask, request, jsonify, render_template,redirect
from bot import auto_reply,get_total_posts,get_logs,get_bot_status,update_bot_status

app = Flask(__name__)

@app.route("/")
def dashboard():
    total_posts = get_total_posts()
    logs = get_logs()
    bot_status = get_bot_status()
    return render_template("dashboard.html",
                            total_posts = total_posts,
                            logs = logs,
                            bot_status = bot_status
                            )

@app.route("/reply", methods=["POST"])
def reply():
    data = request.json
    user_message = data.get("message", "")

    response = auto_reply(user_message)

    return jsonify({
        "user_message": user_message,
        "bot_reply": response
    })

@app.route("/start-bot")
def start_bot():
    update_bot_status("Running")
    return redirect("/")

@app.route("/stop-bot")
def stop_bot():
    update_bot_status("Stopped")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)