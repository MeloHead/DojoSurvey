from django.shortcuts import render, redirect


def index(request):
    print('****'*20)
    print('retrieving info from user')
    return render(request,'index.html')
    #how does route move to /user_info when submit button is clicked


def user_info(request):
    print('****'*20)
    print('this is the user_info page')
    print(f"this is the request.GET {request.GET}")
    print(f"this is the request.POST {request.POST}")
    
    name_from_user = request.POST['namesss']
    location_from_user = request.POST['location']
    language_from_user = request.POST['languages']
    comments_from_user = request.POST['comments']

    context = {
        'name_from_user': name_from_user,
        'location_from_user': location_from_user,
        'language_from_user': language_from_user,
        'comments_from_user': comments_from_user
    }

    print("this is the end of the result page")
    return render(request,'results.html', context)


# def results(request):
#     print('****'*30)
#     print('****'*30)
#     print("this is results page!...")
#     return render(request,"results.html")
    # this is not reading the context from user_info()
