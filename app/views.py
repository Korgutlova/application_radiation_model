from django.shortcuts import render

# Create your views here.
from radiation_model.radiation_calculator import wall_radiation


def custom_handler404(request, exception):
    return render(request, 'app/error404.html', {}, status=404)


def custom_handler500(request):
    return render(request, 'app/error500.html', {}, status=500)


def main(request):
    rad_list = wall_radiation(28, 20, 13, 1, 5, 6, 1, 1)
    print(rad_list)
    output_list = []
    [output_list.append('x: %s z: %s N: %s' % (item.x, item.z, item.rad)) for item in rad_list]
    return render(request, 'app/main.html', {"list": output_list})
