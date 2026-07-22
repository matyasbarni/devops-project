# DevOps Engineer Homework

## Overview

The goal of this assignment is to evaluate how you approach a typical DevOps engineering task involving:

- Application development / scripting
- Containerization
- Kubernetes
- Helm
- Terraform
- CI/CD
- Code review

The repository contains intentionally incomplete and imperfect components.
Your task is to complete, improve and document the solution.

You are not expected to produce a perfect production-ready system. We are more interested in your engineering approach, decision-making and ability to balance quality with the time constraints.

Time limit: approximately **3 hours**

## Repository Contents

The repository contains:

- An incomplete application skeleton
- Terraform configuration requiring review and improvement
- An incomplete Helm chart
- An incomplete CI/CD pipeline

Your task is to complete and improve these components. Our goal is to understand your engineering approach, and we will build the upcoming technical interview on this project.

## Goal 1

Complete and improve the provided project.

The repository contains the following files:

- Incomplete application code
- Broken/incomplete terraform configuration
- Incomplete Helm Chart
- Incomplete Gitlab CI pipeline

### Requirements

#### Application

Implement a simple application in either:

- Go
- Python

The application must expose the following endpoints:

##### `GET /health`

**Response:**

```json
{
    "status": "ok"
}
```

##### `GET /version`

**Response:**

```json
{
    "version": "1.0.0"
}
```

##### `GET /env`

**Response:**

```json
{
    "environment": "<value from ENVIRONMENT variable>"
}
```

##### `POST /config`

**Request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `GET /config/{name}`

**Example:**

```bash
GET /config/database_url
```

**Response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

##### `DELETE /config/{name}`

**Response:**

```json
{
    "deleted": true
}
```

#### Containerization

- Create the necessary Dockerfile with minimal setup
- The image should:
  - build successfully
  - run locally
  - expose the application endpoint

#### Terraform

- Review and fix/complete the Terraform code
- The Terraform code contains several issues and areas for improvement
- In case you don't get time to implement changes describe what would you still improve and why
- Document any changes you make

#### Helm

- Review and fix/complete the Helm Chart
- The chart should deploy the application to Kubernetes
- Document any change you make

#### Gitlab CI

- Complete the pipeline so it becomes capable of building and deploying the application
- The pipeline should support the workflow required to build and deploy the application
- The pipeline should be logically complete and demonstrate how you would automate the process
- Add any other necessary jobs to the pipeline

#### Documentation

Update the project README with following information.

##### What You Changed

- Created a simple Flask service that exposes the required endpoints. They can be tested locally through port-forwarding.
- Created a dockerfile for the containerization of the python app so it can be built with docker and deployed on k8s with a tf helm release.
- Fixed the terraform errors and gave env and image setting to helm since missing proper cicd workflow.
- Made adjustments to Helm templates for a more robust release. Made ingress disabled since local usage. Adjusted values.yaml to support current state of the chart.
- Reworked the pipeline yaml, focusing on implementing necessary principles which could be improved in the future, in order to enable a proper cicd workflow.

##### Assumptions

The assignment was comprehensive and covered well the key areas that could realistically be demonstrated in a home environment. Although the result is understandably far from the level of a production-ready solution, it was fascinating to see how much planning and attention to detail is required to build even a relatively simple workflow from its individual components.
To shape it into a complete, more robust solution, it would still require a significant amount of work. As it stands right now, it is primarily suitable for local testing rather than practical use. That said, there is huge potential for further refinement, particularly in the design and optimization of the pipeline, which could easily become an extensive project on its own...

##### Known Limitations

I intentionally omitted creating a properly working cicd workflow, because that could not be fitted into the time window of the project and the available resources. The main purpose of the ci.yaml is only to broadly demonstrate its usage. That said proper environmental branching and image building is left for future improvements. Also integrating gitops methodology for continuous deployment would also be needed for production usage. Creating tests for the application that runs with pytest was also a feature I intentionally left out for now.

##### Production Improvements

- Setting up a proper pipeline for building, testing, analysing and pushing images based on branches
- Integrating an image registry
- Deploying it into an AKS cluster rather than minikube
- Setting up a gitops workflow using argocd for deploying the application and all of its components
- Creating an underlying azure infrastructure containing keyvault for secrets, storage account for remote state, networking for the provided ingress enablement etc. based on the requirements of the project
- Adding unit tests to the application
- Integrating a static code analysis tool that gets triggered from the pipeline (for example SonarQube)
- Adding persistent storage
- Add logging, metrics exposure

### Deliverables

- Source Code of the Go/Python application
- Dockerfile
- Terraform changes
- Helm changes
- CI pipeline changes
- README describing decisions, assumptions and user guide for the project.

### Notes

You are not expected to deploy to a cloud provider.
The solution should work with a local Kubernetes cluster such as:

- Kind
- Minikube
- K3d

### Timing

Timebox yourself to approximately **3 hours**. If you can't finish the work within the timebox, describe in the README.md what is left and how you would approach it.

## Goal 2

You get this half-baked project from one of your colleagues who is a Junior and asking for your guidance.

Provide a short code review in `REVIEW.md` where you address the **top 5 most important things** to fix so the colleague can move forward.

### Review Timing

Spend no more than **30 minutes** on review and feedback.

### Evaluation Criteria

We will evaluate:

- Code quality
- Terraform quality
- Kubernetes and Helm knowledge
- CI/CD design and implementation
- Documentation quality
- Code review quality
- Maintainability and operational thinking

### Use of AI

The use of AI-assisted tools is permitted. However, we encourage you to complete the assignment primarily based on your own knowledge, experience and reasoning. During the interview, we will discuss your implementation choices, trade-offs and decision-making process, so it is important that you fully understand and can explain every part of your solution.