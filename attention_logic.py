import time
import math

class AttentionTracker:

    def __init__(self,
                 angle_threshold=15,
                 duration_threshold=1):

        self.angle_threshold = angle_threshold
        self.duration_threshold = duration_threshold

        self.start_time = None

        self.total_lookaway_events = 0
        self.max_angle = 0
        self.longest_away_duration = 0

        self.previous_state = False

    def check_attention(self, yaw, pitch):

        yaw_angle = abs(yaw)
        pitch_angle = abs(pitch)

        current_angle = math.sqrt(
    yaw_angle ** 2 +
    pitch_angle ** 2
)

        self.max_angle = max(
            self.max_angle,
            current_angle
        )

        looking_away = False
        away_time = 0

        if current_angle > self.angle_threshold:

            if self.start_time is None:
                self.start_time = time.time()

            away_time = time.time() - self.start_time

            self.longest_away_duration = max(
                self.longest_away_duration,
                away_time
            )

            if away_time >= self.duration_threshold:
                looking_away = True

        else:
            self.start_time = None

        if looking_away and not self.previous_state:
            self.total_lookaway_events += 1

        self.previous_state = looking_away

        return {
            "looking_away": looking_away,
            "angle": round(current_angle, 2),
            "away_time": round(away_time, 2)
        }

    def get_statistics(self):

        return {
            "total_lookaway_events":
                self.total_lookaway_events,

            "maximum_angle":
                round(self.max_angle, 2),

            "longest_away_duration":
                round(self.longest_away_duration, 2)
        }