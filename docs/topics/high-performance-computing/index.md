---
title: High Performance Computing (HPC) on Azure
description: A guide to building running HPC workloads on Azure
author: adamboeglin
ms.date: 12/03/2018
zone_pivot_groups: platform
---

# High Performance Computing (HPC) on Azure

## Introduction to HPC

High Performance Computing (HPC), also called "Big Compute", is the process of using a large number of coordinated CPU or GPU based computers to solve complex mathematical tasks to solve a wide number of problems.

> [!VIDEO https://www.youtube.com/embed/rKURT32faJk]

::: zone pivot="linux"

### HPC industries and workloads

Many industries use HPC to solve some of their most difficult problems.  These include things like:

- Genomics
- Oil & Gas Simulations
- Finance
- Semiconductor Design
- Engineering
- Weather modeling

::: zone-end

::: zone pivot="windows"

### How is HPC different on the cloud

One of the differences between an on-premise HPC system and one in the cloud is that cloud resources can dynamically be added and removed as they're needed.  This moves your bottleneck away from available compute cores and instead focuses on right sizing your infrastructure to the requirements of your job.

The following articles provide more detail about this dynamic scaling capability.

- [Big Compute Architecture Style](/azure/architecture/guide/architecture-styles/big-compute?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Autoscaling best practices](/azure/architecture/best-practices/auto-scaling?toc=/azure/architecture/topics/high-performance-computing/toc.json)

::: zone-end

## Implementation Checklist

Ensure you're reviewed the following areas while building your HPC solution on Azure

- [ ] Choose the appropriate [architecture](#Infrastructure) based on your requirements
  - [ ] Know which [Compute](#compute) options is right for your workload
  - [ ] Identify the right [storage](#storage) solution that meets your needs
- [ ] Decide how you're going to [manage](#manage) all your resources
- [ ] Optimize your [application](#applications) for the cloud
- [ ] [Secure](#security) your Infrastructure

## Infrastructure

There are a number of infrastructure components necessary to build a HPC system.  Compute, Storage, and Networking provide the underlying components, no matter how you choose to manage your HPC workloads.

### Example HPC Architectures

There are a number of different ways to design and implement your HPC architecture on Azure.  High performance computing (HPC) applications can scale to thousands of compute cores, extend on-premises big compute, or run as a 100% cloud native solution.

The following scenarios outline a few of the common ways HPC solutions are built.

<ul class="panelContent cardsC">
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/apps/hpc-saas?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/apps/media/architecture-hpc-saas.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>Computer-aided engineering services on Azure</h3>
                        <p>Provide a software-as-a-service (SaaS) platform for computer-aided engineering (CAE) on Azure.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/hpc-cfd?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/infrastructure/media/architecture-hpc-cfd.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>Computational fluid dynamics (CFD) simulations on Azure</h3>
                        <p>Execute computational fluid dynamics (CFD) simulations on Azure.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/video-rendering?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/infrastructure/media/architecture-video-rendering.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>3D video rendering on Azure</h3>
                        <p>Run native HPC workloads in Azure using the Azure Batch service.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
</ul>

### Compute

Azure offers a range of sizes for compute-intensive workloads. For example, H16r and H16mr VMs can connect to a high throughput back-end RDMA network. This cloud network can improve the performance of tightly coupled parallel applications running under [Microsoft MPI](https://msdn.microsoft.com/library/bb524831.aspx) or Intel MPI.

N-series VMs feature NVIDIA GPUs designed for compute-intensive or graphics-intensive applications including artificial intelligence (AI) learning and visualization.

#### CPU based virtual machines
- [Linux HPC VM's](https://docs.microsoft.com/azure/virtual-machines/linux/sizes-hpc?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Windows HPC VM's](https://docs.microsoft.com/azure/virtual-machines/windows/sizes-hpc?toc=/azure/architecture/topics/high-performance-computing/toc.json) VMs
  
#### GPU-enabled virtual machines
- [Linux GPU VMs](https://docs.microsoft.com/azure/virtual-machines/linux/sizes-gpu?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Windows GPU VMs](https://docs.microsoft.com/azure/virtual-machines/windows/sizes-gpu?toc=/azure/architecture/topics/high-performance-computing/toc.json)

### Storage

Large-scale Batch and HPC workloads have demands for data storage and access that exceed the capabilities of traditional cloud file systems.  There are a number of solutions to manage both the speed and capacity needs of HPC applications on Azure

- [Parallel virtual file systems on Azure](https://azure.microsoft.com/resources/parallel-virtual-file-systems-on-microsoft-azure/)
- High performance cloud storage solutions from [Avere](http://www.averesystems.com/about-us/about-avere)
- BeeGFS
- Local NVMe SSDs
- [Blob, table, and queue storage](https://docs.microsoft.com/azure/storage/storage-introduction?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Azure File sstorage](https://docs.microsoft.com/azure/storage/storage-files-introduction?toc=/azure/architecture/topics/high-performance-computing/toc.json) offers fully managed file shares accessible via the Server Message Block (SMB) protocol

### Networking

- Infiniband Network
- [Virtual Network](https://docs.microsoft.com/azure/virtual-network/virtual-networks-overview?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [ExpressRoute](https://docs.microsoft.com/azure/expressroute/expressroute-introduction?toc=/azure/architecture/topics/high-performance-computing/toc.json)

### Containers
- [Container Service](https://docs.microsoft.com/azure/container-service/dcos-swarm/container-service-intro?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/azure/aks/intro-kubernetes?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Container Registry](https://docs.microsoft.com/azure/container-registry/container-registry-intro?toc=/azure/architecture/topics/high-performance-computing/toc.json)

## Management

### Do-it-yourself

Building an HPC system from scratch on Azure offers a significant amount of flexability, but is often very maintenance intensive.  

1. Set up your own cluster environment in Azure virtual machines or [virtual machine scale sets](https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-overview?toc=/azure/architecture/topics/high-performance-computing/toc.json).
2. Use Azure Resource Manager templates to deploy leading [workload managers](#workload-managers), infrastructure, and [applications](#hpc-applications).
3. Choose [HPC and GPU VM sizes](#hpc-and-gpu-sizes) that include specialized hardware and network connections for MPI or GPU workloads. 
4. Add [high performance storage](#hpc-storage) for I/O-intensive workloads.

### Hybrid & Cloud Bursting

- Architectures for hybrid network
- Information on Azure VPN
- Guide on ExpressRoute
- Extend your on-premises solution to offload ("burst") peak workloads to Azure infrastructure
- Use cloud compute on-demand with your existing [workload manager](#workload-manager).
- Take advantage of [HPC and GPU VM sizes](#hpc-and-gpu-sizes) for MPI or GPU workloads.

### Big Compute solutions as a service

Develop custom Big Compute solutions and workflows using [Azure Batch](#azure-batch) and related [Azure services](#related-azure-services).

- Run Azure-enabled engineering and simulation solutions from vendors including [Altair](http://www.altair.com/), [Rescale](https://www.rescale.com/azure/), and [Cycle Computing](https://cyclecomputing.com/) (now [joined with Microsoft](https://blogs.microsoft.com/blog/2017/08/15/microsoft-acquires-cycle-computing-accelerate-big-computing-cloud/)).
- Use a [Cray supercomputer](https://www.cray.com/solutions/supercomputing-as-a-service/cray-in-azure) as a service hosted in Azure.

### Marketplace solutions

- Use the scale of [HPC applications](#hpc-applications) and [solutions](#marketplace-solutions) offered in the [Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace/). 
- [RogueWave CentOS-based HPC](https://azuremarketplace.microsoft.com/marketplace/apps/RogueWave.CentOSbased73HPC?tab=Overview)
- [SUSE Linux Enterprise Server for HPC](https://azure.microsoft.com/marketplace/partners/suse/suselinuxenterpriseserver12optimizedforhighperformancecompute/)
-  [TIBCO Grid Server Engine](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/tibco-software.gridserverlinuxengine?tab=Overview)
- [Azure Data Science VM for Windows and Linux](https://docs.microsoft.com/azure/machine-learning/machine-learning-data-science-virtual-machine-overview?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [D3View](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/xfinityinc.d3view-v5?tab=Overview)
- [UberCloud](https://azure.microsoft.com/search/marketplace/?q=ubercloud)
- [Intel Cloud Edition for Lustre](https://azuremarketplace.microsoft.com/marketplace/apps/intel.intel-cloud-edition-gs)

### Azure Batch

[Batch](https://docs.microsoft.com/azure/batch/batch-technical-overview?toc=/azure/architecture/topics/high-performance-computing/toc.json) is a platform service for running large-scale parallel and high-performance computing (HPC) applications efficiently in the cloud. Azure Batch schedules compute-intensive work to run on a managed pool of virtual machines, and can automatically scale compute resources to meet the needs of your jobs. 

SaaS providers or developers can use the Batch SDKs and tools to integrate HPC applications or container workloads with Azure, stage data to Azure, and build job execution pipelines. 

### Workload managers

The following are examples of cluster and workload managers that can run in Azure infrastructure. Create stand-alone clusters in Azure VMs or burst to Azure VMs from an on-premises cluster.

- [Alces Flight Compute](https://azuremarketplace.microsoft.com/marketplace/apps/alces-flight-limited.alces-flight-compute-solo?tab=Overview)
- [TIBCO DataSynapse GridServer](https://azure.microsoft.com/blog/tibco-datasynapse-comes-to-the-azure-marketplace/) 
- [Bright Cluster Manager](http://www.brightcomputing.com/technology-partners/microsoft)
- [IBM Spectrum Symphony and Symphony LSF](https://azure.microsoft.com/blog/ibm-and-microsoft-azure-support-spectrum-symphony-and-spectrum-lsf/)
- [PBS Pro](http://pbspro.org)
- [Microsoft HPC Pack](https://technet.microsoft.com/library/mt744885.aspx)
  - [HPC Pack for Windows](https://docs.microsoft.com/azure/virtual-machines/windows/hpcpack-cluster-options.md?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json)
  - [HPC Pack for Linux](https://docs.microsoft.com/azure/virtual-machines/linux/hpcpack-cluster-options.md?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json)

### Partners & Consultants

- HPC software on Azure marketplace
- Integration partners & consulting firms

### Misc

- Cycle Cloud
- [Alces Flight](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/alces-flight-limited.alces-flight-compute-solo?tab=overview%3Fwt.mc_id%3Dcomputeinmanufacturing-docs-ercenk)
- [Microsoft MPI](https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi)
- https://azure.microsoft.com/en-us/blog/tibco-datasynapse-comes-to-the-azure-marketplace/?WT.mc_id=computeinmanufacturing-docs-ercenk
- http://www.brightcomputing.com/technology-partners/microsoft
- https://azure.microsoft.com/en-us/blog/ibm-and-microsoft-azure-support-spectrum-symphony-and-spectrum-lsf/?WT.mc_id=computeinmanufacturing-docs-ercenk

## Cost Management

Managing your HPC cost on Azure can be done through a few different ways.

- [Low priority VM's](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-use-low-priority?toc=/azure/architecture/topics/high-performance-computing/toc.json)  allows you to take advantage of our unutilized capacity at a significant cost savings.
- Upfront commitments
- Discounts when you use microsoft products

## Security

- Centralized user management for Linux & Windows
- Network Isolation
- ExpressRoute
- VPN

## HPC applications

Run custom or commercial HPC applications in Azure. Several examples in this section are benchmarked to scale efficiently with additional VMs or compute cores. Visit the [Azure Marketplace](https://azuremarketplace.microsoft.com/marketplace) for ready-to-deploy solutions.

> [!NOTE]
> Check with the vendor of any commercial application for licensing or other restrictions for running in the cloud. Not all vendors offer pay-as-you-go licensing. You might need a licensing server in the cloud for your solution, or connect to an on-premises license server.

### Engineering applications

- [Altair RADIOSS](https://azure.microsoft.com/blog/availability-of-altair-radioss-rdma-on-microsoft-azure/)
- [ANSYS CFD](https://azure.microsoft.com/blog/ansys-cfd-and-microsoft-azure-perform-the-best-hpc-scalability-in-the-cloud/)
- [MATLAB Distributed Computing Server](https://docs.microsoft.com/azure/virtual-machines/windows/matlab-mdcs-cluster?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [StarCCM+](https://blogs.msdn.microsoft.com/azurecat/2017/07/07/run-star-ccm-in-an-azure-hpc-cluster/)
- [OpenFOAM](https://simulation.azure.com/casestudies/Team-182-ABB-UC-Final.pdf)

### Graphics and rendering

- [Autodesk Maya, 3ds Max, and Arnold](https://docs.microsoft.com/azure/batch/batch-rendering-service?toc=/azure/architecture/topics/high-performance-computing/toc.json) on Azure Batch

### AI and deep learning

- [Microsoft Cognitive Toolkit](https://docs.microsoft.com/cognitive-toolkit/cntk-on-azure)
- [Deep Learning VM](https://azuremarketplace.microsoft.com/marketplace/apps/microsoft-ads.dsvm-deep-learning)
- [Batch Shipyard recipes for deep learning](https://github.com/Azure/batch-shipyard/tree/master/recipes#deeplearning)

## Remote Visualization

<ul class="panelContent cardsC">
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/linux-vdi-citrix?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/infrastructure/media/azure-citrix-sample-diagram.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>Linux virtual desktops with Citrix</h3>
                        <p>Build a VDI environment for Linux Desktops using Citrix on Azure.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
</ul>

## Performance Benchmarks

- [Compute Benchmarks](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/compute-benchmark-scores?toc=/azure/architecture/topics/high-performance-computing/toc.json)

## Customer stories

Examples of customers that have solved business problems with Azure HPC solutions:

- [ANEO](https://customers.microsoft.com/story/it-provider-finds-highly-scalable-cloud-based-hpc-redu) 
- [AXA Global P&C](https://customers.microsoft.com/story/axa-global-p-and-c)
- [Axioma](https://customers.microsoft.com/story/axioma-delivers-fintechs-first-born-in-the-cloud-multi-asset-class-enterprise-risk-solution)
- [d3View](https://customers.microsoft.com/story/big-data-solution-provider-adopts-new-cloud-gains-thou)
- [EFS](https://customers.microsoft.com/story/efs-professionalservices-azure)
- [Hymans Robertson](https://customers.microsoft.com/story/hymans-robertson)
- [MetLife](https://enterprise.microsoft.com/en-us/customer-story/industries/insurance/metlife/)
- [Microsoft Research](https://customers.microsoft.com/doclink/fast-lmm-and-windows-azure-put-genetics-research-on-fa)
- [Milliman](https://customers.microsoft.com/story/actuarial-firm-works-to-transform-insurance-industry-w)
- [Mitsubishi UFJ Securities International](https://customers.microsoft.com/story/powering-risk-compute-grids-in-the-cloud)
- [NeuroInitiative](https://customers.microsoft.com/en-us/story/neuroinitiative-health-provider-azure)
- [Schlumberger](https://azure.microsoft.com/blog/big-compute-for-large-engineering-simulations)
- [Towers Watson](https://customers.microsoft.com/story/insurance-tech-provider-delivers-disruptive-solutions)

## Other Important Information

- Ensure your [vCPU quota](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quotas?toc=/azure/architecture/topics/high-performance-computing/toc.json) has been increased before attempting to run large scale workloads.

## Next steps

For the latest announcements, see:
  - [Microsoft HPC and Batch team blog](http://blogs.technet.com/b/windowshpc/)
  - [Azure blog](https://azure.microsoft.com/blog/tag/hpc/).
- [Set up a Linux RDMA cluster to run MPI applications](https://docs.microsoft.com/azure/virtual-machines/linux/classic/rdma-cluster.md?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Set up a Windows RDMA cluster with Microsoft HPC Pack to run MPI applications](https://docs.microsoft.com/azure/virtual-machines/windows/classic/hpcpack-rdma-cluster.md?toc=/azure/architecture/topics/high-performance-computing/toc.json)

### Microsoft Batch Examples

These tutorials will provide you with details on running applications on Microsoft Batch

- [Get started developing with Batch](https://docs.microsoft.com/azure/batch/quick-run-dotnet?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Use Azure Batch code samples](https://github.com/Azure/azure-batch-samples)
- [Use low-priority VMs with Batch](https://docs.microsoft.com/azure/batch/batch-low-pri-vms?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- [Run containerized HPC workloads with Batch Shipyard](https://github.com/Azure/batch-shipyard)
- [Run parallel R workloads on Batch](https://github.com/Azure/doAzureParallel)
- [Run on-demand Spark jobs on Batch](https://github.com/Azure/aztk)
- [Use compute-intensive VMs in Batch pools](https://docs.microsoft.com/azure/batch/batch-pool-compute-intensive-sizes?toc=/azure/architecture/topics/high-performance-computing/toc.json)