import sys
import cv2
import numpy as np
import pyzed.sl as sl

def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create initialization parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720  # or HD1080, HD2K
    init_params.depth_mode = sl.DEPTH_MODE.NONE  # Only RGB stream for now
    init_params.coordinate_units = sl.UNIT.MILLIMETER

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("ZED Camera not connected or error:", err)
        exit(1)

    # Prepare image container
    image = sl.Mat()

    print("Press 'q' to quit")
    while True:
        if zed.grab() == sl.ERROR_CODE.SUCCESS:
            # Retrieve RGB image
            zed.retrieve_image(image, sl.VIEW.LEFT)
            frame = image.get_data()

            # Convert sl.Mat to OpenCV format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

            # Display using OpenCV
            cv2.imshow("ZED 2i Feed", frame_rgb)

        # Break loop on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close camera
    zed.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
