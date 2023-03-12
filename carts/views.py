from .models import Cart
from rest_framework import generics
from .serializers import CartSerializer
from rest_framework.views import Response
from utils.permissions import AdminPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermissions]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=self.request.user)

        serializer = self.serializer_class(cart)

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=self.request.user)

        serializer = self.serializer_class(cart, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
