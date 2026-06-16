import cv2
import json

from pose_estimation import PoseEstimator
from attention_logic import AttentionTracker

pose_estimator = PoseEstimator()

attention_tracker = AttentionTracker(
    angle_threshold=15,
    duration_threshold=1.5
)
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    pose = pose_estimator.get_head_pose(frame)

    if pose:

        pitch, yaw, roll = pose

        result = attention_tracker.check_attention(yaw,pitch)

        print(json.dumps(result))

        cv2.putText(
            frame,
            f"Yaw: {yaw:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Pitch: {pitch:.2f}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Roll: {roll:.2f}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        status_text = (
            "LOOKING AWAY"
            if result["looking_away"]
            else
            "ATTENTIVE"
        )
        cv2.putText(
    frame,
    f"Away Time: {result['away_time']}s",
    (20, 220),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 0, 0),
    2
)

        color = (
            (0, 0, 255)
            if result["looking_away"]
            else
            (0, 255, 0)
        )

        cv2.putText(
            frame,
            status_text,
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            3
        )

    cv2.imshow(
        "Head Pose Tracking",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break

stats = attention_tracker.get_statistics()

print("\n========== SESSION REPORT ==========")

print(
    f"Total Look Away Events : "
    f"{stats['total_lookaway_events']}"
)

print(
    f"Maximum Angle Reached : "
    f"{stats['maximum_angle']} degrees"
)

print(
    f"Longest Away Duration : "
    f"{stats['longest_away_duration']} sec"
)

print("====================================")

cap.release()
cv2.destroyAllWindows()