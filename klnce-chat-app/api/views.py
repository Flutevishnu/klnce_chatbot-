from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template import loader
from . import options



def get_data(datass):
    if (datass != ""):
        datas = datass.replace("/", "").split(",")
        if "other info" in datas:
            for i in range(len(datas)):
                datas.pop()
                if datas[-1] == "B.TECH Artifical intelligence and Data Science":
                    break
        ans = options.questions["start"]
        for data in datas:
            data = data.strip()
            ans = ans["buttons"][data]
        return ans,datas
    return options.questions["start"]


def web(request):
    template = loader.get_template('template.html')
    enc=""
    if ('text' in request.GET):
        d = request.GET['text']
        # enc = d
        comp, enc = get_data(d)
        enc = ','.join(str(e) for e in enc)
    else:
        comp = get_data('')
    # for i in comp["buttons"]:
        # print(i)
    # if comp["buttons"]:
    # if comp["buttons"] == "other info":



    context = {
        "comp": comp["text"],
        "buttons": comp["buttons"],
        "quer": enc
    }
    return HttpResponse(template.render(context, request))
