#!/usr/bin/env python3

#import libraries
import requests
import shutil

#set the Astronomy picture of the day API key to a constant
APOD_API = "https://api.nasa.gov/planetary/apod" 


def img_download(url):
	file_name = input("Save image as (string): ")
	r = requests.get(url, stream=True)
	
	if r.status_code == 200:
		with open(file_name, 'wb') as file:
			shutil.copyfileobj(r.raw,file)
		print("Image successfully downloaded: ", file_name)
		print("Please check your repo directory to see todays image")
	else:
		print("Image not found")

def main():

	#Send HTTPS Get to the API of Nasa's astronomy picture of the day.
	get_apod_info = requests.get(f'{APOD_API}?api_key=DEMO_KEY')
	
	#decodes response
	got_apod = get_apod_info.json()
	
	url = got_apod['url']
	title = got_apod['title']
	date = got_apod['date']
	explanation = got_apod['explanation']

	print(f"Title: {title}\n")
	print(f"Date:{date}\n")
	print(f"Explanation:  {explanation}\n")

	#for apod in got_apod:
		#print(f"\n{apod}:\n{got_apod[apod]}\n")
	
	img_download(url)
		
	
		
		
	
	

if __name__ == "__main__":
	main()
