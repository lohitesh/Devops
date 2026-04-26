resource "local_file" "pet1" {
 filename = "/home/ubuntu/test1/pet1.txt"
 content = "we love Devops class111"
lifecycle {
        ignore_changes = [
                content
                ]

}
}
#to explain step by step execute below commands
# terraform apply .... once u execute apply it will create file with content we love devops class111
# now change the content of the file via terraform scripts observe below code
resource "local_file" "pet1" {
 filename = "/home/ubuntu/test1/pet1.txt"
 content = "we love Devops class111  Manuall editing"
lifecycle {
        ignore_changes = [
                content
                ]

}
}

#now execute terraform apply ... it will now allow the changes to modifythe content since we have used ignore_changes content
# it will ignore the changes done
