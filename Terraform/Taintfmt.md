Terraform fmt: If any indentation is not correct in terraform files then terraform fmt command will be used to make indentation correct for all terraform files..

Syntax: Terraform fmt

Terraform taint: 
The terraform taint command informs Terraform that a particular object has become degraded or damaged. Terraform represents this by marking the object as "tainted" in the Terraform state, and Terraform will propose to replace it in the next plan you create. once u execute terraform apply then it will destroy and recreate the resources

terraform taint aws_instance.web

