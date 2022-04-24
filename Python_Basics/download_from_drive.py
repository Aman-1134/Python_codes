from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1m01_27QKaoEv_WueLzqqfmPb9CvVvmXn'

# Upload files
directory = "D:/haddi"

# Download files
file_list = drive.ListFile({'q': f"'{folder}' in parents and trashed=false"}).GetList()

for index, file in enumerate(file_list):
	print(index+1, 'file downloaded : ', file['title'])
	file.GetContentFile(file['title'])
	try:
		file.Delete()
	except OSError:
		print('File cant be deleted')
	else:
		print('File Deleted Succesfully')
