from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

genai.configure(api_key="AIzaSyCzjfco6Y6U6350Gx8__T1lpeMLeyTzS-c")
model = genai.GenerativeModel("gemini-2.0-flash")

def home(request):
    return render(request, "chat/home.html")

def index(request):
    return render(request, "chat/index.html")

def chat_view(request):
    if request.method == "POST":
        message = request.POST.get("message")
        try:
            response = model.generate_content(message)
            return JsonResponse({"response": response.text})
        except Exception as e:
            return JsonResponse({"response": str(e)})
    return JsonResponse({"error": "Invalid request"}, status=400)
