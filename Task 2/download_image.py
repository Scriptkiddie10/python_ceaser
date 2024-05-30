import requests
from PIL import Image
from io import BytesIO

# URL of the image of Barbarian King (make sure the URL points to an image)
image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReRm_YeFshnJGk9yOFJyH9OxiMV_R3A1J7bViHyNTAiQ&s"

# Download the image
response = requests.get(image_url)
if response.status_code == 200:
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    
    # Save the image as a PNG file
    image_path = 'barbarian_king.png'
    image.save(image_path)
    print(f"Image saved as {image_path}")
else:
    print("Failed to download image")
