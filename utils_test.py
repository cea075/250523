from utils import save_all_medications

test_data = [
    {"사용자": "홍길동", "약 이름": "메트포르민", "복용 날짜": "2025-05-21", "복용 시간": "08:00", "비고": "식전"}
]

save_all_medications(test_data)
print("✅ 저장 완료")
