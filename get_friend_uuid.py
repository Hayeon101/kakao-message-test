# get_friend_uuid.py
import requests


def get_friends_list(access_token: str):
    API_URL = "https://kapi.kakao.com/v1/api/talk/friends"
    headers = {"Authorization": f"Bearer {access_token}"}
    res = requests.get(API_URL, headers=headers)

    if res.status_code == 200:
        friends_data = res.json()
        print("✅ 친구 목록 가져오기 성공!")
        for friend in friends_data["elements"]:
            # 테스터로 등록된 친구만 목록에 나타납니다.
            print(f"- 닉네임: {friend['profile_nickname']}, UUID: {friend['uuid']}")
    else:
        print(f"❌ 친구 목록 가져오기 실패: {res.json()}")


if __name__ == "__main__":
    # 2단계에서 새로 발급받은 액세스 토큰을 여기에 붙여넣으세요.
    my_new_access_token = (
        "your_token"
    )

    if "여기에" in my_new_access_token:
        print("🛑 스크립트를 수정하여 실제 토큰 값을 넣어주세요.")
    else:
        get_friends_list(my_new_access_token)
