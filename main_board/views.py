from django.db.models import Max, Q
from django.shortcuts import render
from django.views import View

from main_board.models import ValueUpdate


class BoardView(View):

    def get(self, request):
        # Note: Query to be changed upon migration to postgres
        max_pairs = ValueUpdate.objects.values(
            'market_index'
        ).annotate(latest_record=Max('updated_at'))
        q = Q()
        for pair in max_pairs:
            q |= Q(market_index=pair['market_index']) & \
                 Q(updated_at=pair['latest_record'])

        current_index_values = ValueUpdate.objects.filter(q)
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
