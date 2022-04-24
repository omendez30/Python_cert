#!/usr/bin/env python3

#import libraries

import requests
import shutil
import crayons


#set the Astronomy picture of the day API key to a constant
APOD_API = "https://api.nasa.gov/planetary/apod"

#This function will download the photo of the day to you current directory

def img_download(url):
	see_photo = input("Would you like to see today Astronomy photo of the day? Y/N: ").lower()
	
	if see_photo == 'y':
		file_name = input("Save image as (string): ")
		
		#retrieves the image using get, stream ensures there's no interruption while method is running
		r = requests.get(url, stream=True)
	
		if r.status_code == 200: #if response is successful, and returns 200
			with open(file_name, 'wb') as file: #open the file using writ-and-binary mode
				shutil.copyfileobj(r.raw,file) #copying the content of the file like object to the file
			print("Image successfully downloaded: ", file_name) #img downloaded, and saved into the file name that was given
			print("Please check your repos directory under the submitted name to see todays image")
		else:
			print("Image not found")
	else:
		print("Thanks for checking out NASA's Astronomy Photo of the day")
		return

def main():

	#Send HTTPS Get to the API of Nasa's astronomy picture of the day.
	get_apod_info = requests.get(f'{APOD_API}?api_key=DEMO_KEY')

	#Generated an API key in the event that I surpassed the rate limit allowed
	#get_apod_info = requests.get(f'{APOD_API}?api_key=c5S9CpJiWOhefmhFxa7OVuVi3zcWGTP0WYoh0b03')
	
	#decodes response
	got_apod = get_apod_info.json()
	
	
	url = got_apod['url'] #get the url used for the photo of the day	
	title = got_apod['title'] #title of the photo
	date = got_apod['date'] #"date published
	explanation = got_apod['explanation'] #Explaination of the photo
	
	#print the info above highlighting the titles of each section in green
	#print(f"{got_apod}\n\n")	
	print(crayons.green("Welcome to NASA's ASTRONOMY PHOTO OF THE DAY!!\n", bold=True))
	print(f"{crayons.green('Title:')} {title}\n")
	print(f"{crayons.green('Date:')} {date}\n")
	print(f"{crayons.green('Explanation:')}  {explanation}\n")

	
	img_download(url)
		
	
		
		
	
	

if __name__ == "__main__":
	main()
