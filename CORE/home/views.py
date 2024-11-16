from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("""<h1>Hey, I'm a Django Server..</h1>
#                         <p>Hey, This is coming from django server.</p>
#                         <br>
#                         <h3 style = "color:blue">Have a nice day.</h3>
#                         """)

def home(request):

    peoples = [
        {'name' : 'Stunt', 'Age': 23},
        {'name' : 'Psycho', 'Age': 27},
        {'name' : 'Cherry', 'Age': 63},
        {'name' : 'Chinnu', 'Age': 12},
        {'name' : 'Sweety', 'Age': 38}
    ]

    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit facere corrupti dolor dicta porro iure aliquid. Fugit dolore dolores voluptates commodi sed rerum cum culpa perspiciatis, deleniti animi quibusdam, alias consequuntur. Voluptatum error, recusandae quia molestias necessitatibus sit est dolor autem omnis doloribus adipisci nam alias eius. Cumque laborum repudiandae quidem dignissimos labore adipisci ullam illum tempora iure aliquam. Animi deleniti autem harum earum. Labore, voluptate blanditiis. Soluta atque et assumenda modi totam, nisi architecto laudantium voluptatibus beatae a earum ab, sequi temporibus fugit ipsam harum tempore delectus! Nisi perspiciatis repellendus esse libero quis nemo omnis maxime doloremque rem maiores.
    """

    for people in peoples:
        print(people)
    
    return render(request, "index.html", context = {'page': 'Django tutorial 2023', 'peoples':peoples, 'text':text})

def about(request):
    context = {'page':'About'}
    return render(request, "about.html", context)

def contacts(request):
    context = {'page':'Contacts'}
    return render(request, "contacts.html", context)


def success_page(request):
    return HttpResponse("<h1>This is a success page.</h1>")