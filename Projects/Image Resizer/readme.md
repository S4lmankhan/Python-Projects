---

# Image Resizer Script

This Python script allows you to resize an image using the OpenCV library. Simply update the name of your image file and the scale percentage to resize your image.

## Prerequisites

- Python 3.x
- OpenCV library

## Installation

First, ensure you have Python installed. Then, install the OpenCV library using pip:

```bash
pip install opencv-python
```

## Usage

1. **Update the image file name**: Modify the `cv2.imread` function in the script to include the name of the image file you want to resize. For example:

    ```python
    image = cv2.imread("your_image.jpg", cv2.IMREAD_UNCHANGED)
    ```

2. **Update the scale percentage**: Set the desired scale percentage in the `scale_percent` variable. For example:

    ```python
    scale_percent = 50  # Scale the image to 50% of its original size
    ```

3. **Run the script**: Execute the script to resize the image.

    ```python
    import cv2

    image = cv2.imread("your_image.jpg", cv2.IMREAD_UNCHANGED)

    scale_percent = 50  # Update this scale as an integer

    # Calculate new dimensions
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)

    output = cv2.resize(image, (new_width, new_height))

    # Save and display the resized image
    cv2.imwrite("resized_image.jpg", output)
    cv2.imshow("Resized Image", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

4. The script will resize the specified image file to the desired scale percentage and save the resized image as `resized_image.jpg`.

## Example

Here is a complete example of the script:

```python
import cv2

image = cv2.imread("your_image.jpg", cv2.IMREAD_UNCHANGED)

scale_percent = 50  # Update this scale as an integer

# Calculate new dimensions
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (new_width, new_height))

# Save and display the resized image
cv2.imwrite("resized_image.jpg", output)
cv2.imshow("Resized Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Contact

If you encounter any issues or have any questions, feel free to reach out to me on Instagram: [CodeWithSalty](https://www.instagram.com/CodeWithSalty).

## Credits

This script is created and maintained by [Salman Khan](https://github.com/S4lmankhan). If you find it useful, please give credit where it's due.

## License

This script is provided under the MIT License.

---
