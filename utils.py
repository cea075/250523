# ✅ utils.py
import os
import json

# 🔹 사용자 정보 저장 함수
def save_patient_info(data: dict, filename="patient_data.json"):
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            patients = json.load(f)
            if not isinstance(patients, list):
                patients = []
    except (FileNotFoundError, json.JSONDecodeError):
        patients = []

    updated = False
    for i, p in enumerate(patients):
        if (
            p.get("name") == data["name"] and
            p.get("age") == data["age"] and
            p.get("gender") == data["gender"]
        ):
            patients[i] = data
            updated = True
            break

    if not updated:
        patients.append(data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(patients, f, ensure_ascii=False, indent=2)

# 🔹 사용자 정보 불러오기
def load_patient_info(filename="patient_data.json"):
    path = os.path.join("data", filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# 🔹 사용자 전체 정보 저장 (삭제 시 사용)
def save_all_patient_info(data_list, filename="patient_data.json"):
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

# 🔹 복용중인 약 정보 저장 함수 (디버깅 포함)
def save_medications(user_id: str, med_list: list, filename="medications.json"):
    os.makedirs("data", exist_ok=True)
    path = os.path.join("data", filename)

    print("\n💾 [save_medications] 실행됨")
    print("   사용자 ID:", user_id)
    print("   약 개수:", len(med_list))
    print("   저장 경로:", os.path.abspath(path))

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                data = {}
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[user_id] = med_list

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✅ 저장 완료!")
    except Exception as e:
        print("❌ 저장 중 오류:", e)

# 🔹 복용중인 약 정보 불러오기 함수
def load_medications(user_id: str, filename="medications.json"):
    path = os.path.join("data", filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(user_id, [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []
