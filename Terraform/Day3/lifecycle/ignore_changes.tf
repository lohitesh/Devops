resource "local_file" "pet1" {
 filename = "/home/ubuntu/test1/pet1.txt"
 content = "we love Devops class111"
lifecycle {
        ignore_changes = [
                content
                ]

}
}
