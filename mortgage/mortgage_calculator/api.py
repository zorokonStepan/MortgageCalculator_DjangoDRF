from rest_framework import viewsets

from .models import MortgageOffers
from .serializers import MortgageOffersSerializer, MortgageOffersReceiveProcessSerializer
from rest_framework.response import Response
from .utils import calculate_monthly_payment


class MortgageOffersViewSet(viewsets.ModelViewSet):
    """
    Implements API CRUD
    To process a GET request with and without parameters, the method has been redefined list
    """
    queryset = MortgageOffers.objects.all()
    serializer_class = MortgageOffersSerializer

    def list(self, request):
        """To process a GET request with and without parameters"""
        if not request.query_params:  # GET request without parameters
            serializer_class = MortgageOffersSerializer(self.queryset, many=True)
            return Response(serializer_class.data)
        else:  # GET request with parameters
            try:  # a complete set of valid parameters
                price = int(self.request.query_params.get('price'))  # the price of the property
                deposit = int(self.request.query_params.get('deposit'))  # initial payment as a percentage
                term = int(self.request.query_params.get('term')) * 12  # number of years of mortgage

                loan_amount = price - price * deposit / 100
                queryset = MortgageOffers.objects.all().values()

                for q in queryset:
                    monthly_payment = calculate_monthly_payment(loan_amount, term, q['rate_min'])[0]
                    q['payment'] = monthly_payment

                queryset = sorted(queryset, key=lambda x: x['payment'])
                serializer_class = MortgageOffersReceiveProcessSerializer(queryset, many=True)
                return Response(serializer_class.data)

            except:  # the parameters are not all or the wrong data type
                return Response({})
