# Watermarking Tool

This is a Python script using Tkinter to create a graphical user interface for adding watermarks to images. The script
allows users to customize text, font, color, opacity, and position of the watermark on an image.

## Getting Started

### Prerequisites

- Make sure you have Python installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/watermark-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd watermark-tool
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Script

Execute the script using the following command:

```bash
python watermark_tool.py
```

## Usage

1. The main window opens with a canvas displaying a demo image.
2. Use the form on the right to customize the watermark.
3. Enter text, choose font and size, pick color, set opacity, and adjust the position.
4. Click the "Get Text Over Image" button to apply the watermark to the image.
5. Use additional buttons to upload a new image, save the current image, and perform other functions.

## Form Controls

- **Text Entry**: Enter the text for the watermark.
- **Font Entry**: Choose the font for the text.
- **Font Size Entry**: Set the font size.
- **Color Picker**: Pick a color for the text.
- **Opacity Entry**: Set the opacity level for the text.
- **Move Up/Down/Left/Right Buttons**: Adjust the position of the watermark.
- **Degree Entry**: Set the rotation angle for the text.
- **Upload Picture Button**: Upload a new image for watermarking.
- **Save Picture Button**: Save the current image with the watermark.

## Callback Functions

- `bind_for_change_text_color`: Change text color based on the selected color in the form.
- `bind_for_get_text_over_image`: Apply the watermark to the image.
- `bind_for_get_img`: Upload a new image to the canvas.
- `bind_for_change_font`: Change text font and size based on user input.
- `bind_for_opacity`: Change the opacity of the text.
- `bind_for_move_up/down/left/right`: Move the text in the specified direction.
- `bind_for_rotate_text`: Rotate the text by the specified angle.
- `bind_for_save_img`: Save the image with the watermark.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
