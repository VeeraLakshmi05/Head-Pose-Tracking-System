from attention_logic import AttentionTracker

tracker = AttentionTracker()

test_angles = [10, 15, 30, 40, 12, 50]

for angle in test_angles:
    result = tracker.check_attention(angle)
    print(f"Yaw={angle} -> {result}")