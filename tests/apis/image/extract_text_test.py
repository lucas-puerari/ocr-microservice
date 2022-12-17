import os
import pytest


@pytest.mark.parametrize(
    "image_name,mimetype",
    [
        ("image.png", "image/png"),
        ("image.jpg", "image/jpeg"),
        ("image.jpeg", "image/jpeg"),
    ]
)
def test_200_extract_text(client, image_name, mimetype):
    """
    TODO
    """

    image_path = f"{os.getcwd()}/tests/apis/image/data/{image_name}"

    response = client.post(
        "/extract-text",
        files={
            "file": (image_name, open(image_path, "rb"), mimetype)
        }
    )

    content = response.json()

    assert response.status_code == 200
    assert isinstance(content, object)
    assert isinstance(content["message"], str)


@pytest.mark.parametrize(
    "image_name,mimetype",
    [
        ("image.bmp", "image/bmp"),
        ("image.pdf", "application/pdf"),
    ]
)
def test_400_extract_text(client, image_name, mimetype):
    """
    TODO
    """

    image_path = f"{os.getcwd()}/tests/apis/image/data/{image_name}"

    response = client.post(
        "/extract-text",
        files={
            "file": (image_name, open(image_path, "rb"), mimetype)
        }
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Recived file has a mimetype not allowed"
    }
