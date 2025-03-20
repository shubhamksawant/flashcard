questions = [
    {
        "question": """How do you secure a Kubernetes cluster?""",
        "answer": """Key aspects of Kubernetes security:
1. Network Security:
   - Implement Network Policies to restrict pod communication
   - Use secure communication channels (TLS)

2. Pod Security:
   - Use Pod Security Policies to restrict privileges
   - Run containers as non-root users
   - Limit container capabilities

3. Image Security:
   - Use trusted image sources
   - Implement image scanning
   - Sign and verify container images

4. RBAC:
   - Implement Role-Based Access Control
   - Use minimum required permissions
   - Regularly audit access controls""",
        "topic": "security"
    },
    {
        "question": """How do you handle secret management in Kubernetes?""",
        "answer": """Secret management approaches:
1. Kubernetes Secrets:
   - Built-in secret management
   - Base64 encoded
   - Can be mounted as volumes or environment variables

2. External Tools:
   - HashiCorp Vault: Advanced features like dynamic secrets
   - AWS Secrets Manager: Cloud-native secret management
   - Azure Key Vault: Microsoft's secret management solution

Best Practices:
- Encrypt secrets at rest
- Use RBAC to control access
- Rotate secrets regularly
- Consider external secret management tools for production""",
        "topic": "security"
    },
]
