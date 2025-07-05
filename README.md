## 카카오 친구목록 / 메시지 API 테스트

#### 1) .env 에 다음을 추가
```
KAKAO_REST_API_KEY="테스트 앱 REST API 키"
KAKAO_REDIRECT_URI="https://<ngrok 주소>/kakao/auth"
```

#### 2) 테스트 앱 Redirect URI에 다음의 주소를 추가
```
https://<ngrok 주소>/kakao/auth
```

#### 3) server.py 를 실행하여 친구 목록 및 메시지 에 대한 액세스 토큰 발급
- `https://<ngrok 주소>/login`
- 메시지를 보낼 친구도 해당 링크도 로그인을 해야함

#### 4) 액세스 토큰을 받아 get_friend_uuid.py 실행하여 친구의 uuid 발급

#### 5) 액세스 토큰 및 uuid 를 넣어서 test_message_sender.py 실행
