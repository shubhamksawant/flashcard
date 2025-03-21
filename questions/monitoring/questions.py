questions = [
    {
        "question": """What are the key components of a monitoring system?""",
        "answer": """Key components include: 1) Data collection agents/exporters, 2) Time-series database for storage, 3) Query and processing engine, 4) Visualization platform, 5) Alerting system, 6) Log aggregation system.""",
        "topic": "monitoring"
    },
    {
        "question": """What is the difference between metrics, logs, and traces?""",
        "answer": """Metrics are numerical measurements over time (e.g., CPU usage), Logs are timestamped records of discrete events, and Traces track the flow of requests across distributed systems showing the relationship between services.""",
        "topic": "monitoring"
    },
    {
        "question": """What is an SLI, SLO, and SLA?""",
        "answer": """SLI (Service Level Indicator) is a metric measuring service performance (e.g., latency). SLO (Service Level Objective) is a target value for an SLI (e.g., 99% of requests < 100ms). SLA (Service Level Agreement) is a contract with users about service performance.""",
        "topic": "monitoring"
    },
    {
        "question": """What is the USE method in monitoring?""",
        "answer": """USE stands for Utilization, Saturation, and Errors. It's a methodology for analyzing system performance: Utilization (how busy is the resource), Saturation (amount of queued work), and Errors (count of error events).""",
        "topic": "monitoring"
    },
    {
        "question": """What is the difference between push and pull monitoring?""",
        "answer": """In push monitoring, agents actively send metrics to the monitoring system (e.g., StatsD). In pull monitoring, the monitoring system scrapes metrics from targets (e.g., Prometheus). Pull is generally more reliable and provides better control.""",
        "topic": "monitoring"
    },
    {
        "question": """How do you monitor and log Kubernetes clusters?""",
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
    },
]
