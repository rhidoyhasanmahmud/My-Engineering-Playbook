# AWS & cloud roadmap

[All roadmaps](README.md) · [AWS notes](../notes/aws/README.md)

**Goal:** Understand cloud fundamentals and explain architecture choices in terms of availability, security and cost.

**Prerequisites:** Basic backend concepts and a general understanding of servers, storage and networking. An AWS account is not required to read the current notes.

| Step | Topic | Study material | Status | Practical checkpoint |
| --- | --- | --- | --- | --- |
| 1 | Cloud concepts and service models | [Cloud computing basics](../notes/aws/saa-c03/03-cloud-computing-basics.md) | Draft | Compare IaaS, PaaS and SaaS; distinguish scalability from elasticity |
| 2 | AWS foundations | [AWS basics](../notes/aws/saa-c03/04-aws-basics.md) | Draft | Explain Regions, Availability Zones and shared responsibility |
| 3 | Identity and networking | Notes to be written | Planned | Sketch a network boundary and describe least-privilege access |
| 4 | Compute, storage and databases | Notes to be written | Planned | Choose services for a small application and explain the alternatives |
| 5 | Resilience and cost | Notes to be written | Planned | Describe failure recovery, RTO/RPO and the main cost drivers |
| 6 | Architecture practice | Lab to be written | Planned | Design a small backend deployment and explain its security and availability choices |

## Optional background and certification reading

- [History of AWS](../notes/aws/saa-c03/02-history-of-aws.md): optional background, retained as a draft.
- [Existing SAA-C03 exam notes](../notes/aws/saa-c03/01-exam-details.md): historical study material. Check the [current official certification page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) before relying on exam codes, fees, policies or domain weights.

The `saa-c03` folder preserves the original collection's context. This roadmap is a cloud learning path, not a claim that the repository covers a complete or current certification syllabus.

## Suggested application

Draw a deployment for a small web API with a database. Explain access, credentials, component failures and cost drivers. Deployment instructions and an automated lab are still planned.
