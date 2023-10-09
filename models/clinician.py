class Clinician:
    def __init__(
        self,
        id: str,
        name: str,
        shift_count: int,
        timeliness: str,
        open_shifts_picked: int,
        streak: int,
        email: str,
    ):
        self.id = id
        self.name = name
        self.shift_count = shift_count
        self.timeliness = timeliness
        self.open_shifts_picked = open_shifts_picked
        self.streak = streak
        self.email = email

    def __str__(self):
        return f"Clinician(id={self.id}, name={self.name}, shift_count={self.shift_count}, timeliness={self.timeliness}, open_shifts_picked={self.open_shifts_picked}, streak={self.streak}, email={self.email})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "shift_count": self.shift_count,
            "timeliness": self.timeliness,
            "open_shifts_picked": self.open_shifts_picked,
            "streak": self.streak,
            "email": self.email,
        }
