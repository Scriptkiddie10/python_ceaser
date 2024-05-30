from PIL import Image, ImageDraw

# Create an image with RGB mode and size 100x100
image = Image.new('RGB', (100, 100), color='white')

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Draw a simple rectangle
draw.rectangle([25, 25, 75, 75], fill='blue')

# Save the image
image_path = 'generated_image.png'
image.save(image_path)

print(f"Image saved as {image_path}")
