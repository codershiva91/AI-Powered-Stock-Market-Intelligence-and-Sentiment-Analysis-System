from datetime import datetime


def current_timestamp():
    return datetime.now()


def combine_text(title, article):
    """
    Merge title and article into one string.
    """
    title = title or ""
    article = article or ""

    return f"{title}. {article}"