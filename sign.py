import os
import argparse
import subprocess

def sign(file):
    
    cmd = " ".join(
        [
            "c:/Program Files (x86)/Windows Kits/8.1/bin/x64/signtool.exe", 
            "sign",
            "/debug",
            "/a",
            "/tr",
            "http://rfc3161timestamp.globalsign.com/advanced",
            "/td",
            "SHA256",
            "\"" + os.path.abspath(file) + "\""
        ]
    )
    if 0 != subprocess.call(cmd) :
        raise Exception("can not sign file " + cmd) 

#
# code
#
def main():
    parser = argparse.ArgumentParser(description='Signs MSI installer.')
    parser.add_argument("--msi", help="full path to MSI to sign", required=True)
    
    args = parser.parse_args()    
    sign(args.msi)

#
# entry point
#
main()
