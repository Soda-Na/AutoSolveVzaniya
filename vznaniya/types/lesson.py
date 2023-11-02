class Lesson:
    def __init__(self, lesson: dict) -> None:
        self.id            = int(lesson.get('id'))
        self.group_id      = int(lesson.get('group_id'))
        self.tasks: dict   = lesson.get('additional_info').get('tasks')
        self.expires: str  = lesson.get('expires_at')
        self.name: str     = lesson.get('name')