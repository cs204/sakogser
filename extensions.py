filename = input("File name: ")
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith((".jpg", "jpeg")):
    print("image/jpeg")
elif filename.endswith((".png")):
    print("image/png")
elif filename.endswith((".pdf")):
    print("application/pdf")
elif filename.endswith((".txt")):
    print("text/plain")
elif filename.endswith(("/zip")):
    print("application/zip")
else:
    print("application/octet-stream")