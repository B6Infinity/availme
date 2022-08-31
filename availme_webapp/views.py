from time import sleep
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def master_api(request):
    if request.user.username == 'broteen':

        page_id = request.POST['requested_page']

        html = f'''<h1>THIS IS BEGINNIN of {page_id}</h1>
        '''
        sleep(0.2)
        return JsonResponse({
            "content": {
                "html": html,
                "page": page_id
            }
        })
    else:
        return JsonResponse({"FORBIDDEN": "Authentication Error", "ELABORATION": "Unauthenticated Request"})

