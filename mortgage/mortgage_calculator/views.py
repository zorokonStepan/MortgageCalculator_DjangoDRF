from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import GetCalculatorArgs
from .models import MortgageOffers
from .utils import calculate_monthly_payment


def run_calculator(request: HttpRequest):
    """Processing of GET and POST requests at '/'"""
    context = dict()

    if request.method == 'POST':  # getting data from the form
        form = GetCalculatorArgs(request.POST)
        context['form'] = form
        if form.is_valid():
            url = request.get_full_path() + '?'
            tail = ''
            if request.POST['cost_estate']:
                tail += f'sum={request.POST["cost_estate"]}'
            if request.POST['initial_amount']:
                tail += f'&initialAmount={request.POST["initial_amount"]}' if tail \
                    else f'initialAmount={request.POST["initial_amount"]}'
            if request.POST['payment_term']:
                payment_term = int(request.POST['payment_term']) * 12
                if payment_term > 0:
                    tail += f'&term={payment_term}' if tail else f'term={payment_term}'
            if request.POST['param_sort']:
                if request.POST['param_sort'] in ('rate', 'payment'):
                    tail += f'&paramSort={request.POST["param_sort"]}' if tail \
                        else f'paramSort={request.POST["param_sort"]}'
            url += tail
            return redirect(url)

    elif request.method == 'GET':
        form = GetCalculatorArgs()
        context['form'] = form
        context['data'] = []

        cost_estate = None
        initial_amount = 0
        payment_term = None
        param_sort = None

        if request.GET:
            try:  # if the parameters have the correct data type
                if 'sum' in request.GET:
                    cost_estate = int(request.GET['sum'])
                if 'initialAmount' in request.GET:
                    initial_amount = int(request.GET['initialAmount'])
                if 'term' in request.GET:
                    payment_term = int(request.GET['term'])
                if 'paramSort' in request.GET:
                    param_sort = request.GET['paramSort']

                # required for calculation cost_estate and payment_term otherwise context['data'] will remain empty
                # in this case, return all the data
                if cost_estate and payment_term:
                    loan_amount = cost_estate - initial_amount
                    initial_payment_amount = 0 if loan_amount == 0 else (initial_amount / loan_amount * 100)

                    valid_mortgage_offers = \
                        MortgageOffers.objects.filter(term_min__lte=payment_term,
                                                      term_max__gte=payment_term,
                                                      payment_min__lte=loan_amount,
                                                      payment_max__gte=loan_amount,
                                                      initial_payment_min__lte=initial_payment_amount,
                                                      initial_payment_max__gte=initial_payment_amount,)

                    context['data'] = [(mo.bank_name,
                                        mo.rate_min,
                                        *calculate_monthly_payment(loan_amount, payment_term, mo.rate_min))
                                                                                        for mo in valid_mortgage_offers]
                    # data output sorted by rate or payment
                    if param_sort == 'rate':
                        context['data'].sort(key=lambda x: x[1])
                    elif param_sort == 'payment':
                        context['data'].sort(key=lambda x: x[2])
            except:  # context['data'] will remain empty and return all the data
                pass

        if not context['data']:  # return all the data
            mortgage_offers = MortgageOffers.objects.all()
            context['data'] = [(mo.bank_name,
                                mo.rate_min,
                                mo.rate_max,
                                mo.payment_min / 1_000_000,
                                mo.payment_max / 1_000_000,
                                mo.initial_payment_min,
                                mo.initial_payment_max) for mo in mortgage_offers]

            # data output sorted by rate
            if param_sort == 'rate':
                context['data'].sort(key=lambda x: x[1])

        return render(request, 'calculator/calculator.html', context=context)
