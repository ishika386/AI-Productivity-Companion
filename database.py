import sqlite3

# ==========================
# DATABASE CONNECTION
# ==========================

conn = sqlite3.connect(
    "tasks.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================
# TASK TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    deadline TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()


# ==========================
# ADD TASK
# ==========================

def add_task(task, deadline, priority):

    cursor.execute(
        """
        INSERT INTO tasks
        (task, deadline, priority)
        VALUES (?, ?, ?)
        """,
        (task, deadline, priority)
    )

    conn.commit()


# ==========================
# GET ALL TASKS
# ==========================

def get_tasks():

    cursor.execute(
        """
        SELECT *
        FROM tasks
        ORDER BY id DESC
        """
    )

    return cursor.fetchall()


# ==========================
# MARK COMPLETE
# ==========================

def mark_completed(task_id):

    cursor.execute(
        """
        UPDATE tasks
        SET status='Completed'
        WHERE id=?
        """,
        (task_id,)
    )

    conn.commit()


# ==========================
# DELETE TASK
# ==========================

def delete_task(task_id):

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id=?
        """,
        (task_id,)
    )

    conn.commit()


# ==========================
# PENDING TASKS
# ==========================

def get_pending_tasks():

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE status='Pending'
        """
    )

    return cursor.fetchall()


# ==========================
# COMPLETED TASKS
# ==========================

def get_completed_tasks():

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE status='Completed'
        """
    )

    return cursor.fetchall()

def mark_completed(task_id):

    cursor.execute(
        """
        UPDATE tasks
        SET status='Completed'
        WHERE id=?
        """,
        (task_id,)
    )

    conn.commit()


# ==========================
# PRODUCTIVITY STATS
# ==========================

def get_productivity_stats():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        """
    )

    total = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM tasks
        WHERE status='Completed'
        """
    )

    completed = cursor.fetchone()[0]

    pending = total - completed

    if total == 0:
        score = 0
    else:
        score = round((completed / total) * 100)

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "score": score
    }