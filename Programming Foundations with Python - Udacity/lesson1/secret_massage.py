import os
def secret_msg():
    file_msg = os.listdir(r"E:\Programming\UdacityCource\Python\prank\alphabet")
    saved_path = os.getcwd()
    os.chdir(r"E:\Programming\UdacityCource\Python\prank\alphabet")

    for secret_massage in file_msg:
        os.rename(secret_massage,secret_massage.translate(None,"0123456789"))
        os.chdir(saved_path)

        secret_msg()
