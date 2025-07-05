# test_message_sender.py (수정)
import requests
import json


def send_message_to_friend(access_token: str, friend_uuid: str, message: str):
    """지정한 친구에게 메시지를 보냅니다."""

    API_URL = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

    headers = {"Authorization": f"Bearer {access_token}"}

    template_object = {
        "object_type": "text",
        "text": message,
        "link": {"web_url": "https://www.kookmin.ac.kr"},
    }

    # receiver_uuids에 친구의 UUID를 리스트 형태로 넣습니다.
    data = {
        "receiver_uuids": json.dumps([friend_uuid]),
        "template_object": json.dumps(template_object),
    }

    res = requests.post(API_URL, headers=headers, data=data)

    if res.status_code == 200:
        print("✅ 친구에게 메시지 전송 성공!")
    else:
        print(f"❌ 친구에게 메시지 전송 실패: {res.json()}")


if __name__ == "__main__":
    # 1단계에서 새로 발급받은 액세스 토큰
    my_new_access_token = (
        "your_token"
    )

    # 2단계에서 복사한 팀원의 UUID
    friend_uuid_to_send = "friend_uuid"

    test_message = "팀원에게 보내는 메시지 테스트!"

    if "여기에" in my_new_access_token or "여기에" in friend_uuid_to_send:
        print("🛑 스크립트를 수정하여 실제 토큰과 UUID 값을 넣어주세요.")
    else:
        send_message_to_friend(my_new_access_token, friend_uuid_to_send, test_message)
