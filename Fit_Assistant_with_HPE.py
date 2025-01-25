import cv2
import streamlit as st
import numpy as np

BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]
net = cv2.dnn.readNetFromTensorflow("graph_opt.pb")

measurements = {"shoulder_width": None, "waist_width": None}

def LightTheme():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: transparent;
            background-image: url("https://images.unsplash.com/uploads/14116941824817ba1f28e/78c8dff1?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background: transparent;
            background-image: url("https://images.unsplash.com/photo-1447433693259-c8549e937d62?q=80&w=1777&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .Widget>label {
            color: white;
        }
        [class^="st-b"]  {
            color: white;
        }
        .st-bb {
            color: white;
        }
        .st-at {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        div.stButton>button {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def DarkTheme():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: black;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background: black;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .Widget>label {
            color: white;
        }
        [class^="st-b"]  {
            color: white;
        }
        .st-bb {
            color: white;
        }
        .st-at {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        div.stButton>button {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def measure_distance(point1,point2):
    return np.linalg.norm(np.array(point1)-np.array(point2))
# Function to perform pose estimation and extract measurements
def pose_estimation(frame):
     inWidth = 368
     inHeight = 368
     threshold = 0.2
     frameWidth = frame.shape[1]
     frameHeight = frame.shape[0]
     net.setInput(cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
     out = net.forward()
     out = out[:, :19, :, :]
     points = []
     for i in range(len(BODY_PARTS)):
         heatMap = out[0, i, :, :]
         _, conf, _, point = cv2.minMaxLoc(heatMap)
         x = (frameWidth * point[0]) / out.shape[3]
         y = (frameHeight * point[1]) / out.shape[2]
         points.append((int(x), int(y)) if conf > threshold else None)
    
     if BODY_PARTS['LShoulder'] < len(points) and BODY_PARTS['RShoulder'] < len(points):
        measurements["shoulder_width"] = measure_distance(points[BODY_PARTS['LShoulder']], points[BODY_PARTS['RShoulder']]) if points[BODY_PARTS['LShoulder']] and points[BODY_PARTS['RShoulder']] else None
     else:
        measurements["shoulder_width"] = None
     if BODY_PARTS['LHip'] < len(points) and BODY_PARTS['RHip'] < len(points):
         measurements["waist_width"] = measure_distance(points[BODY_PARTS['LHip']], points[BODY_PARTS['RHip']]) if points[BODY_PARTS['LHip']] and points[BODY_PARTS['RHip']] else None
     else:
        measurements["waist_width"] = None
     for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]
        if idFrom < len(points) and idTo < len(points):
            if points[idFrom] and points[idTo]:
                cv2.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
                cv2.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
                cv2.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
     return frame, measurements
     
st.title('Custom Tailoring Assistance Tool') 
st.sidebar.header('Upload Section')
st.sidebar.write('Upload an image or video for pose detection and measurements.')
 # File uploader
uploaded_file = st.sidebar.file_uploader("Choose an image or video", type=["jpg", "jpeg", "png", "mp4"])
known_length_pixels = 100
known_length_cm =10.9
scale_factor = known_length_cm / known_length_pixels
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)
    # Perform pose estimation and measurement extraction 
    processed_image, measurements = pose_estimation(frame)
    st.image(processed_image, caption='Detected Poses', use_column_width=True)
    st.write("### Measurements")
    if measurements["shoulder_width"]:
         st.write(f"**Shoulder Width**: {measurements['shoulder_width']:.2f} px")
    else:
         st.write("Shoulder Width: Not detected") 
    if measurements["waist_width"]:
         st.write(f"**Waist Width**: {measurements['waist_width']:.2f} px")
    else:
         st.write("Waist Width: Not detected")
 # Display other measurements here
# #   Option to save measurements
# if st.button('Save Measurements'):
#      save_measurements(measurements)
#      st.success('Measurements saved successfully!')
 # Sidebar customization options
    
 
 # Apply adjustments to measurements 
if measurements['shoulder_width'] is not None:
    measurements['shoulder_width']  *= scale_factor
else:
    measurements['shoulder_width'] = "Not detected"
if measurements['waist_width'] is not None:
    measurements['waist_width'] *= scale_factor
else:
    measurements['waist_width'] = "Not detected"
 # Display adjusted measurements
if isinstance(measurements['shoulder_width'], str):
    st.write(f"**Adjusted Shoulder Width**: {measurements['shoulder_width']}")
else:
    st.write(f"**Adjusted Shoulder Width**: {measurements['shoulder_width']:.2f} cm")
if isinstance(measurements['waist_width'], str):
    st.write(f"**Adjusted Waist Width**: {measurements['waist_width']} ")
else:
    st.write(f"**Adjusted Waist Width**: {measurements['waist_width']:.2f} cm")