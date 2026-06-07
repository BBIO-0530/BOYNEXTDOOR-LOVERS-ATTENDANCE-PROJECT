import datetime

class P_or_A:
    def __init__(self):
        # 관리 대상 명단
        self.name = ["성호", "리우", "재현", "태산", "이한", "운학", "지코"]
        
        # 크루 명단 별도 분류
        self.crews = ["Makeup crew", "Clothing crew", "Hairstyle crew", "HYBE LABLES MEDICAL TEAM"]
        
        # 비밀번호 딕셔너리
        self.pw = {
            "성호": "tjdgh0904", "리우": "fldn1022", "재현": "wogus1204",
            "태산": "xotks0810", "이한": "dlgks1020", "운학": "dnsgkr1129",
            "지코": "wlzh0914", "Makeup crew": "0530apdlzmdjq", "Clothing crew": "0530dhtzhel",
            "HYBE LABLES MEDICAL TEAM": "0530dmlfyrjawls"
        }

        # 개인별 상세 스케줄
        self.schedule = {
            "성호": (
                "07:10 : 🎤  (신규 앨범)노래 녹음\n"
                "09:00 : 💪  운동 시간\n"
                "09:40 : 🚗  이동 (개인)\n"
                "10:30 : 📷  화보 촬영 (재현 유닛)\n"
                "11:10 : 🚗  이동 (개인)\n"
                "11:30 : 🤝  개인 스캐줄 회의 (ROOM #2)\n"
                "12:00 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "리우": (
                "07:10 : 🚗  이동 (개인)\n"
                "07:30 : 📷  화보 촬영 08:30 (태산 유닛)\n"
                "09:40 : 🚗  이동 (개인)\n"
                "10:00 : 💪  운동 시간\n"
                "10:40 : 🤝  개인 스캐줄 회의\n"
                "11:10 : 🎤  (신규 앨범)노래 녹음 (재현이랑 20분 유닛)\n"
                "12:00 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "재현": (
                "07:10 : 💪  운동 시간\n"
                "09:00 : 🤝  개인 스캐줄 회의\n"
                "09:40 : 🚗  이동 (개인)\n"
                "10:30 : 📷  화보 촬영(성호 유닛)\n"
                "11:10 : 🚗  이동 (개인)\n"
                "11:30 : 🎤  (신규 앨범)노래 녹음 (리우랑 20분 유닛)\n"
                "12:00 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "태산": (
                "07:10 : 🚗  이동 (개인)\n"
                "07:30 : 📷  화보 촬영 08:30 (리우 유닛)\n"
                "09:40 : 🚗  이동 (개인)\n"
                "10:00 : 🎤  (신규 앨범)노래 녹음 (ROOM #1)\n"
                "10:40 : 💪  운동 시간\n"
                "11:10 : 🤝  개인 스캐줄 회의(ROOM #1)\n"
                "12:00 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "이한": (
                "07:10 : 🚗  이동 (개인)\n"
                "07:35 : 📷  화보 촬영 08:30 (운학 유닛)\n"
                "09:45 : 🚗  이동 (개인)\n"
                "10:05 : 💪  운동 시간\n"
                "10:40 : 🎤  (신규 앨범)노래 녹음\n"
                "11:10 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "운학": (
                "07:10 : 🚗  이동 (개인)\n"
                "07:35 : 📷  화보 촬영 08:30 (이한 유닛)\n"
                "09:45 : 🚗  이동 (개인)\n"
                "10:05 : 🎤  (신규 앨범)노래 녹음 (ROOM #2)\n"
                "11:10 : 💪  운동 시간\n"
                "11:50 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🚗  (그룹)이동\n"
                "13:00 : 🎥  (유튜브)촬영(왓도어)\n"
                "14:40 : 🚗  (개인)이동\n"
                "14:55 : 🏠  개인 작업 및 퇴근"
            ),
            "지코": (
                "07:10 : 📝  노래 작업\n"
                "08:30 : 🤝  개인 스케줄 회의\n"
                "09:00 : ☕  쉬는 시간\n"
                "10:00 : 👔  보낵도 스케줄 회의\n"
                "10:30 : 🏠  개인 작업 및 퇴근"
            ),
            "Makeup crew": (
                "07:20 : 💄  화보 메이크업\n"
                "09:45 : ☕  쉬는 시간\n"
                "10:10 : 💄  화보 메이크업\n"
                "11:10 : 🧹  메이크업 청소\n"
                "11:25 : 🏢  회사로 돌아가기 및 쉬는 시간\n"
                "11:50 : 🍽️  점심 시간\n"
                "13:00 : 💄  왓도어 메이크업\n"
                "14:40 : 🧹  메이크업 청소\n"
                "14:55 : 🏠  퇴근"
            ),
            "Clothing crew": (
                "07:20 : 👕  화보 옷 코디 및 수정\n"
                "09:45 : ☕  쉬는 시간\n"
                "10:10 : 👕  화보 옷 코디 및 수정\n"
                "11:10 : 🧹  옷 청소\n"
                "11:25 : 🏢  회사로 돌아가기 및 쉬는 시간\n"
                "11:50 : 🍽️  점심 시간\n"
                "13:00 : 👕  왓도어 옷 코디 및 수정\n"
                "14:40 : 🧹  옷 청소\n"
                "14:55 : 🏠  퇴근"
            ),
            "HYBE LABLES MEDICAL TEAM": (
                "07:10 : 🩺  재현 운동 코치 & 식단 관리\n"
                "09:00 : 🩺  성호 운동 코치 & 식단 관리\n"
                "09:40 : ☕  쉬는 시간\n"
                "10:00 : 🩺  리우 & 이한 운동 코치 & 식단 관리\n"
                "10:40 : 🩺  태산 & 운학 운동 코치 & 식단 관리\n"
                "11:50 : 🍽️  점심 및 쉬는 시간\n"
                "12:45 : 🏠  개인 관리 및 퇴근"
            )
        }

        # 출근 인원수 관리 (멤버는 1명 정원, 크루/팀은 12명 정원)
        self.attendance = {}
        for name in self.name + self.crews:
            if "crew" in name.lower() or "TEAM" in name:
                self.attendance[name] = [0, 12]
            else:
                self.attendance[name] = [0, 1]

    def check(self, name, password):
        """출근 등록 함수"""
        if name not in self.pw:
            print(f"⚠️{name}의 이름은 명단에 없습니다.⚠️지금부터 보안 요원 호출을 시작합니다. 방문자일 경우 옆 안내 카운터를 통해 알리시오.⚠️")
            return
        
        if self.pw[name] == password:
            if self.attendance[name][0] < self.attendance[name][1]:
                self.attendance[name][0] += 1
                print(f"{name}님!\n출근 등록이 완료되었습니다.")
                ASK=input(f"{name}님 스케줄을 확인하시겠습니까?: ")
                if ASK=="예" or ASK=="네" or ASK=="넵":
                    print(f"\n{name}님의 스케줄\n{self.schedule.get(name)}")
                else:
                    print("홈 화면으로 돌아가겠습니다.")
            else:
                print("이미 출근 등록이 완료되어 있습니다.")
        else:
            print("password가 틀렸습니다.\n방문자이실 경우 옆 안내 카운터를 통해 알리시오.\n처음 화면으로 돌아가겠습니다.")

    def check_out(self, name, password):
        """퇴근 등록 함수"""
        if name not in self.pw:
            print(f"⚠️{name}의 이름은 명단에 없습니다.⚠️지금부터 보안 요원 호출을 시작합니다. 방문자일 경우 옆 안내 카운터를 통해 알리시오.⚠️")
            return
        
        if self.pw[name] == password:
            if self.attendance[name][0] > 0:
                self.attendance[name][0] -= 1
                print(f"{name}님!\n퇴근 등록이 완료되었습니다 :)")
            else:
                print("이미 퇴근 등록이 완료되었습니다")
        else:
            print("password가 틀렸습니다.\n방문자일 경우 옆 안내 카운터를 통해 나간다는 것을 알리시오.\n \n처음 화면으로 돌아가겠습니다.")

    #출근 현황 확인
    def status(self):
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n📋🖋️💼출퇴근 현황 확인📋🖋️💼")
        for name in self.name + self.crews:
            curr, total = self.attendance[name]
            print(f"{name}:{curr}/{total}")

system=P_or_A()
while True:
    system.status()
    asking=input("출퇴근 등록을 하시겠습니까?(예/아니요): ").strip()
    if asking in ["예", "네", "넵", "ㅇㅇ"]:
        secondQ=input("출퇴근 중 무엇을 하시겠습니까?: ").strip()
        if secondQ == "출근":
            ask=input("이름을 입력해주세요: ").strip()
            Ask=input("비밀번호를 입력해주세요: ").strip()
            system.check(ask,Ask)

        elif secondQ == "퇴근":
            ask=input("이름을 입력해주세요: ").strip()
            Ask=input("비밀번호를 입력해주세요: ").strip()
            system.check_out(ask,Ask)

        else:
            print("출근 또는 퇴근이라고 입력해 주십시오.")

    elif asking in ["아니오","ㄴㄴ","아니요","ㄱㅊ"]:
        print("system을 종료하겠습니다.")
        break
