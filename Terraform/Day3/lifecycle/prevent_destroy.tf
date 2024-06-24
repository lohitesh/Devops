resource "local_file" "pet" {
 filename = "/home/ubuntu/test1/pet.txt"
 content = "we love Devops class"
lifecycle {
        prevent_destroy = true
}
}
