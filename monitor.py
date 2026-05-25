import os

print("Monitoring Started...")

if os.path.exists("model.pkl"):
    print("Model file exists")
    print("Application status: HEALTHY")
else:
    print("Model file missing")
    print("Application status: FAILED")