If i need to create a differenct workspace for different environment then we need to use workspace concept

if we r not using the worksapce concept then it will never create resource for different environment like dev, prod, stage.. instead of that it will update the same resources.


terraform workspace new dev ----- create workspace
terraform workspace delete dev ----- delete workspace

terraform workspace select dev ---- switch to specific workspace

terraform workspace list -- list all worksapce
