import cloudinary
from decouple import config  # os.environ.get()

# Configuration
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME', default='')
CLOUDINARY_PUBLIC_API_KEY = config('CLOUDINARY_PUBLIC_API_KEY', default='917431891649895')
CLOUDINARY_SECRET_API_KEY = config('CLOUDINARY_SECRET_API_KEY')


def cloudinary_init():
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_PUBLIC_API_KEY,
        api_secret=CLOUDINARY_SECRET_API_KEY,  # Click 'View API Keys' above to copy your API secret
        secure=True
    )
