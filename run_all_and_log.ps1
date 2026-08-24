$env:PYTHONIOENCODING="utf-8"
$env:PYTHONUNBUFFERED="1"

Write-Host "Running Step 1..."
python src/01_langsmith_rag_pipeline.py

Write-Host "Running Step 2..."
python src/02_prompt_hub_ab_routing.py > evidence/02_ab_routing_log.txt

Write-Host "Running Step 3 (This takes a while)..."
python src/03_ragas_evaluation.py > evidence/03_ragas_scores.txt

Write-Host "Running Step 4..."
python src/04_guardrails_validator.py > evidence/04_pii_demo_log.txt
Copy-Item evidence/04_pii_demo_log.txt evidence/04_json_demo_log.txt

Write-Host "All tasks completed!"
