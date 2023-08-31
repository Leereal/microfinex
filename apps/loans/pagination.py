from rest_framework.pagination import PageNumberPagination


class LoanPagination(PageNumberPagination):
    page_size = 4