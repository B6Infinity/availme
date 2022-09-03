import json
from time import sleep
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from .models import Board



# INTERNAL FUNCTIONS
def fetchBoards(request, context):

    context_body = context['body']
    filters = context_body['filters']
    
    
    
    # -------------------------------------------------------------------------------------------------------------------------
    
    

    # GET FROM DB
    fetched_boards = []
    
    if len(filters) == 0:
        fetched_boards = Board.objects.all()
    else:
        if 'LOCATION' in filters:
            print(filters['LOCATION'])
            fetched_boards += Board.objects.filter(location__iexact=filters['LOCATION'])
        if 'STATUS' in filters:
            fetched_boards += Board.objects.filter(status=filters['STATUS'])

    

    # SERIALISE
    FETCHED_BOARDS = {}

    for board in fetched_boards:

        FETCHED_BOARDS[board.id] = {
            "coordinates": [board.lattitude, board.longitude],
            "location": board.location,
            "status": board.status,
            "title": board.title
        }

    

    
    

    RESPONSE = {
        "request_username": request.user.username,
        "requested_boards": FETCHED_BOARDS
    }
    
    return RESPONSE

def fetchPageHTML(request, context):
    pageid = ''
    return {}



# -------------------------------------------------------------------------------------------------------------------------




# GLOBAL VARS
API_CONTEXT_REFERENCE = {
    "asg4tsdg4g": fetchPageHTML, # "PAGE_HTML_INJECTION", 
    "df6b1c2b6f": fetchBoards, # "BOARD"
}




# -------------------------------------------------------------------------------------------------------------------------






# Create your views here.
def index(request):
    return render(request, 'index.html')

def master_api(request):
    '''
    The body of each Request should be like the following:

    
    context_refernce = "",
    context = {
        "body":{}
    },
    
    '''

    # Authenticate Request
    if request.user.username == 'broteen':

        # Identify what the client is asking for
        context_action = API_CONTEXT_REFERENCE[request.POST['context_refernce']]
        context = json.loads(request.POST['context'])

        

        # Get what the client is asking for
        JSON_RESPONSE = context_action(request, context)


        # RETURN JSON RESPONSE
        return JsonResponse(JSON_RESPONSE, safe=False)
    else:
        return JsonResponse({"FORBIDDEN": "Authentication Error", "ELABORATION": "Unauthenticated Request"})







