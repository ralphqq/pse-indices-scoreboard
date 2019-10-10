from django.db.models import Max
from django.shortcuts import render
from django.views import View

from main_board.models import ValueUpdate


class BoardView(View):

    def get(self, request):
        current_index_values = ValueUpdate.objects.order_by(
            'market_index__name',
            '-updated_at'
        ).distinct('market_index__name')
        current_update_time = ValueUpdate.objects.aggregate(
            as_of=Max('updated_at')
        )
        return render(
            request,
            'main_board/index.html',
            {
                'current_index_values': current_index_values,
                'last_update_time': current_update_time.get('as_of')
            }
        )
