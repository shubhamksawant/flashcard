kubernetes_questions = [
    {
        "question": "How do you create a Kubernetes cluster from scratch?",
        "answer": """Steps to create a Kubernetes cluster:
1. Set up infrastructure: Provision EC2 instances in AWS VPC for master and worker nodes
2. Install Kubernetes tools: Install kubeadm, kubelet, and kubectl on all nodes
3. Initialize master node: Use 'kubeadm init' to initialize the control plane
4. Set up kubeconfig: Configure kubectl access
5. Join worker nodes: Use 'kubeadm join' command to add worker nodes
6. Install network plugin: Deploy a network solution like Calico or Weave
7. Verify cluster: Check nodes are ready using 'kubectl get nodes'""",
        "topic": "kubernetes"
    },
    {
        "question": "What is a StatefulSet and when would you use it over a Deployment?",
        "answer": """A StatefulSet is used for applications that require:
- Persistent storage
- Stable network identities
- Ordered deployment and scaling
- Ordered automated rolling updates

Use StatefulSets for applications like databases (MySQL, PostgreSQL) where you need stable hostnames and persistent data even if pods are rescheduled. Unlike Deployments, StatefulSets maintain a fixed identity for each pod.""",
        "topic": "kubernetes"
    },
    {
        "question": "How do you configure horizontal pod autoscaling in Kubernetes?",
        "answer": """To configure Horizontal Pod Autoscaling (HPA):
1. Enable Metrics Server in the cluster
2. Create HPA using kubectl or YAML:
   kubectl autoscale deployment my-app --cpu-percent=50 --min=1 --max=10
   
You can scale based on:
- CPU utilization
- Memory usage
- Custom metrics
- External metrics

HPA automatically adjusts the number of pods based on the defined metrics.""",
        "topic": "kubernetes"
    }
]

security_questions = [
    {
        "question": "How do you secure a Kubernetes cluster?",
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
        "question": "How do you handle secret management in Kubernetes?",
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
    }
]

cicd_questions = [
    {
        "question": "How do you handle continuous integration/continuous deployment (CI/CD) in Kubernetes?",
        "answer": """CI/CD in Kubernetes involves:
1. CI Process:
   - Automated building and testing
   - Container image creation
   - Image vulnerability scanning
   - Push to container registry

2. CD Process:
   - Automated deployment to Kubernetes
   - Rolling updates
   - Canary deployments
   - Automated rollbacks

Tools:
- Jenkins
- GitLab CI
- CircleCI
- ArgoCD (GitOps)

Example Pipeline:
1. Code commit triggers build
2. Run tests
3. Build container image
4. Push to registry
5. Update Kubernetes manifests
6. Deploy to cluster""",
        "topic": "cicd"
    },
    {
        "question": "How do you perform rolling updates and rollbacks in Kubernetes?",
        "answer": """Rolling Updates:
1. Update deployment image:
   kubectl set image deployment/my-deployment container=new-image:v2

2. Monitor rollout:
   kubectl rollout status deployment/my-deployment

Rollbacks:
1. View rollout history:
   kubectl rollout history deployment/my-deployment

2. Rollback to previous version:
   kubectl rollout undo deployment/my-deployment

3. Rollback to specific revision:
   kubectl rollout undo deployment/my-deployment --to-revision=2""",
        "topic": "cicd"
    }
]

monitoring_questions = [
    {
        "question": "How do you monitor and log Kubernetes clusters?",
        "answer": """Monitoring and Logging Setup:
1. Monitoring Tools:
   - Prometheus: Metrics collection
   - Grafana: Visualization
   - Alert Manager: Alerting

2. Logging Solutions:
   - ELK Stack (Elasticsearch, Logstash, Kibana)
   - Fluentd
   - Loki

3. Key Metrics to Monitor:
   - Node health
   - Pod resource usage
   - Application metrics
   - Network performance

4. Best Practices:
   - Centralized logging
   - Real-time monitoring
   - Alert configuration
   - Dashboard creation""",
        "topic": "monitoring"
    }
]

disaster_recovery_questions = [
    {
        "question": "What strategies do you use for disaster recovery in Kubernetes?",
        "answer": """Disaster Recovery Strategies:
1. Backup and Restore:
   - Regular etcd backups
   - Helm charts and YAML backups
   - PersistentVolume backups

2. Cross-Region Replication:
   - Multi-cluster deployment
   - Data replication
   - Geographic distribution

3. Automated Recovery:
   - Use tools like Velero
   - Automated backup scheduling
   - Testing restore procedures

4. Best Practices:
   - Regular backup testing
   - Documentation of recovery procedures
   - Multi-zone deployment
   - Use of PodDisruptionBudgets""",
        "topic": "disaster_recovery"
    }
]

helm_questions = [
    {
        "question": "How do you use Helm for application deployment?",
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
    }
]

questions = (
    kubernetes_questions +
    security_questions +
    cicd_questions +
    monitoring_questions +
    disaster_recovery_questions +
    helm_questions
) 