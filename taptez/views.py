# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from taptez.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from taptez.models import *
from rest_framework.renderers import TemplateHTMLRenderer

class createVendorProfile():
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'taptez/template/vendor/vendor_list.html'

    def get(self,request):
        vehicle_brand = vendor_utils.vehicle_brand()
        return Response({'vehicle_brand': vehicle_brand})


class VendorListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'vendor/vendor_list.html'

    def get(self,request):
        vendor_list = VendorProfile.objects.all()
        serializer = VendorSerializer(vendor_list, many=True)
        return Response({'vendor_list': serializer.data})