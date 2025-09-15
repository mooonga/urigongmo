import socket
from django.http import HttpResponse

def check_session(request):
    session_key = request.session.session_key
    if not session_key:
        request.session['init'] = True  # 세션 생성
        session_key = request.session.session_key
    server_ip = socket.gethostbyname(socket.gethostname())
    return HttpResponse(f"Session ID: {session_key} | Server: {server_ip}")