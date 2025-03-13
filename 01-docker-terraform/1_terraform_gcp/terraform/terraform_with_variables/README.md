markdown
# My First Steps with Terraform and Google Cloud Platform (GCP)

This project demonstrates infrastructure as code (IaC) principles using Terraform and Google Cloud Platform (GCP). Key demonstrations include:

* Terraform fundamentals: providers, resources, state management.
* GCP setup: project configuration and service accounts.
* GCP service provisioning: Cloud Storage (GCS) and BigQuery.
* Access control: IAM roles and permissions.

Here's a breakdown of what I've learned...

## What I'm Learning

* **Terraform Basics:**
    * I'm getting to grips with what Terraform is and why it's super useful.
    * I've started to understand key Terraform concepts like providers, resources, and how Terraform keeps track of things with its state.
    * I'm practicing the Terraform workflow: `init`, `plan`, `apply`, and `destroy`.
* **Google Cloud Platform (GCP) Fundamentals:**
    * I've learned how to set up a GCP project and create service accounts.
    * I'm exploring GCP services like Google Cloud Storage (GCS) and BigQuery.
    * I am learning how to manage IAM roles and permissions.
* **Hands-on Practice:**
    * I'm using Terraform to create real GCP infrastructure.
    * I'm getting hands-on experience creating storage buckets and BigQuery datasets/tables.

## Concepts I've Encountered

* **Terraform Overview:**
    * I've looked into the core concepts of Terraform and IaC.
    * You can find my notes in the [Terraform Overview Document](1_terraform_overview.md).
    * [Video](https://www.youtube.com/watch?v=18jIzE41fJ4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=2)
* **GCP Overview:**
    * I've started learning about Google Cloud Platform and the services I'm using.
    * [Video](https://www.youtube.com/watch?v=18jIzE41fJ4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=2)

## My Local Setup

### Things I Needed

1.  **Terraform:**
    * I downloaded and installed Terraform from the official website: [Terraform Downloads](https://www.terraform.io/downloads).
2.  **Google Cloud Account:**
    * I created a free GCP account (up to EUR 300 credits) to start experimenting: [Google Cloud Console](https://console.cloud.google.com/).

### My Steps

1.  **GCP Setup:**
    * I followed the instructions in the [GCP Overview Document](2_gcp_overview.md#initial-setup) to set up my GCP project and service account.
    * I had to look at the [Windows Setup Document](windows.md) because I am using windows, and it helped me with the google cloud sdk.
2.  **IAM and Access:**
    * I configured IAM roles and enabled the necessary APIs as shown in the [GCP Overview Document](2_gcp_overview.md#setup-for-access).
3.  **Authentication:**
    * I set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to my service account key file.

    bash
    export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
    gcloud auth application-default login
    

## Running Terraform

### What I'm Working With

* `main.tf`: This is where I'm putting the main Terraform configuration, defining the resources I want to create.
* `variables.tf`: I'm using this to define input variables for my configuration.
* `terraform`: this is the directory that holds all of my terraform files.
* `.tfstate`: Terraform uses this file to keep track of the infrastructure it manages.

### My Execution Steps

1.  **Initialize Terraform:**

    bash
    terraform init
    

    * This sets up my working directory, downloads providers, and configures the backend.

2.  **Plan Changes:**

    bash
    terraform plan -var="project=<my-gcp-project-id>"
    

    * This shows me what Terraform will change in my infrastructure. I replace `<my-gcp-project-id>` with my actual GCP project ID.

3.  **Apply Changes:**

    bash
    terraform apply -var="project=<my-gcp-project-id>"
    

    * This applies the changes to create the infrastructure. I always double-check the plan before confirming.

4.  **Destroy Infrastructure:**

    bash
    terraform destroy -var="project=<my-gcp-project-id>"
    

    * This removes the infrastructure. I use it when I'm finished to avoid any unnecessary costs.

## Windows Specifics

If you are using a plain windows environment, without WSL, please refer to the [GCP and Terraform on Windows](windows.md) document for extra setup steps.

## Resources I'm Using

* **HashiCorp Learn:** [Terraform on GCP Getting Started](https://learn.hashicorp.com/collections/terraform/gcp-get-started)
* **GCP Documentation:** [Google Cloud Documentation](https://cloud.google.com/docs)

I'm excited to continue learning and building with Terraform and GCP!