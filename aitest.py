import requests
from PIL import Image
from io import BytesIO
import os

# importing openai module
import openai
# assigning API KEY to the variable
  
openai.api_key = os.environ['OPENAI_API_KEY']


def generateTransform(text):
  # Read the image file from disk and resize it
  image = Image.open("darwin.jpeg")
  width, height = 256, 256
  image = image.resize((width, height))

  # Convert the image to a BytesIO object
  byte_stream = BytesIO()
  image.save(byte_stream, format='PNG')

  byte_array = byte_stream.getvalue()

  response = openai.Image.create_variation(
    image=byte_array,
    n=1,
    size="1024x1024"
  )
  return response["data"][0]["url"]

def generate(text):
  res = openai.Image.create(
    # text describing the generated image
    prompt=text,
    # number of images to generate 
    n=3,
    # size of each generated image
    size="1024x1024",
  )
  # returning the URL of one image as 
  # we are generating only one image
  # return res["data"][0]["url"]
  return res["data"]
# text = "photograph of fans celebrating, anfield football stadium with players, stadium lights, night"


text_array=[
  'Jurgen Klopp liverpool manager with cap',
  "Avenger",
  "Nick fury eye patch",
  "anfield in background",
  "Realistic",
  "Comicbook syle art"
  # 'darwin nunez',
  # 'celebrating'
  # 'cartoon egyptian pharaoh',
  # 'players playing on the ground',
  # 'salah liverpool player with his afro',
  # 'Liverpool football club', 
  # 'anfeild liverpool stadium ',
  'with lights in the background',
  # 'YNWA banner',
  # 'You will never walk alone'
  # 'national geographic', 
  # 'portrait', 'photo', 'photography'
  # '19 year old woman','35mm', 'F/2.8'
]


# text = "artistic van gough style, painting of domink szoboslai foorball player, celebrating, anfeild liverpool stadium with lights in the background"
text=','.join(text_array)
# calling the custom function "generate"
# saving the output in "url1"
data = generate(text)
counter = 0
print("data",data)

# f = open("urls.txt", "wb")

for d in data:
  counter=counter+1
  url =d["url"]

  file_content = text + ": " + str(url.encode('utf-8')) + "\n"
  print("file_content: ",file_content.encode('utf-8'))
  # f.write(file_content.encode('utf-8'))
  print ("saving image ",counter)
  with open("urls.txt", "a") as f:
   f.write(file_content)
  response = requests.get(url)
  filename = "image" + str(counter) + ".png"
  with open(filename, "wb") as f:
    f.write(response.content)

# f.close()
# using requests library to get the image in bytes
# response = requests.get(url1)
# print (response)
# with open("img.png", "wb") as f:
#   f.write(response.content)
# using the Image module from PIL library to view the image
# Image.open(response.raw)