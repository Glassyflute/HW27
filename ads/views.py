from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return JsonResponse(
        {"status": "ok"}, status=200
    )


@method_decorator(csrf_exempt, name="dispatch")
class VacancyView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        search_text = request.GET.get("text", None)
        if search_text:
            vacancies = vacancies.filter(text=search_text)

        response = []
        for vacancy in vacancies:
            response.append(
                {
                    "id": vacancy.id,
                    "text": vacancy.text
                }
            )

        return JsonResponse(response, safe=False)

    def post(self, request):
        vacancy_data = json.loads(request.body)

        vacancy = Vacancy()
        vacancy.text = vacancy_data["text"]

        vacancy.save()

        return JsonResponse({
                    "id": vacancy.id,
                    "text": vacancy.text
                })


class VacancyDetailView(DetailView):
     model = Vacancy

     def get(self, request, *args, **kwargs):
        vacancy = self.get_object()

        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })


