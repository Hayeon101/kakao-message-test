import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from config.logger_config import setup_logger
from config.env_loader import (
    ENV,
)  # .dev.env 파일에서 KAKAO_REST_API_KEY를 가져오기 위함

# 로거 설정
logger = setup_logger(__name__)

# FastAPI 앱 생성
app = FastAPI()


# 1. 사용자가 카카오 로그인을 시작하는 주소
@app.get("/login")
async def kakao_login():
    """카카오 로그인 페이지로 리디렉션합니다."""
    kakao_auth_url = (
        f"https://kauth.kakao.com/oauth/authorize?"
        f"client_id={ENV['KAKAO_REST_API_KEY']}"
        f"&redirect_uri={ENV['KAKAO_REDIRECT_URI']}"
        f"&response_type=code"
        f"&scope=friends,talk_message"
    )
    return RedirectResponse(kakao_auth_url)


# 2. 로그인이 성공하면 카카오가 우리 서버로 코드를 보내주는 주소 (Redirect URI)
@app.get("/kakao/auth")
async def kakao_auth_callback(code: str):
    """카카오 로그인 성공 후, 인증 코드로 액세스 토큰을 발급받습니다."""
    token_url = "https://kauth.kakao.com/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": ENV["KAKAO_REST_API_KEY"],
        "redirect_uri": ENV["KAKAO_REDIRECT_URI"],
        "code": code,
    }

    # 카카오 서버에 토큰 요청
    res = requests.post(token_url, data=payload)
    token_data = res.json()

    access_token = token_data.get("access_token")

    if access_token:
        logger.info(f"✅ 액세스 토큰 발급 성공: {access_token}")
        # 나중에는 이 토큰을 DB에 사용자 정보와 함께 저장해야 합니다.
        return {
            "status": "success",
            "message": "액세스 토큰이 발급되었습니다. 서버 로그를 확인하세요.",
        }
    else:
        logger.error(f"❌ 액세스 토큰 발급 실패: {token_data}")
        return {"status": "error", "message": "액세스 토큰 발급에 실패했습니다."}


# .env 파일에 아래 두 줄을 추가하고, 본인의 값으로 채워주세요.
# KAKAO_REST_API_KEY="여러분의 테스트 앱 REST API 키"
# KAKAO_REDIRECT_URI="https://<ngrok 주소>/kakao/auth"
#
# 기존의 챗봇 응답 핸들러는 잠시 주석 처리하거나 지워도 좋습니다.
# @app.post("/kakao")
# ...

if __name__ == "__main__":
    logger.info("🚀 카카오 REST API 테스트 서버 시작")
    logger.info(f"📍 서버 주소: http://localhost:8000")
    logger.info(f"📍 로그인 테스트: http://localhost:8000/login")
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
