import streamlit as st
import os

# Set page title
st.set_page_config(page_title="Swapnil Roy's Media Uploader")

# Create a sidebar menu for selecting media type
media_type = st.sidebar.selectbox("Select media type", ("Image", "Video"))

if media_type == "Video":
    # Create a file uploader widget for videos
    video_file = st.file_uploader("Choose a video file", type=["mp4", "avi"])

    # Set the video caption to the file name, if a file is selected
    video_caption = video_file.name if video_file is not None else None

    # Add a text input for the video caption
    video_caption = st.text_input(
        "Enter a caption for the video (optional)", value=video_caption)

    # Display the video if a file is selected
    if video_file is not None:
        # Replace None with an empty string for video_caption
        video_caption = "" if video_caption is None else video_caption
        st.video(video_file, caption=video_caption)

        # Add a "Save" button to save the video
        if st.button("Save Video"):
            # Get the file name and extension
            file_name, ext = os.path.splitext(video_file.name)
            # Save the file in the same directory as the script
            with open(file_name + ext, "wb") as f:
                f.write(video_file.getbuffer())
            st.success(f"{file_name}{ext} saved successfully!")

elif media_type == "Image":
    # Create a sidebar menu for selecting image source
    image_source = st.sidebar.selectbox(
        "Select image source", ("Upload", "Capture"))

    if image_source == "Upload":
        # Create a file uploader widget for images
        image_file = st.file_uploader(
            "Choose an image file", type=["jpg", "jpeg", "png"])

        # Set the image caption to the file name, if a file is selected
        image_caption = image_file.name if image_file is not None else None

        # Add a text input for the image caption
        image_caption = st.text_input(
            "Enter a caption for the image (optional)", value=image_caption)

        # Display the image if a file is selected
        if image_file is not None:
            st.image(image_file, use_column_width=True, caption=image_caption)

            # Add a "Save" button to save the image
            if st.button("Save Image"):
                # Get the file name and extension
                file_name, ext = os.path.splitext(image_file.name)
                # Save the file in the same directory as the script
                with open(file_name + ext, "wb") as f:
                    f.write(image_file.getbuffer())
                st.success(f"{file_name}{ext} saved successfully!")

    elif image_source == "Capture":
        # Get an image from the user's camera
        image = st.camera_input("Take a picture")

        # Set the image caption to the default name "captured_image"
        image_caption = "captured_image"

        # Add a text input for the image caption
        image_caption = st.text_input(
            "Enter a caption for the image (optional)", value=image_caption)

        # Display the image
        if image is not None:
            # Replace None with an empty string for image_caption
            image_caption = "" if image_caption is None else image_caption
            st.image(image, use_column_width=True, caption=image_caption)

        # Add a "Save" button to save the image
        if st.button("Save Image"):
            # Save the file in the same directory as the script
            file_name = image_caption
            ext = ".jpg"
            with open(file_name + ext, "wb") as f:
                f.write(image.getvalue())
            st.success(f"{file_name}{ext} saved successfully!")
