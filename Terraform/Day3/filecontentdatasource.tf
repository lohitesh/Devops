//hello.txt needs to be created before running script

data "local_file" "user_data_script" {
  filename = "/home/ubuntu/hello.txt"
}

resource "null_resource" "display_file_content" {
  # This resource doesn't manage any infrastructure, it's just used to execute local commands
  provisioner "local-exec" {
    command = "echo '${data.local_file.user_data_script.content}'"
  }
}
