import zipfile
import tempfile
import os
import logging
import subprocess
from pathlib import Path




#logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logging.basicConfig(level=os.environ.get("LOGLEVEL"))
logger = logging.getLogger(__name__)
logging = logging.getLogger("build_validation_log1")




def build_validation(mac_target_dir,mac_zip_name):
    
    
#    zf.extractall()
    logging.info("loop")
    with tempfile.TemporaryDirectory() as tempdir:

        try:

            #setting the zip file and doing extract
            zf = zipfile.ZipFile(os.path.join(mac_target_dir, mac_zip_name))
            zf.extractall(tempdir)

            #getting the tempdirectory path
            temp_dir = Path(tempdir)

            #print("Temp Directory", temp_dir)
            #print("inside directory")
            #files_in_dir = os.listdir(path=tempdir)
            #print(tempdir)
            #print(files_in_dir)

            
            filename = Path(tempdir + "/" + "GoogleChrome.app")
            codesigncommand = "codesign -dvvv " + tempdir +  "/" + "GoogleChrome.app"
            notarycommand = "spctl -v -a " + tempdir +  "/" + "GoogleChrome.app"
            
            codesign_output = subprocess.getoutput(codesigncommand)
            notarize_output = subprocess.getoutput(notarycommand)

            logging.info(codesign_output)
            logging.info(notarize_output)

            if codesign_output.find("Google LLC") !=-1:
                print("Code Sign Sucessful")
            else:
                print("Code Sign Not Sucessful")
            
            if notarize_output.find("accepted") !=-1:
                print("Notarized Sucessful")
            else:
                print("Notarized Unsucessful")
            
        
        except Exception as e:
            logging.error(e)






if __name__ == "__main__":


#    mac_target_dir="dist/mac"
#    mac_zip_name="../1Password-x86_64.zip"
#    build_validation()

#     mac_target_dir="dist/mac-arm64"
#     mac_zip_name="../1Password-aarch64.zip"
#     build_validation()

#     mac_target_dir="dist/mac-universal"
#     mac_zip_name="../1Password.zip"
#     build_validation()
    
    
    
    mac_target_dir="/Users/sureshvankadara/Desktop/test_folder/chrometest"
    mac_zip_name="GoogleChrome.zip"


    try: 
        if (os.path.isdir(mac_target_dir)):
            build_validation(mac_target_dir,mac_zip_name)
        else:
            logging.error("Directory Not Found - " , mac_target_dir)

    except Exception as e:
        logging.error(e)


   