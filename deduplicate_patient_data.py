import json
import os

file_path = os.path.join("data", "patient_data.json")

if not os.path.exists(file_path):
    print("❌ patient_data.json 파일이 없습니다.")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

if not isinstance(data, list):
    print("❌ JSON 파일 구조가 리스트가 아닙니다.")
    exit()

# ✅ 이름 기준으로 중복 제거 (뒤에 나오는 게 최신으로 간주)
unique = {}
for entry in data:
    name = entry.get("name")
    if name:
        unique[name] = entry  # 동일 이름일 경우 덮어씀

deduped = list(unique.values())

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(deduped, f, ensure_ascii=False, indent=2)

print(f"✅ 중복 제거 완료: 총 {len(deduped)}명 저장됨.")
