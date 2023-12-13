from django.shortcuts import render
from .models import Area, Servicio
from .serializers import AreasSerializer, ServiciosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#def inicio(request):
#    context={}
#    return render(request, 'productos/index.html',context)
@api_view(["GET"])
def ListarAreas(request):
    areas = Area.objects.all()
    serializer = AreasSerializer(areas, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def ListarServicios(request):
    servicios  = Servicio.objects.all()
    serializer = ServiciosSerializer(servicios, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def FiltrarServicio(request, pk):
    servicios = Servicio.objects.get(id_servicio=pk)
    serializer = ServiciosSerializer(servicios, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CrearServicio(request):
    serializer = ServiciosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ActualizarServicio(request, pk):
    servicios = Servicio.objects.get(id_servicio=pk)
    serializer = ServiciosSerializer(instance=servicios, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def EliminarServicio(request, pk):
    servicios = Servicio.objects.get(id_servicio=pk)
    servicios.delete()

    return Response('Producto eliminado')
