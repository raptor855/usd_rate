from datetime import timedelta
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.http import require_GET

from .models import USDRateRequest
from .services import get_usd_rate

MIN_INTERVAL = timedelta(seconds=10)

@require_GET
def get_current_usd(request):
    last_request = USDRateRequest.objects.first()

    if last_request and now() - last_request.created_at < MIN_INTERVAL:
        return JsonResponse(
            {"error": "Requests are allowed not more than once per 10 seconds"},
            status=429
        )

    rate = get_usd_rate()
    USDRateRequest.objects.create(rate=rate)

    last_10 = USDRateRequest.objects.all()[:10]

    return JsonResponse({
        "current_rate": float(rate),
        "last_requests": [
            {
                "rate": float(item.rate),
                "requested_at": item.created_at.isoformat()
            }
            for item in last_10
        ]
    })