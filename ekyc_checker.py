aadhar = input("AADHAR submitted ?(yes/no):").lower()
pan = input("PAN Submitted(yes/no):").lower()
photo = input("Photo submitted (yes/no):").lower()

if aadhar=="no":
    print("Missing aadhar pls. visit the branch")
if pan=="no":
    print("Missing PAN pls. visit the branch")
if photo=="no":
    print("Missing photo pls. visit the branch")

if aadhar=="yes" and pan=="yes" and photo=="yes":
    print("e-KYC Completed")