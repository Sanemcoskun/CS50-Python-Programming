file = input("File name: ").strip().lower()
extension = file.split(".")[-1] #noktadan sonraki eki aldı

if extension == "gif":
    print("image/gif")
elif extension == "jpg" or extension == "jpeg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
    
#Başka bir yöntem
    
# def main():
#     # Dictionary mapping file extensions to media types
#     media_types = {
#         ".gif": "image/gif",
#         ".jpg": "image/jpeg",
#         ".jpeg": "image/jpeg",
#         ".png": "image/png",
#         ".pdf": "application/pdf",
#         ".txt": "text/plain",
#         ".zip": "application/zip"
#     }

#     # Prompt user for file name
#     file_name = input("Enter the name of the file: ").strip()

#     # Extract file extension
#     file_extension = file_name.lower().split(".")[-1]

#     # Look up media type in the dictionary
#     media_type = media_types.get("." + file_extension, "application/octet-stream")

#     # Output the media type
#     print("Media type:", media_type)

# if __name__ == "__main__":
#     main()

    