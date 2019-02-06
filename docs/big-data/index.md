---
title: Building big data architectures on Azure
description: Building big data architectures on Azure
ms.date: 10/23/2018
layout: LandingPage
ms.topic: landing-page
---

# Building big data architectures on Azure

<!-- markdownlint-disable MD033 -->

<img src="../_images/data-guide.svg" style="float:left; margin-top:8px; margin-right:8px;"/>

A big data architecture is designed to handle the ingestion, processing, and analysis of data that is too large or complex for traditional database systems.

<ul  class="panelContent cardsZ">
<li style="display: flex; flex-direction: column;">
    <a href="../data-guide/big-data/index.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>What is a big data architecture?</h3>
                        <p>This article describes the logical components that fit into a big data architecture.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
</ul>

## Data warehouses

<ul  class="panelContent cardsZ">
<li style="display: flex; flex-direction: column;">
    <a href="../data-guide/relational-data/data-warehousing.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Overview of data warehousing</h3>
                        <p>A data warehouse is a central, organizational, relational repository of integrated data.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../data-guide/relational-data/etl.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Overview of ETL (extract, transform, and load) processing</h3>
                        <p>ETL is a data pipeline that collects data from various sources, transforms it according to business rules, and loads it into a data store.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../reference-architectures/data/enterprise-bi-sqldw.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Enterprise BI in Azure with SQL Data Warehouse</h3>
                        <p>This reference architecture implements an extract, load, and transform (ELT) pipeline that moves data from SQL Server into SQL Data Warehouse for analysis.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../reference-architectures/data/enterprise-bi-adf.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Automated enterprise BI with SQL Data Warehouse and Azure Data Factory</h3>
                        <p>This reference architecture shows how to automate an ELT pipeline using Azure Data Factory.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../reference-architectures/data/enterprise-bi-adf.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Hybrid ETL with existing on-premises SSIS and Azure Data Factory</h3>
                        <p>This example discusses using existing SQL Server Integration Services (SSIS) packages as part of a cloud data workflow.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
</ul>

## Real-time stream processing

<ul  class="panelContent cardsZ">
<li style="display: flex; flex-direction: column;">
    <a href="../data-guide/relational-data/data-warehousing.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Overview of real-time processing architectures</h3>
                        <p>Real-time processing captures steams of data in real-time and processes them with minimal latency.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../reference-architectures/data/stream-processing-databricks.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Stream processing with Azure Databricks</h3>
                        <p>This reference architecture shows an end-to-end stream processing pipeline using Spark on Azure Databricks.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../reference-architectures/data/stream-processing-stream-analytics.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>Stream processing with Azure Stream Analytics</h3>
                        <p>This reference architecture shows an end-to-end stream processing pipeline using Azure Stream Analytics.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
<li style="display: flex; flex-direction: column;">
    <a href="../microservices/ingestion-workflow.md" style="display: flex; flex-direction: column; flex: 1 0 auto;">
        <div class="cardSize" style="flex: 1 0 auto; display: flex;">
            <div class="cardPadding" style="display: flex;">
                <div class="card">
                    <div class="cardText">
                        <h3>High-scale message ingestion with Event Hubs</h3>
                        <p>Use Event Hubs to manage a workflow at very high throughput.</p>
                    </div>
                </div>
            </div>
        </div>
    </a>
</li>
</ul>
