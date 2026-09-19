import logging

logger = logging.getLogger(__name__)


def summarize(tasks: list[dict]) -> dict[str, int]:
    total = len(tasks)
    done = sum(1 for task in tasks if task.get("done"))
    logger.info("Summarized tasks", extra={"total": total, "done": done})
    return {"total": total, "done": done, "pending": total - done}
