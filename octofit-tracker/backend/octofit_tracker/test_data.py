from bson import ObjectId
from datetime import timedelta

test_data = {
    "users": [
        {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"_id": ObjectId(), "name": "Blue Team", "members": []},
        {"_id": ObjectId(), "name": "Gold Team", "members": []},
    ],
    "activities": [
        {"_id": ObjectId(), "user": None, "activity_type": "Cycling", "duration": timedelta(hours=1)},
        {"_id": ObjectId(), "user": None, "activity_type": "Crossfit", "duration": timedelta(hours=2)},
        {"_id": ObjectId(), "user": None, "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
        {"_id": ObjectId(), "user": None, "activity_type": "Strength", "duration": timedelta(minutes=30)},
        {"_id": ObjectId(), "user": None, "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
    ],
    "leaderboard": [
        {"_id": ObjectId(), "user": None, "score": 100},
        {"_id": ObjectId(), "user": None, "score": 90},
        {"_id": ObjectId(), "user": None, "score": 95},
        {"_id": ObjectId(), "user": None, "score": 85},
        {"_id": ObjectId(), "user": None, "score": 80},
    ],
    "workouts": [
        {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
        {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
        {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
        {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
        {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
    ],
}
