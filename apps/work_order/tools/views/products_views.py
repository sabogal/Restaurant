from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from apps.tools.custom_return import CustomResponse, CustomAPIException 
from apps.work_order.tools.serializers.serializers_products import ProductsSerializer
### Erencias
from apps.tools.CustomDjangoPermissions import CustomPermissions  ### PERMISOS CUSTOM
from ..models.products_models import Products
from django.http import Http404
from django.db import transaction

class ProductsViewset(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]  ### Permisos
    serializer_class = ProductsSerializer  ### Serializer
    model = Products  ### Modelo
    queryset = model.objects

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.queryset.all()
        return self.queryset

    def get_object(self, pk):
        try: 
            instance = get_object_or_404(self.model, pk=pk, is_active=True) 
        except Http404 as e:
            raise ValueError("No existe el dato a consultar")
        return instance

    # Crear Grilla de canales
    @transaction.atomic()
    def create(self, request):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user_creation = request.user)
                data["status"] = status.HTTP_200_OK
                data["msg"] = "Se ha creado la orden de trabajo exitosamente."
                data["type"] = "success"
            else:
                data["msg"] = serializer.errors
                raise
        except Exception as e:
            data.setdefault("msg", str(e))
            data["type"] = "error"
        return Response(data, status=data["status"])
    
    def list(self, request, *args, **kwargs):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST
        try:
            queryset = self.queryset.filter(is_active=True)
            serializer = self.serializer_class(queryset, many=True)
            return CustomResponse(msg="Informacion encontrada exitosamente", data=serializer.data)
        except Exception as e:
            data["msg"] = str(e)
            data["type"] = "error"
            return Response(data, status=data["status"])

    # Listar un objeto de grilla de canales
    def retrieve(self, request, pk=None):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST

        try:
            obj = self.get_object(pk)
            if obj:
                user_serializer = self.serializer_class(obj)
                data["type"] = "success"
                data["data"] = user_serializer.data
                data["msg"] = "Informacion encontrada"
                data["status"] = status.HTTP_200_OK
            else:
                raise ValueError("El registro se encuentra eliminado")
        except Exception as e:
            data["msg"] = str(e)
            data["type"] = "error"
        return Response(data, status=data["status"])

    # Editar Grilla de canales
    def update(self, request, pk=None):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST

        try:
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj, data = request.data)
            if serializer.is_valid():
                serializer.save(user_updated = request.user)
                return Response(
                    {"message": "Campaña actualizado correctamente!"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "msg": "hay errores en la actualizacion ",
                    "error": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            data["msg"] = str(e)
            data["type"] = "error"
        return Response(data, status=data["status"])

    # Eliminar Grilla de canales
    def destroy(self, request, pk=None):
        data = {}
        data["status"] = status.HTTP_400_BAD_REQUEST

        try:
            obj = self.get_object(pk)
            if obj:
                obj.is_active = False
                obj.save()
            return CustomResponse(msg="Se ha eliminado el dato exitosamente.")
        except Exception as e:
            data["msg"] = str(e)
            data["type"] = "error"
        return Response(data, status=data["status"])
