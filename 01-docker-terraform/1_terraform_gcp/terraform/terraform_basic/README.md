markdown
# Terraform Basic - Google Cloud Setup

This project demonstrates basic Terraform usage to create Google Cloud resources.

## What I Learned

* **Providers:** Defined the `google` provider to interact with Google Cloud.
* **Resources:** Created a Cloud Storage bucket (`google_storage_bucket`) and a BigQuery dataset (`google_bigquery_dataset`).
* **Configuration:** Configured bucket settings like location, storage class, versioning, and lifecycle rules.
* **Project and Region:** Set the Google Cloud project and region for resource deployment.

## Usage

1.  **Replace Placeholders:** Update `<Your Project ID>` and `<Your Unique Bucket Name>` in `main.tf`.
2.  **Initialize Terraform:** Run `terraform init`.
3.  **Apply Changes:** Run `terraform apply`.