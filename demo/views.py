from django.shortcuts import render
import logging
from django.http import JsonResponse
from prometheus_client import generate_latest
from django.http import HttpResponse

logger = logging.getLogger('django')

def sample_view(request):
    logger.info("Sample view was accessed.")
    return JsonResponse({'message': 'Logged some info!'})

def metrics_view(request):
    """Expose Prometheus metrics, including log counters."""
    metrics = generate_latest()
    return HttpResponse(metrics, content_type='text/plain')