<!-- TEMPLATE FILE - DO NOT ADD METADATA -->
<!-- markdownlint-disable MD002 MD041 -->

### Governance of resources

Enforcing governance across subscriptions will come from Azure Blueprints and the associated assets within the blueprint.

1. Create a blueprint named `governance-baseline`.
    1. Enforce the use of standard Azure roles.
    2. Enforce that users can only authenticate against existing an RBAC implementation.
    3. Apply this blueprint to all subscriptions within the management group.
2. Create an Azure policy to apply or enforce the following:
    1. Resource tagging should require values for Business Function, Data Classification, Criticality, SLA, Environment, and  Application.
    2. The value of the Application tag should match the name of the resource group.
    3. Validate role assignments for each resource group and resource.
3. Publish and apply the `governance-baseline` blueprint to each management group.

These patterns enable resources to be discovered and tracked, and enforce basic role management.

### Demilitarized Zone (DMZ)

Specific subscriptions often require some level of access to on-premise resources. This is common in migration scenarios or dev scenarios where dependent resources reside in the on-premises datacenter.  

Until trust in the cloud environment is fully established it's important to tightly control and monitor any allowed communication between the on-premises environment and cloud workloads, and that the on-premises network is secured against potential unauthorized access from cloud-based resources. To support these scenarios, the governance MVP adds the following best practices:

1. Establish a cloud DMZ.
    1. The [Cloud DMZ reference architecture](/azure/architecture/reference-architectures/dmz/secure-vnet-hybrid) establishes a pattern and deployment model for creating a VPN Gateway in Azure.
    2. Validate that proper DMZ connectivity is in place for a local edge device in the on-premises datacenter, and that on-premises security and traffic management mechanisms are configured to only allow access to and from authorized resources and services hosted in the cloud.
    3. Validate that the local edge device is compatible with Azure VPN Gateway requirements.
    <!-- 4. Once connection to the on-premisess VPN has been verified, capture the Resource Manager template created by that reference architecture. -->
1. Create a second blueprint named `dmz`.
    1. Add the Resource Manager template for the VPN Gateway to the blueprint.
1. Apply the DMZ blueprint to any subscriptions requiring on-premises connectivity. This blueprint should be applied in addition to the governance MVP blueprint.

One of the biggest concerns raised by IT security and traditional governance teams is the risk that early stage cloud adoption will compromise existing assets. The above approach allows cloud adoption teams to build and migrate hybrid solutions, with reduced risk to on-premises assets. As trust in the cloud environment increases, later evolutions may remove this temporary solution.

> [!NOTE]
> The above is a starting point to quickly create a baseline governance MVP. This is only the beginning of the governance journey. Further evolution will be needed as the company continues to adopt the cloud and takes on more risk in the following areas:
>
> - Mission-critical workloads
> - Protected data
> - Cost management
> - Multi-cloud scenarios
>
>Moreover, the specific details of this MVP are based on the example journey of a fictitious company, described in the articles that follow. We highly recommend becoming familiar with the other articles in this series before implementing this best practice.
