from database import get_connection

def auto_post():
    conn = get_connection()
    cursor = conn.cursor()

    message = "This is an automatic scheduled post"

    query = "INSERT INTO posts (content) VALUES (%s)"
    cursor.execute(query, (message,))

    conn.commit()
    cursor.close()
    conn.close()

    print("Post published successfully")
    save_log("post published successfully")


def auto_reply(user_message):
    if "hello" in user_message.lower():
        return "Hello! Welcome to our platform"

    elif "help" in user_message.lower():
        return "Support team will contact you soon"

    else:
        return "Thank you for your message"
    
def get_total_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM posts")
    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def save_log(message):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO logs (message) VALUES (%s)"
    cursor.execute(query,(message,))

    conn.commit()
    cursor.close()
    conn.close()

def get_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT message FROM logs ORDER BY id DESC LIMIT 5")
    logs = cursor.fetchall()

    cursor.close()
    conn.close()

    return logs

def get_bot_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM bot_status ORDER BY id DESC LIMIT 1")
    status = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return status

def update_bot_status(new_status):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO bot_status (status) VALUES (%s)"
    cursor.execute(query,(new_status,))
    
    conn.commit()
    cursor.close()
    conn.close()

    save_log(f"Bot status changed to { new_status}")