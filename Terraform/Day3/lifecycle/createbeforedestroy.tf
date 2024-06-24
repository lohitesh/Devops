resource "local_file" "pet" {
 filename = "/home/ubuntu/test1/pet.txt"
 content = "we love Devops"
lifecycle {
        create_before_destroy = true
}
}
