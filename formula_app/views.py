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
    x = math.cos(math.radians(float(phi))-math.radians(float(alpha)))/(math.cos(math.radians(float(alpha)))*(1+math.sqrt(math.sin(math.radians(float(phi)+float(delta_a)))*math.sin(math.radians(float(phi)-float(betha)))/math.cos(math.radians(float(delta_a)+float(alpha)))*math.cos((-1)*math.radians(float(alpha))+math.radians(float(betha))))))
    kagh =  pow(x, 2)
    kag = float(kagh) / math.cos(math.radians(float(delta_a) + float(alpha)))
    kagv = float(kagh) * math.tan(math.radians(float(delta_a) + float(alpha)))
    kaph = math.cos(math.radians(float(alpha))) * math.cos(math.radians(float(betha))) / math.cos(math.radians(float(alpha) - float(betha))) * float(kagh)
    kach = 2 * math.cos(math.radians(float(phi)))*math.cos(math.radians(float(alpha)-float(betha)))*math.cos(math.radians(float(delta_a)+float(alpha)))/(1 + math.sin(math.radians(float(phi) + float(alpha) + float(delta_a) - float(betha)))) * math.cos(math.radians(float(alpha)))
    teta_a = float(phi)+90-math.degrees(math.atan(math.tan(math.radians(float(phi)-float(alpha)))+(1/math.cos(math.radians(float(phi)-float(alpha))))*math.sqrt((math.sin(math.radians(float(delta_a)+float(phi)))*math.cos(math.radians(float(betha)-float(alpha))))/(math.sin(math.radians(float(phi)-float(betha)))*math.cos(math.radians(float(delta_a)+float(alpha)))))))
    k0n=0.5*((1+(1-math.sin(math.radians(float(phi)))))-(1-(1-math.sin(math.radians(float(phi)))))*math.cos(math.radians(2*float(alpha))))
    k0t = 0.5*(1-(1-math.sin(math.radians(float(phi)))))*math.sin(math.radians(2*float(alpha)))
    k0h = float(k0n)*math.cos(math.radians(abs(float(alpha))))-float(k0t)*math.sin(math.radians(abs(float(alpha))))
    k0V = float(k0n)*math.sin(math.radians(abs(float(alpha))))+float(k0t)*math.cos(math.radians(abs(float(alpha))))
    kpgh = math.pow(math.cos(math.radians(float(phi)+float(alpha)))/(math.cos(math.radians(float(alpha)))*(1-math.sqrt((math.sin(math.radians(float(phi)-float(delta_p)))*math.sin(math.radians(float(phi)+float(betha))))/(math.cos(math.radians(-float(delta_p)-float(alpha)))*math.cos(math.radians(float(betha)-float(alpha))))))), 2) 
    kpph = float(kpgh)*((math.cos(math.radians(float(alpha)))*math.cos(math.radians(float(betha))))/(math.cos(math.radians((float(alpha))-(float(betha))))))
    kpch = (2*math.cos(math.radians(float(phi)))*math.cos(math.radians((float(alpha))-(float(betha))))*math.cos(math.radians((float(delta_p))+(float(alpha)))))/(math.cos(math.radians(float(alpha)))*(1-math.sin(math.radians((float(phi))-(float(delta_p))-(float(alpha))+(float(betha))))))
    teta_p = -float(phi)+90-math.degrees(math.atan((math.tan(math.radians(-float(phi)-float(alpha))))+((1/math.cos(math.radians(-float(phi)-float(alpha))))*(math.sqrt((math.sin(math.radians(float(delta_p)-float(phi)))*math.cos(math.radians(float(betha)-float(alpha))))/(-math.sin(math.radians(float(phi)+float(betha)))*math.cos(math.radians(float(delta_p)+float(alpha)))))))))
    # print("kag", kag)
    # print("kagh", kagh)
    # print("kagv", kagv)
    # print("kaph", kaph)
    # print("kach", kach)
    # print("teta_a", teta_a)
    # print("k0n", k0n)
    # print("k0t", k0t)
    # print("k0h", k0h)
    # print("k0V", k0V)
    # print("kpgh", kpgh)
    # print("kpph", kpph)
    # print("kpch", kpch)
    # print("teta_p", teta_p)
    result = Output(kagh = kagh, kag = kag, kagv = kagv, kaph = kaph, kach = kach, teta_a = teta_a, k0t = k0t, k0h = k0h, k0V = k0V, kpgh = kpgh, kpph = kpph, kpch = kpch, teta_p = teta_p)
    result.save()
    return HttpResponse("submit function ended")