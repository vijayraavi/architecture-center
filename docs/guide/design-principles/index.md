---
title: Design principles for Azure applications
description: Design principles for Azure applications
author: MikeWasson
ms.date: 10/30/2018
---

# Ten design principles for Azure applications

Follow these design principles to make your application more scalable, resilient, and manageable. 

## Design for self healing

**Design your application to be self healing when failures occur**. This requires a three-pronged approach:

- Detect failures.
- Respond to failures gracefully.
- Log and monitor failures, to give operational insight.

Don't just consider big events like regional outages, which are generally rare. Focus just as much on handling local, short-lived failures, such as network connectivity failures or failed database connections.

### Recommendations

**Retry failed operations**. Build [retry logic][retry] into your application to handle transient failures. Transient failures include momentary loss of network connectivity, a dropped database connection, or a timeout when a service is busy.

**Protect failing remote services**. If a failure is non-transient, then automatic retries can lead to cascading failures, as requests back up. Use the [Circuit Breaker Pattern][circuit-breaker] to fail fast when an operation is likely to fail.  

**Isolate critical resources**. Failures in one subsystem can sometimes cascade, if resources such as threads or sockets become exhausted. Use the [Bulkhead Pattern][bulkhead] to partition a system into isolated groups, so that a failure in one partition doesn't bring down the entire system.  

**Perform load leveling**. Applications may experience sudden spikes in traffic that can overwhelm services on the backend. To avoid this, use the [Queue-Based Load Leveling Pattern][load-level] to queue work items to run asynchronously. The queue acts as a buffer that smooths out peaks in the load. 

**Fail over**. If an instance can't be reached, fail over to another instance. For things that are stateless, like a web server, put several instances behind a load balancer. For things that store state, like a database, use replicas and fail over. 

**Compensate failed transactions**. Avoid distributed transactions, as they require coordination across services and resources. Instead, compose an operation from smaller individual transactions. If an operation fails, use [Compensating Transactions][compensating-transactions] to undo any steps that already completed. 

**Checkpoint long-running transactions**. Checkpoints can provide resiliency if a long-running operation fails. When the operation restarts, it can be resumed from the last checkpoint.

**Degrade gracefully**. Sometimes you can't work around a problem, but you can provide reduced functionality that is still useful. Entire subsystems might be noncritical for the application. For example, in an e-commerce site, product recommendations are probably less critical than order processing.

**Throttle clients**. Sometimes a small number of users create excessive load, which can reduce your application's availability for other users. In this situation, [throttle][throttle] the client for a certain period of time. 

**Block bad actors**. If a client consistently exceeds their quota or otherwise behaves badly, you might block them. Define an out-of-band process for user to request getting unblocked.

**Use leader election**. When you need to coordinate a task, use [Leader Election][leader-election] to select a coordinator, so the coordinator is not a single point of failure. Rather than implement a leader election algorithm from scratch, consider an off-the-shelf solution such as Zookeeper.  

**Test with fault injection**. All too often, the success path is well tested but not the failure path. A system could run in production for a long time before a failure path is exercised. Use fault injection to test the resiliency of the system to failures, either by triggering actual failures or by simulating them. 

**Embrace chaos engineering**. Chaos engineering extends the idea of fault injection, by randomly injecting failures or abnormal conditions into production instances. 

For a structured approach to making your applications self healing, see [Design resilient applications for Azure][resiliency-overview].  

## Make all things redundant

**Build redundancy into your application, to avoid having single points of failure**. A resilient application routes around failure. Identify the critical paths in your application. Is there redundancy at each point in the path? If a subsystem fails, will the application fail over to something else?

### Recommendations 

**Consider business requirements**. The amount of redundancy built into a system can affect both cost and complexity. Your architecture should be informed by your business requirements, such as recovery time objective (RTO). 

**Place VMs behind a load balancer**. Don't use a single VM for mission-critical workloads. Instead deploy two or more VMs behind a load balancer. 

**Replicate databases**. Azure SQL Database and Cosmos DB automatically replicate the data within a region, and you can enable geo-replication across regions. If you are using an IaaS database solution, choose one that supports replication and failover. 

**Partition for availability**. Database partitioning can improve availability. If one shard goes down, the other shards can still be reached. A failure in one shard will only disrupt a subset of the total transactions. 

**Deploy to more than one region**. For the highest availability, deploy the application to more than one region. In the rare case that a problem affects an entire region, the application can fail over to another region. 

## Minimize coordination

**Minimize coordination between application services to achieve scalability.** Most cloud applications consist of multiple application services &mdash; web front ends, databases, business processes, reporting and analysis, and so on. 

What happens when two instances try to perform concurrent operations that affect some shared state? In some cases, there must be coordination across nodes, for example to preserve ACID guarantees. In this diagram, `Node2` is waiting for `Node1` to release a database lock:

![](./images/database-lock.svg)

Coordination limits the benefits of horizontal scale and creates bottlenecks. As you scale out the application and add more instances, you'll see increased contention. In the worst case, the front-end instances will spend most of their time waiting.

### Recommendations

**Embrace eventual consistency**. When data is distributed, strong consistency can only be achieve by coordinating across nodes. Often it's better if the system can accommodate eventual consistency. Use the [Compensating Transaction][compensating-transaction] pattern to logically roll back after a failure.

**Use domain events to synchronize state**. A [domain event][domain-event] is an event that records when something happens that has significance within the domain. Interested services can listen for the event, rather than using a global transaction to coordinate across multiple services. If this approach is used, the system must tolerate eventual consistency (see previous item). 

**Consider patterns such as CQRS and event sourcing**. These two patterns can help to reduce contention between read workloads and write workloads. 

- The [CQRS pattern][cqrs-pattern] separates read operations from write operations. In some implementations, the read data is physically separated from the write data. 

- In the [Event Sourcing pattern][event-sourcing], state changes are recorded as a series of events to an append-only data store. Appending an event to the stream is an atomic operation, requiring minimal locking. 

However these patterns can be challenging to implement correctly. See [CQRS architecture style][cqrs-style].

**Partition data**.  Avoid putting all of your data into one data schema that is shared across many application services. A microservices architecture enforces this principle by making each service responsible for its own data store. Within a single database, partitioning the data into shards can improve concurrency, because a service writing to one shard does not affect a service writing to a different shard.

**Design idempotent operations**. When possible, design operations to be idempotent. That way, they can be handled using at-least-once semantics. For example, put work items on a queue. If a worker crashes in the middle of an operation, another worker simply picks up the item.

**Use asynchronous parallel processing**. If an operation requires multiple steps that are performed asynchronously (such as remote service calls), you might be able to call them in parallel and aggregate the results.	

**Use optimistic concurrency when possible**. Pessimistic concurrency control uses database locks to prevent conflicts. This can cause poor performance and reduce availability. With optimistic concurrency control, each transaction modifies a copy or snapshot of the data. When the transaction is committed, the database engine validates the transaction and rejects any transactions that would affect database consistency. 

Azure SQL Database and SQL Server support optimistic concurrency through [snapshot isolation][sql-snapshot-isolation]. Some Azure storage services support optimistic concurrency through the use of Etags, including [Azure Cosmos DB][cosmosdb-faq] and [Azure Storage][storage-concurrency].

**Consider MapReduce or other parallel, distributed algorithms**. Depending on the data and type of work to be performed, you may be able to split the work into independent tasks that can be performed by multiple nodes working in parallel. See [Big compute architecture style][big-compute].

**Use leader election for coordination**. If you do need to coordinate operations, make sure the coordinator does not become a single point of failure. Use the [Leader Election pattern][leader-election]. If the leader fails, a new instance is elected to be the leader.
 
## Design to scale out

**Design your application so that it can scale horizontally**. A big advantage of the cloud is elastic scaling &mdash; the ability to use as much capacity as you need, scaling out as load increases, and scaling in when the extra capacity is not needed. Design your application so that it can scale horizontally, adding or removing new instances as demand requires.

### Recommendations

**Avoid instance stickiness**. Stickiness, or *session affinity*, is when requests from the same client are always routed to the same server. Stickiness limits the application's ability to scale out. Make sure that any instance can handle any request.

**Identify bottlenecks**. Scaling out isn't a magic fix for every performance issue. If your backend database is the bottleneck, it won't help to add more web servers. Identify and resolve the bottlenecks in the system first, before throwing more instances at the problem. Stateful parts of the system are the most likely cause of bottlenecks. 

**Decompose workloads by scalability requirements.**  Applications often consist of multiple workloads, with different requirements for scaling. For example, an application might have a public-facing site and a separate administration site. The public site may experience sudden surges in traffic, while the administration site has a smaller, more predictable load. 

**Offload resource-intensive tasks.** Move tasks that require a lot of CPU or I/O resources to [background jobs][background-jobs] when possible, to minimize the load on the front end that handles user requests.

**Use built-in autoscaling features**. Many Azure services have built-in support for autoscaling. If the application has a predictable, regular workload, scale out on a schedule. Otherwise, performance metrics such as CPU or request queue length to trigger autoscaling. See [Autoscaling best practices][autoscaling].

**Consider aggressive autoscaling for critical workloads**. For critical workloads, you want to keep ahead of demand. It's better to add new instances quickly under heavy load to handle the additional traffic, and then gradually scale back.

**Design for scale in**.  With elastic scale, the application will have periods of scale in, when instances get removed. The application must gracefully handle instances being removed:

- Listen for shutdown events (when available) and shut down cleanly. 
- Clients/consumers of a service should support transient fault handling and retry. 
- For long-running tasks, consider breaking up the work, using checkpoints or the [Pipes and Filters][pipes-filters-pattern] pattern. 
- Put work items on a queue so that another instance can pick up the work, if an instance is removed in the middle of processing. 

## Partition around limits

**Use partitioning to work around database, network, and compute limits**. In the cloud, all services have limits in their ability to scale up. Azure service limits are documented in [Azure subscription and service limits, quotas, and constraints][azure-limits]. Limits include number of cores, database size, query throughput, and network throughput. If your system grows sufficiently large, you may hit one or more of these limits. Use partitioning to work around these limits.

There are many ways to partition a system, such as:

- Partition a database to avoid limits on database size, data I/O, or number of concurrent sessions.

- Partition a queue or message bus to avoid limits on the number of requests or the number of concurrent connections.

- Partition an App Service web app to avoid limits on the number of instances per App Service plan. 

A database can be partitioned *horizontally*, *vertically*, or *functionally*.

- In horizontal partitioning, also called sharding, each partition holds data for a subset of the total data set. The partitions share the same data schema. For example, customers whose names start with A&ndash;M go into one partition, N&ndash;Z into another partition.

- In vertical partitioning, each partition holds a subset of the fields for the items in the data store. For example, put frequently accessed fields in one partition, and less frequently accessed fields in another.

- In functional partitioning, data is partitioned according to how it is used by each bounded context in the system. For example, store invoice data in one partition and product inventory data in another. The schemas are independent.

For more detailed guidance, see [Data partitioning][data-partitioning-guidance].

### Recommendations

**Partition different parts of the application**. Databases are one obvious candidate for partitioning, but also consider storage, cache, queues, and compute instances.

**Design the partition key to avoid hot spots**. If you partition a database, but one shard still gets the majority of the requests, then you haven't solved your problem. Ideally, load gets distributed evenly across all the partitions. For example, hash by customer ID and not the first letter of the customer name, because some letters are more frequent. The same principle applies when partitioning a message queue. Pick a partition key that leads to an even distribution of messages across the set of queues. For more information, see [Sharding][sharding].

**Partition around Azure subscription and service limits**. Individual components and services have limits, but there are also limits for subscriptions and resource groups. For very large applications, you might need to partition around those limits.  

**Partition at different levels**. Consider a database server deployed on a VM. The VM has a VHD that is backed by Azure Storage. The storage account belongs to an Azure subscription. Notice that each step in the hierarchy has limits. The database server may have a connection pool limit. VMs have CPU and network limits. Storage has IOPS limits. The subscription has limits on the number of VM cores. Generally, it's easier to partition lower in the hierarchy. Only large applications should need to partition at the subscription level. 

## Design for operations

**Design an application so that the operations team has the tools they need.** The cloud has dramatically changed the role of the operations team. They are no longer responsible for managing the hardware and infrastructure that hosts the application.  That said, operations is still a critical part of running a successful cloud application. Some of the important functions of the operations team include:

- Deployment
- Monitoring
- Escalation
- Incident response
- Security auditing

Robust logging and tracing are particularly important in cloud applications. Involve the operations team in design and planning, to ensure the application gives them the data and insight thay need to be successful.  <!-- to do: Link to DevOps checklist -->

### Recommendations

**Make all things observable**. Once a solution is deployed and running, logs and traces are your primary insight into the system. *Tracing* records a path through the system, and is useful to pinpoint bottlenecks, performance issues, and failure points. *Logging* captures individual events such as application state changes, errors, and exceptions. Log in production, or else you lose insight at the very times when you need it the most.

**Instrument for monitoring**. Monitoring gives insight into how well (or poorly) an application is performing, in terms of availability, performance, and system health. For example, monitoring tells you whether you are meeting your SLA. Monitoring happens during the normal operation of the system. It should be as close to real-time as possible, so that the operations staff can react to issues quickly. Ideally, monitoring can help avert problems before they lead to a critical failure. For more information, see [Monitoring and diagnostics][monitoring].

**Instrument for root cause analysis**. Root cause analysis is the process of finding the underlying cause of failures. It occurs after a failure has already happened. 

**Use distributed tracing**. Use a distributed tracing system that is designed for concurrency, asynchrony, and cloud scale. Traces should include a correlation ID that flows across service boundaries. A single operation may involve calls to multiple application services. If an operation fails, the correlation ID helps to pinpoint the cause of the failure. 

**Standardize logs and metrics**. The operations team will need to aggregate logs from across the various services in your solution. If every service uses its own logging format, it becomes difficult or impossible to get useful information from them. Define a common schema that includes fields such as correlation ID, event name, IP address of the sender, and so forth. Individual services can derive custom schemas that inherit the base schema, and contain additional fields.

**Automate management tasks**, including provisioning, deployment, and monitoring. Automating a task makes it repeatable and less prone to human errors. 

**Treat configuration as code**. Check configuration files into a version control system, so that you can track and version your changes, and roll back if needed. 

## Use managed services

**When possible, use platform as a service (PaaS) rather than infrastructure as a service (IaaS)**. IaaS is like having a box of parts. You can build anything, but you have to assemble it yourself. Managed services are easier to configure and administer. You don't need to provision VMs, set up VNets, manage patches and updates, and all of the other overhead associated with running software on a VM.

For example, suppose your application needs a message queue. You could set up your own messaging service on a VM, using something like RabbitMQ. But Azure Service Bus already provides reliable messaging as service, and it's simpler to set up. Just create a Service Bus namespace (which can be done as part of a deployment script) and then call Service Bus using the client SDK. 

Of course, your application may have specific requirements that make an IaaS approach more suitable. However, even if your application is based on IaaS, look for places where it may be natural to incorporate managed services. These include cache, queues, and data storage.

| Instead of running... | Consider using... |
|-----------------------|-------------|
| Active Directory | Azure Active Directory Domain Services |
| Elasticsearch | Azure Search |
| Hadoop | HDInsight |
| IIS | App Service |
| MongoDB | Cosmos DB |
| Redis | Azure Redis Cache |
| SQL Server | Azure SQL Database |


## Use the best data store for the job

**Pick the storage technology that is the best fit for your data and how it will be used.** Gone are the days when you would just stick all of your data into a big relational SQL database. Relational databases are very good at what they do &mdash; providing ACID guarantees for transactions over relational data. But they come with some costs:

- Queries may require expensive joins.
- Data must be normalized and conform to a predefined schema (schema on write).
- Lock contention may impact performance.

In any large solution, it's likely that a single data store technology won't fill all your needs. Alternatives to relational databases include key/value stores, document databases, search engine databases, time series databases, column family databases, and graph databases. Each has pros and cons, and different types of data fit more naturally into one or another. 

For example, you might store a product catalog in a document database, such as Cosmos DB, which allows for a flexible schema. In that case, each product description is a self-contained document. For queries over the entire catalog, you might index the catalog and store the index in Azure Search. Product inventory might go into a SQL database, because that data requires ACID guarantees.

Remember that data includes more than just the persisted application data. It also includes application logs, events, messages, and caches.

### Recommendations

**Don't use a relational database for everything**. Consider other data stores when appropriate. See [Choose the right data store][data-store-overview].

**Embrace polyglot persistence**. In any large solution, it's likely that a single data store technology won't fill all your needs. 

**Consider the type of data**. For example, put transactional data into SQL, put JSON documents into a document database, put telemetry data into a time series data base, put application logs in Elasticsearch, and put blobs in Azure Blob Storage.

**Prefer availability over (strong) consistency**. The CAP theorem implies that a distributed system must make trade-offs between availability and consistency. (Network partitions, the other leg of the CAP theorem, can never be completely avoided.) Often, you can achieve higher availability by adopting an *eventual consistency* model. 

**Consider the skill set of the development team**. There are advantages to using polyglot persistence, but it's possible to go overboard. Adopting a new data storage technology requires a new set of skills. The development team must understand how to get the most out of the technology. They must understand appropriate usage patterns, how to optimize queries, tune for performance, and so on. Factor this in when considering storage technologies. 

**Use compensating transactions**. A side effect of polyglot persistence is that single transaction might write data to multiple stores. If something fails, use compensating transactions to undo any steps that already completed.

**Look at bounded contexts**. *Bounded context* is a term from domain driven design. A bounded context is an explicit boundary around a domain model, and defines which parts of the domain the model applies to. Ideally, a bounded context maps to a subdomain of the business domain. The bounded contexts in your system are a natural place to consider polyglot persistence. For example, "products" may appear in both the Product Catalog subdomain and the Product Inventory subdomain, but it's very likely that these two subdomains have different requirements for storing, updating, and querying products.
 
## Design for evolution

**An evolutionary design is key for continuous innovation.** All successful applications change over time, whether to fix bugs, add new features, bring in new technologies, or make existing systems more scalable and resilient. If all the parts of an application are tightly coupled, it becomes very hard to introduce changes into the system. A change in one part of the application may break another part, or cause changes to ripple through the entire codebase.

This problem is not limited to monolithic applications. An application can be decomposed into services, but still exhibit the sort of tight coupling that leaves the system rigid and brittle. But when services are designed to evolve, teams can innovate and continuously deliver new features. 

Microservices are becoming a popular way to achieve an evolutionary design, because they address many of the considerations listed here.

### Recommendations

**Enforce high cohesion and loose coupling**. A service is *cohesive* if it provides functionality that logically belongs together. Services are *loosely coupled* if you can change one service without changing the other. High cohesion generally means that changes in one function will require changes in other related functions. If you find that updating a service requires coordinated updates to other services, it may be a sign that your services are not cohesive. One of the goals of domain-driven design (DDD) is to identify those boundaries.

**Encapsulate domain knowledge**. When a client consumes a service, the responsibility for enforcing the business rules of the domain should not fall on the client. Instead, the service should encapsulate all of the domain knowledge that falls under its responsibility. Otherwise, every client has to enforce the business rules, and you end up with domain knowledge spread across different parts of the application. 

**Use asynchronous messaging**. Asynchronous messaging is a way to decouple the message producer from the consumer. The producer does not depend on the consumer responding to the message or taking any particular action. With a pub/sub architecture, the producer may not even know who is consuming the message. New services can easily consume the messages without any modifications to the producer.

**Don't build domain knowledge into a gateway**. Gateways can be useful in a microservices architecture, for things like request routing, protocol translation, load balancing, or authentication. However, the gateway should be restricted to this sort of infrastructure functionality. It should not implement any domain knowledge, to avoid becoming a heavy dependency.

**Expose open interfaces**. Avoid creating custom translation layers that sit between services. Instead, a service should expose an API with a well-defined API contract. The API should be versioned, so that you can evolve the API while maintaining backward compatibility. That way, you can update a service without coordinating updates to all of the upstream services that depend on it. Public facing services should expose a RESTful API over HTTP. Backend services might use an RPC-style messaging protocol for performance reasons. 

**Design and test against service contracts**. When services expose well-defined APIs, you can develop and test against those APIs. That way, you can develop and test an individual service without spinning up all of its dependent services. (Of course, you would still perform integration and load testing against the real services.)

**Abstract infrastructure away from domain logic**. Don't let domain logic get mixed up with infrastructure-related functionality, such as messaging or persistence. Otherwise, changes in the domain logic will require updates to the infrastructure layers and vice versa. 

**Offload cross-cutting concerns to a separate service**. For example, if several services need to authenticate requests, you could move this functionality into its own service. Then you could evolve the authentication service &mdash; for example, by adding a new authentication flow &mdash; without touching any of the services that use it.

**Deploy services independently**. When the DevOps team can deploy a single service independently of other services in the application, updates can happen more quickly and safely. Bug fixes and new features can be rolled out at a more regular cadence. Design both the application and the release process to support independent updates.


## Build for the needs of business

**Every design decision must be justified by a business requirement.** This design principle may seem obvious, but it's crucial to keep in mind when designing a solution. Do you anticipate millions of users, or a few thousand? Is a one hour application outage acceptable? Do you expect large bursts in traffic, or a very predictable workload? Ultimately, every design decision must be justified by a business requirement. 

### Recommendations

**Define business objectives**, including the recovery time objective (RTO), recovery point objective (RPO), and maximum tolerable outage (MTO). These numbers should inform decisions about the architecture. For example, to achieve a low RTO, you might implement automated failover to a secondary region. But if your solution can tolerate a higher RTO, that degree of redundancy might be unnecessary.

**Document service level agreements (SLA) and service level objectives (SLO)**, including availability and performance metrics. You might build a solution that delivers 99.95% availability. Is that enough? The answer is a business decision. 

**Model the application around the business domain**. Start by analyzing the business requirements. Use these requirements to model the application. Consider using a domain-driven design (DDD) approach to create [domain models][domain-model] that reflect the business processes and use cases. 

**Capture both functional and nonfunctional requirements**. Functional requirements let you judge whether the application does the right thing. Nonfunctional requirements let you judge whether the application does those things *well*. In particular, make sure that you understand your requirements for scalability, availability, and latency. These requirements will influence design decisions and choice of technology.

**Decompose by workload**. The term "workload" in this context means a discrete capability or computing task, which can be logically separated from other tasks. Different workloads may have different requirements for availability, scalability, data consistency, and disaster recovery. 

**Plan for growth**. A solution might meet your current needs, in terms of number of users, volume of transactions, data storage, and so forth. However, a robust application can handle growth without major architectural changes. See [Design to scale out](scale-out.md) and [Partition around limits](partition.md). Also consider that your business model and business requirements will likely change over time. If an application's service model and data models are too rigid, it becomes hard to evolve the application for new use cases and scenarios. See [Design for evolution](design-for-evolution.md).

**Manage costs**. In a traditional on-premises application, you pay upfront for hardware (CAPEX). In a cloud application, you pay for the resources that you consume. Make sure that you understand the pricing model for the services that you consume. The total cost will include network bandwidth usage, storage, IP addresses, service consumption, and other factors. See [Azure pricing][pricing] for more information. Also consider your operations costs. In the cloud, you don't have to manage the hardware or other infrastructure, but you still need to manage your applications, including DevOps, incident response, disaster recovery, and so forth. 

[domain-model]: https://martinfowler.com/eaaCatalog/domainModel.html
[pricing]: https://azure.microsoft.com/pricing/

[monitoring]: ../../best-practices/monitoring.md
[big-compute]: ../architecture-styles/big-compute.md
[compensating-transaction]: ../../patterns/compensating-transaction.md
[cqrs-style]: ../architecture-styles/cqrs.md
[cqrs-pattern]: ../../patterns/cqrs.md
[cosmosdb-faq]: /azure/cosmos-db/faq
[domain-event]: https://martinfowler.com/eaaDev/DomainEvent.html
[event-sourcing]: ../../patterns/event-sourcing.md
[leader-election]: ../../patterns/leader-election.md
[sas-pattern]: ../../patterns/scheduler-agent-supervisor.md
[sql-snapshot-isolation]: /sql/t-sql/statements/set-transaction-isolation-level-transact-sql
[storage-concurrency]: https://azure.microsoft.com/blog/managing-concurrency-in-microsoft-azure-storage-2/
[azure-limits]: /azure/azure-subscription-service-limits
[data-partitioning-guidance]: ../../best-practices/data-partitioning.md
[sharding]: ../../patterns/sharding.md
[multi-vm-blueprint]: ../../reference-architectures/virtual-machines-windows/multi-vm.md

[cassandra]: https://cassandra.apache.org/
[cosmosdb-geo-replication]: /azure/cosmos-db/distribute-data-globally
[sql-always-on]: https://msdn.microsoft.com/library/hh510230.aspx
[sql-geo-replication]: /azure/sql-database/sql-database-geo-replication-overview

[autoscaling]: ../../best-practices/auto-scaling.md
[background-jobs]: ../../best-practices/background-jobs.md
[pipes-filters-pattern]: ../../patterns/pipes-and-filters.md

[circuit-breaker]: ../../patterns/circuit-breaker.md
[compensating-transactions]: ../../patterns/compensating-transaction.md
[leader-election]: ../../patterns/leader-election.md
[load-level]: ../../patterns/queue-based-load-leveling.md
[resiliency-overview]: ../../resiliency/index.md
[retry]: ../../patterns/retry.md
[throttle]: ../../patterns/throttling.md
[transient-fault-handling]: ../../best-practices/transient-faults.md
[data-store-overview]: ../technology-choices/data-store-overview.md
[bulkhead]: ../../patterns/bulkhead.md