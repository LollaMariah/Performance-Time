from django.shortcuts import render, redirect
from neomodel import db


def QueryCyper(request):
    return render(request, 'QueryCyper.html')

# views.py

import time
import json
from django.http import JsonResponse
from neomodel import db

def run_cypher_query(request):
    if request.method == 'POST':
        try:
            # Ambil query dari request body
            request_data = json.loads(request.body)
            cypher_query = request_data.get('query', '')

            if not cypher_query:
                return JsonResponse({'error': 'Query cannot be empty'}, status=400)

            start_time = time.time()

            # Eksekusi Cypher query
            results, meta = db.cypher_query(cypher_query)
            end_time = time.time()
            performance_time = end_time - start_time

            # Format data hasil query
            formatted_results = []
            for result in results:
                formatted_results.append([str(item) for item in result])

            response_data = {
                'query_result': formatted_results,
                'performance_time': performance_time
            }

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
