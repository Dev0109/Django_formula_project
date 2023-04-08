# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Input, Output
import math

def formula(request):
    inputs = Input.objects.all().values()
    outputs = Output.objects.all().values().last()
    context = {
        'inputs': inputs,
        'outputs': outputs,
    }
    template = loader.get_template('formula.html')
    return HttpResponse(template.render(context, request))

def submit(request):
    # print(request.GET['alpha'])    
    alpha = request.GET['alpha']
    betha = request.GET['betha']
    phi = request.GET['phi']
    delta_a = request.GET['delta_a']
    delta_p = request.GET['delta_p']
    input_value = Input(alpha = alpha, betha = betha, phi = phi, delta_a = delta_a, delta_p = delta_p)
    input_value.save()
    x = (math.cos(float(phi) - float(alpha)) / math.cos(1 + math.sqrt(math.sin(float(phi) + float(delta_a))*math.sin(float(phi) - float(betha))/math.cos(float(alpha) - float(betha))*math.cos(float(alpha) + float(delta_a)))))
    kagh =  pow(x, 2)
    print(kagh)
    kag = float(kagh) / math.cos(float(delta_a) + float(alpha))
    kagv = float(kagh) * math.tan(float(delta_a) + float(alpha))
    kaph = math.cos(float(alpha)) * math.cos(float(betha)) / math.cos(float(alpha) - float(betha)) * float(kagh)
    kach = 2 * math.cos(float(alpha) - float(betha)) * math.cos(float(betha)) * math.cos(float(alpha) + float(delta_a)) / (1 + math.sin(float(phi) + float(alpha) + float(delta_a) - float(betha))) * math.cos(float(alpha))
    teta_a =  float(phi) + math.atan(math.cos(float(phi) - float(alpha)) / math.sin(float(phi) - float(alpha)) + math.sqrt(math.sin(float(alpha) + float(delta_a)) * math.cos(float(alpha) - float(betha)) / math.sin(float(phi) - float(betha)) * math.cos(float(alpha) + float(delta_a))))
    teta_a = float(phi)+90-(math.atan(math.tan((float(phi)*math.pi/180)-(float(alpha)*math.pi/180))+((1/(math.cos((float(phi)*math.pi/180)-(float(alpha)*math.pi/180))))*math.sqrt((math.sin((float(delta_a)*math.pi/180)+(float(phi)*math.pi/180))*math.cos((float(betha)*math.pi/180)-(float(alpha)*math.pi/180)))/(math.sin((float(phi)*math.pi/180)-(float(betha)*math.pi/180))*math.cos((float(delta_a)*math.pi/180)+(float(alpha)*math.pi/180))))))*(180/math.pi))
    k0t = 0.5*(1-(1-math.sin(float(phi)*math.pi/180)))*math.sin(2*float(alpha)*math.pi/180)
    k0h = k0n*math.cos(math.abs(float(alpha)*math.pi/180))-float(k0t)*math.sin(math.abs(float(alpha)*math.pi/180))
    k0V = k0n*math.sin(math.abs(float(alpha)*math.pi/180))+float(k0t)*math.cos(math.abs(float(alpha)*math.pi/180))
    kpgh = math.pow(2, ((math.cos((float(phi)*math.pi/180)+(float(alpha)*math.pi/180)))/(math.cos((float(alpha)*math.pi/180))*(1-math.sqrt((math.sin((float(phi)*math.pi/180)-(float(delta_p)*math.pi/180))*math.sin((float(phi)*math.pi/180)+(float(betha)*math.pi/180)))/(math.cos((-float(delta_p)*math.pi/180)-(float(alpha)*math.pi/180))*math.cos((float(betha)*math.pi/180)-(float(alpha)*math.pi/180))))))))
    kpph = float(delta_p)*((math.cos(float(alpha)*math.pi/180)*math.cos(float(betha)*math.pi/180))/(math.cos((float(alpha)*math.pi/180)-(float(betha)*math.pi/180))))
    kpch = (2*math.cos(float(phi)*math.pi/180)*math.cos((float(alpha)*math.pi/180)-(float(betha)*math.pi/180))*math.cos((float(delta_p)*math.pi/180)+(float(alpha)*math.pi/180)))/(math.cos(float(alpha)*math.pi/180)*(1-math.sin((float(phi)*math.pi/180)-(float(delta_p)*math.pi/180)-(float(alpha)*math.pi/180)+(float(betha)*math.pi/180))))
    teta_p = -float(alpha)+90-(math.atan(math.tan((-float(betha)*math.pi/180)-(float(alpha)*math.pi/180))+((1/(math.cos((-float(phi)*math.pi/180)-(float(alpha)*math.pi/180))))*math.sqrt((math.sin((float(delta_p)*math.pi/180)-(float(phi)*math.pi/180))*math.cos((float(betha)*math.pi/180)-(float(alpha)*math.pi/180)))/(-math.sin((float(phi)*math.pi/180)+(float(betha)*math.pi/180))*math.cos((float(delta_p)*math.pi/180)+(float(alpha)*math.pi/180))))))*(180/math.pi))
    # result = Output(kagh = kagh, kag = kag, kagv = kagv, kaph = kaph, kach = kach, teta_a = teta_a, k0t = k0t, k0h = k0h, k0V = k0V, kpgh = kpgh, kpph = kpph, kpch = kpch, teta_p = teta_p)
    # result.save()
    return HttpResponse("submit function ended")