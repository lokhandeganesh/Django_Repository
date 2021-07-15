from django.shortcuts import render
from .models import Destination
# Create your views here.

#Render html file#
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City that never sleeps'
    dest1.price = 894
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.desc = 'The capital of India'
    dest2.price = 832
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.name = 'Jaipur'
    dest3.desc = 'The pink city of India'
    dest3.price = 950
    dest3.img = 'destination_3.jpg'

    dests = [dest1,dest2,dest3]

    # return render(request,'index.html',{'dest1':dest1,'dest2':dest2})
    return render(request,'index.html',{'dests':dests})