from time import sleep
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def master_api(request):
    if request.user.username == 'broteen':

        page_id = request.POST['requested_page']

        if page_id == 'MAP':
            return JsonResponse({
                "content": {
                    "html": '''
                    <div id="INJECTED_HTML">
                        <div id="map"></div>
                        <div id="markerdetails_panel">
                            <div class="header" style="height: 60px;">
                                <h2 id="board_title">Click on a Pin</h2>
                            </div>

                            <div id="board_details">
                                <h2 class="details-heading">Location</h2>
                                <h4 id="board_location">--</h4>
                                <!-- <button id="open_board_in_maps" style="">Open in Google Maps</button> -->
                                <br>
                                <h2 class="details-heading">STATUS</h2>
                                <h4 id="board_status">--</h4>
                                
                                <img id="board_image" src="https://dummyimage.com/1600x900/7f7f7f" alt="">
                                
                                <h2 class="details-heading">Details</h2>
                                


                            </div>

                        </div>
                    </div>

                    <style>
    
                        #INJECTED_HTML{
                            color: rgb(246, 246, 223);
                            font-family: ABeeZee, sans-serif;
                            margin: 0%;
                            padding: 0%;

                            display: flex;
                            flex-direction: row;
                            
                        }
                        #map{
                            flex-grow: 1;
                            height: 90vh;
                            
                        }
                        #markerdetails_panel{
                            width: 250px;
                            background-color: #141313;
                        }
                        
                        

                        .details-heading{
                            margin: 8px 0;
                        }
                        #board_details{
                            background-color: #141313;
                            height: 80vh;
                            overflow: auto;
                        }

                        #board_title{
                            padding: 10px;
                        }
                        #board_details{
                            padding: 20px;
                            
                        }
                        #board_image{
                            width: 100%;
                            object-fit: contain;
                            margin: 20px 0;
                        }

                    </style>

                    
                    ''',
                    "JS": ''''''
                },
                "page": page_id
            })



        html = f'''<h1>THIS IS BEGINNIN of {page_id}</h1>
        '''
        # sleep(0.2)
        return JsonResponse({
            "content": {
                "html": html,
                "page": page_id
            }
        })
    else:
        return JsonResponse({"FORBIDDEN": "Authentication Error", "ELABORATION": "Unauthenticated Request"})

