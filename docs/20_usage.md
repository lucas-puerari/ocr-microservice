# OCR Usage

## POST /extract-text

To extract text from an image, make a POST request to the `/extract-text` endpoint with the image file attached. The microservice will return a JSON object containing the extracted text.

**Request**

(run this curl from `/docs/images` folder)

      curl -X 'POST' \
        'http://0.0.0.0:3000/extract-text' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@ocr-hello-world.png;type=image/png'

**Response**

      { "message": "Hello world\n\f" }
