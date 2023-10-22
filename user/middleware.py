from django.shortcuts import redirect

class UserBlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            user_profile = request.user.userprofile
            if user_profile.is_blocked:
                return redirect('login')
        response = self.get_response(request)
        return response
