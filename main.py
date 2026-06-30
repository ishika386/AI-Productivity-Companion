from ai_agent import (
    breakdown_task,
    prioritize_tasks,
    create_schedule,
    productivity_coach
)


def get_task_breakdown(task):
    return breakdown_task(task)


def get_priorities(tasks):
    return prioritize_tasks(tasks)


def get_schedule(tasks):
    return create_schedule(tasks)


def get_coaching(message):
    return productivity_coach(message)