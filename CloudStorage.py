# This app helps uploading files to dropbox directly and in a easier way instead of going though a lot of complicated steps.

import dropbox

class MoveFiles:
    def __init__(self, token):
        self.token = token

    def upload_file(self, original_place, destination):
    
        dropBox = dropbox.Dropbox(self.token)

        with open(destination, 'rb') as f:
            dropBox.files_upload(f.read(), destination)

def main():
    token = "XtpS0CoAGZoAAAAAAAAAATDzdrCVcorTE6OlhVKrtZDYM8NYzK5C0y6_kpjDHMmc"
    moveFiles = MoveFiles(token)

    original_place = input("Enter the file name you want to upload: ")
    destination = input("Enter the full path to dropbox: ") 

    
    moveFiles.upload_file(original_place, destination)

main()
