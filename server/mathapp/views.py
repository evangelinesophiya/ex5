from django.shortcuts import render

def rectangle_area(request):
    context = {}
    if request.method == "POST":
        if request.POST.get("length") and request.POST.get("breadth"):
            length = float(request.POST.get("length"))
            breadth = float(request.POST.get("breadth"))
            area = length * breadth
            context['length'] = length
            context['breadth'] = breadth
            context['area'] = area
            print("request is POST")
        else:
            print("request is POST but no length or breadth")
    else:
        print("request is GET")
    return render(request, "mathapp/math.html", context)