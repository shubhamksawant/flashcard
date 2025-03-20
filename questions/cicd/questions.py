questions = [
    {
        "question": """What is Continuous Integration (CI)?""",
        "answer": """Continuous Integration is the practice of automatically integrating code changes from multiple contributors into a single software project. It's usually done several times a day.""",
        "topic": "cicd"
    },
    {
        "question": """What is Continuous Deployment (CD)?""",
        "answer": """Continuous Deployment is a software release process that uses automated testing to validate if changes to a codebase are correct and stable for immediate autonomous deployment to a production environment.""",
        "topic": "cicd"
    },
    {
        "question": """What is a Pipeline in CI/CD?""",
        "answer": """A pipeline is a set of automated processes and tools that allows developers and DevOps professionals to reliably and efficiently compile, build, and deploy their code to production environments.""",
        "topic": "cicd"
    },
    {
        "question": """What is the difference between Continuous Delivery and Continuous Deployment?""",
        "answer": """Continuous Delivery ensures code can be rapidly and safely deployed to production by delivering every change to a production-like environment. Continuous Deployment takes it further by automatically deploying every change that passes tests to production.""",
        "topic": "cicd"
    },
    {
        "question": """What are Build Artifacts?""",
        "answer": """Build artifacts are the files created by the build process, such as compiled code, packages, executables, logs, and documentation that are needed for deployment.""",
        "topic": "cicd"
    },
    {
        "question": """What is a Build Trigger?""",
        "answer": """A build trigger is a set of criteria that, when met, initiates an automated build process. Common triggers include code commits, pull requests, and scheduled times.""",
        "topic": "cicd"
    },
    {
        "question": """What is Infrastructure as Code (IaC) in CI/CD?""",
        "answer": """IaC in CI/CD refers to managing and provisioning infrastructure through code instead of manual processes, allowing version control and automated deployment of infrastructure changes.""",
        "topic": "cicd"
    },
    {
        "question": """What is a Deployment Strategy?""",
        "answer": """A deployment strategy is a method used to roll out changes to production. Common strategies include blue-green deployment, canary releases, and rolling updates.""",
        "topic": "cicd"
    },
    {
        "question": """What is Jenkins?""",
        "answer": """Jenkins is an open-source automation server that helps automate parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery.""",
        "topic": "cicd"
    },
    {
        "question": """What are Environment Variables in CI/CD?""",
        "answer": """Environment variables are dynamic values that can affect the way running processes will behave on a computer. In CI/CD, they're used to store configuration settings and sensitive information.""",
        "topic": "cicd"
    },
    {
        "question": """How do you handle continuous integration/continuous deployment (CI/CD) in Kubernetes?""",
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
        "question": """How do you perform rolling updates and rollbacks in Kubernetes?""",
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
    },
]
