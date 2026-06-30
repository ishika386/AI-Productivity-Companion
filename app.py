import streamlit as st
from database import (
    add_task,
    get_tasks,
    get_productivity_stats,
    mark_completed
)
from main import (
    get_task_breakdown,
    get_priorities,
    get_schedule,
    get_coaching
)


st.set_page_config(
    page_title="AI Productivity Companion",
    page_icon="🚀",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg,#4f46e5,#7c3aed);
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.metric-card {
    padding: 1rem;
    border-radius: 15px;
    background: #1e293b;
    border: 1px solid #334155;
}

.task-card {
    padding: 15px;
    border-radius: 12px;
    background: #111827;
    border-left: 5px solid #6366f1;
    margin-bottom: 10px;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class='hero'>
<h1>🚀AI Productivity Companion</h1>
<h4>  Your Agentic Productivity Companion</h4>
<p>Plan Smarter • Beat Deadlines • Stay Consistent</p>
</div>
""", unsafe_allow_html=True)


st.sidebar.title("⚡ Quick Actions")

st.sidebar.info("""
This AI assistant helps you:

✅ Break down tasks

✅ Prioritize intelligently

✅ Generate schedules

✅ Stay productive

✅ Avoid missing deadlines
""")


tasks = get_tasks()

stats = get_productivity_stats()

total_tasks = stats["total"]
completed_tasks = stats["completed"]
productivity_score = stats["score"]

high_priority = sum(
    1 for t in tasks if t[3].lower() == "high"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📋 Total Tasks", total_tasks)

with col2:
    st.metric("🔥 High Priority", high_priority)

with col3:
    st.metric("✅ Completed", completed_tasks)

with col4:
    st.metric("📈 Productivity", f"{productivity_score}%")

st.divider()


tab1, tab2, tab3, tab4 = st.tabs(
    [
        "➕ Add Task",
        "🎯 Prioritize",
        "📅 Schedule",
        "🧠 AI Coach"
    ]
)


with tab1:

    st.subheader("Add New Task")

    task = st.text_input(
        "Task Name",
        placeholder="Prepare internship presentation"
    )

    col1, col2 = st.columns(2)

    with col1:
        deadline = st.date_input("Deadline")

    with col2:
        priority = st.selectbox(
            "Priority",
            ["High", "Medium", "Low"]
        )

    if st.button("🚀 Add Task & Generate Breakdown"):

        if task.strip():

            add_task(
                task,
                str(deadline),
                priority
            )

            st.success("Task Added Successfully!")

            with st.spinner(
                "AI is breaking task into actionable steps..."
            ):
                breakdown = get_task_breakdown(task)

            st.markdown("### 🧩 AI Task Breakdown")

            st.markdown(breakdown)

        else:
            st.warning("Please enter a task.")

    st.divider()

    st.subheader("📋 Existing Tasks")

    current_tasks = get_tasks()

    if current_tasks:

        for t in current_tasks:

            col_task, col_btn = st.columns([5, 1])

            with col_task:

                status_color = "🟢" if t[4] == "Completed" else "🟡"

                st.markdown(
                    f"""
                    <div class='task-card'>
                    <b>{t[1]}</b><br>
                    📅 Deadline: {t[2]}<br>
                    🔥 Priority: {t[3]}<br>
                    {status_color} Status: {t[4]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col_btn:

                if t[4] == "Pending":

                    if st.button(
                        "✅ Done",
                        key=f"done_{t[0]}"
                    ):

                        mark_completed(t[0])

                        st.balloons()

                        st.success(
                            f"Task '{t[1]}' completed!"
                        )

                        st.rerun()

                else:

                    st.success("Done")

    else:
        st.info("No tasks added yet.")


with tab2:

    st.subheader("🎯 AI Task Prioritization")

    if st.button("Generate Priority Ranking", key="priority_btn"):

        tasks = get_tasks()

        if tasks:

            task_text = "\n".join(
                [
                    f"{t[1]} | Deadline:{t[2]} | Priority:{t[3]}"
                    for t in tasks
                ]
            )

            with st.spinner(
                "Analyzing urgency and importance..."
            ):
                result = get_priorities(task_text)

            st.markdown(result)

        else:
            st.warning("Add tasks first.")


with tab3:

    st.subheader("📅 AI Schedule Planner")

    if st.button("Generate Smart Schedule", key="schedule_btn"):

        tasks = get_tasks()

        if tasks:

            task_text = "\n".join(
                [
                    f"{t[1]} | Deadline:{t[2]} | Priority:{t[3]}"
                    for t in tasks
                ]
            )

            with st.spinner(
                "Creating optimized daily plan..."
            ):
                schedule = get_schedule(task_text)

            st.markdown(schedule)

        else:
            st.warning("Add tasks first.")


with tab4:

    st.subheader("🧠 AI Productivity Coach")

    user_message = st.text_area(
        "What's stopping you today?",
        placeholder="I have too many deadlines and don't know where to start..."
    )

    if st.button("Get AI Advice", key="coach_btn"):

        if user_message.strip():

            with st.spinner(
                "Thinking like a productivity coach..."
            ):
                advice = get_coaching(user_message)

            st.markdown(advice)

        else:
            st.warning(
                "Please enter your concern."
            )


st.divider()

st.caption(
    "Built with ❤️ using Streamlit, Gemini AI and SQLite"
)