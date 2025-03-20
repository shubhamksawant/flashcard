questions = [
    {
        "question": """What strategies do you use for disaster recovery in Kubernetes?""",
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
    },
]
