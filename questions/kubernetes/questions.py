questions = [
    {
        "question": """What is Kubernetes?""",
        "answer": """Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a Pod in Kubernetes?""",
        "answer": """A Pod is the smallest deployable unit in Kubernetes that can contain one or more containers. Containers within a Pod share storage and network resources.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a Kubernetes Service?""",
        "answer": """A Service is an abstraction that defines a logical set of Pods and a policy by which to access them. It enables network connectivity to Pods.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a Deployment in Kubernetes?""",
        "answer": """A Deployment provides declarative updates for Pods and ReplicaSets. It manages the deployment and scaling of applications.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a Kubernetes Namespace?""",
        "answer": """A Namespace is a way to divide cluster resources between multiple users, teams, or projects. It provides a scope for names.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a ConfigMap?""",
        "answer": """ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables or files.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a Secret in Kubernetes?""",
        "answer": """A Secret is an object that contains sensitive data such as passwords, tokens, or keys. It's similar to ConfigMaps but specifically for confidential data.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is a DaemonSet?""",
        "answer": """A DaemonSet ensures that all or some nodes run a copy of a Pod. As nodes are added or removed, DaemonSet automatically adds or removes Pods.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is Kubernetes Ingress?""",
        "answer": """Ingress is an API object that manages external access to services in a cluster, typically HTTP. It provides load balancing, SSL termination, and name-based virtual hosting.""",
        "topic": "kubernetes"
    },
    {
        "question": """What is kubectl?""",
        "answer": """kubectl is the command-line tool for interacting with the Kubernetes cluster. It allows you to run commands against Kubernetes clusters.""",
        "topic": "kubernetes"
    },
    {
        "question": """How do you create a Kubernetes cluster from scratch?""",
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
        "question": """What is a StatefulSet and when would you use it over a Deployment?""",
        "answer": """A StatefulSet is used for applications that require:
- Persistent storage
- Stable network identities
- Ordered deployment and scaling
- Ordered automated rolling updates

Use StatefulSets for applications like databases (MySQL, PostgreSQL) where you need stable hostnames and persistent data even if pods are rescheduled. Unlike Deployments, StatefulSets maintain a fixed identity for each pod.""",
        "topic": "kubernetes"
    },
    {
        "question": """How do you configure horizontal pod autoscaling in Kubernetes?""",
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
    },
]
