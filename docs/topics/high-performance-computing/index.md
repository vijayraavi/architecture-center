---
title: High Performance Computing (HPC) on Azure
description: A guide to building running HPC workloads on Azure
author: adamboeglin
ms.date: 12/03/2018
layout: LandingPage
ms.topic: landing-page
---
# High Performance Computing (HPC) on Azure

## Introduction to HPC

Brief introduction to HPC to set the context.

> [!VIDEO https://www.youtube.com/embed/rKURT32faJk]

### Problems solved with High Performance Computing

Many industries:

- Genomics
- Oil & Gas
- Finance
- Semiconductor Design
- Engineering
- Weather modeling

### How is HPC different on the cloud

- [Big Compute Architecture Style](/azure/architecture/guide/architecture-styles/big-compute?toc=/azure/architecture/topics/high-performance-computing/toc.json)
- Dynamic Scaling
- Pay for only what you use

### Architecture Guidance

There are a number of different ways to design and implement your HPC architecture on Azure.  The following scenarios outline a few of the common ways HPC solutions are built.

<ul class="panelContent cardsC">
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/apps/hpc-saas.md?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/apps/media/architecture-hpc-saas.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>A computer-aided engineering service on Azure</h3>
                        <p>Provide a software-as-a-service (SaaS) platform for computer-aided engineering (CAE) on Azure.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/hpc-cfd.md?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardImageOuter">
                        <div class="cardImage">
                            <img src="../../example-scenario/infrastructure/media/architecture-hpc-cfd.png" height="140px" />
                        </div>
                    </div>
                    <div class="cardText">
                        <h3>Running computational fluid dynamics (CFD) simulations on Azure</h3>
                        <p>Execute computational fluid dynamics (CFD) simulations on Azure.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/video-rendering.md?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
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

## Infrastructure

### Networking

- Infiniband Network
- High speed VM networking

### Compute

Details on popular VM sizes used for HPC and the different capabilities of them

- GPU Servers

- Cray Supercomputers

### Storage

- Avere for hybrid
- BeeGFS
- Object storage for HPC
- Local NVMe SSD's

## Management

- [Microsoft HPC Pack](https://docs.microsoft.com/en-us/powershell/high-performance-computing/overview?view=hpc16-ps)
- [Azure Batch](https://docs.microsoft.com/en-us/azure/batch/)
- Cycle Cloud
- [Alces Flight](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/alces-flight-limited.alces-flight-compute-solo?tab=overview%3Fwt.mc_id%3Dcomputeinmanufacturing-docs-ercenk)

- https://azure.microsoft.com/en-us/blog/tibco-datasynapse-comes-to-the-azure-marketplace/?WT.mc_id=computeinmanufacturing-docs-ercenk
- http://www.brightcomputing.com/technology-partners/microsoft
- https://azure.microsoft.com/en-us/blog/ibm-and-microsoft-azure-support-spectrum-symphony-and-spectrum-lsf/?WT.mc_id=computeinmanufacturing-docs-ercenk
- https://www.pbspro.org/

## Cloud Bursting

- Architectures for hybrid network
- Information on Azure VPN
- Guide on ExpressRoute

## Cost Management

- Low priority VM's
- Upfront commitments
- Discounts when you use microsoft products

## Authentication

- Centralized user management for Linux & Windows

## Supported Applications & Partners

Logo's of applications & vendors that we have relationships and experience with that link to relevant case studies or materials
- [StarCCM+](https://azure.microsoft.com/en-us/blog/availability-of-star-ccm-on-microsoft-azure/?WT.mc_id=computeinmanufacturing-docs-ercenk)

- [Microsoft MPI](https://docs.microsoft.com/en-us/message-passing-interface/microsoft-mpi)

## Remote Visualization

<ul class="panelContent cardsC">
<li style="display: flex; flex-direction: column;">
    <a href="/azure/architecture/example-scenario/infrastructure/linux-vdi-citrix.md?toc=/azure/architecture/topics/high-performance-computing/toc.json" style="display: flex; flex-direction: column; flex: 1 0 auto;">
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

- [Compute Benchmarks](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/compute-benchmark-scores)
- Benchmarks for performance for various applications

## Customer References & Stories

- Customer references

## Partners & Consultants

- HPC software on Azure marketplace
- Integration partners & consulting firms

## Other Links
- [Compute HPC Page](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/high-performance-computing?WT.mc_id=computeinmanufacturing-docs-ercenk)
