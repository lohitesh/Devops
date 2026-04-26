resource "local_file" "pet" {
 filename = "/home/ubuntu/test1/pet.txt"
 content = "we love Devops class"
lifecycle {
        prevent_destroy = true
}
}


#once resource was created if u try to destroy using terraform destroy it will never destroy the object because we have used prevent_destroy
