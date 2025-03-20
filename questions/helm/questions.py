questions = [
    {
        "question": """How do you use Helm for application deployment?""",
        "answer": """Helm Usage:
1. Chart Structure:
   - Chart.yaml: Metadata
   - values.yaml: Default values
   - templates/: Kubernetes manifests
   - charts/: Dependencies

2. Common Commands:
   - helm install: Deploy a chart
   - helm upgrade: Update a release
   - helm rollback: Revert changes
   - helm list: View releases

3. Best Practices:
   - Version control charts
   - Use value overrides
   - Template validation
   - Documentation

4. Example Usage:
   helm install my-release stable/nginx
   helm upgrade my-release stable/nginx
   helm rollback my-release 1""",
        "topic": "helm"
    },
]
