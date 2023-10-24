

# import tempfile
# import streamlit as st

# #import cv2
# # import mediapipe as mp


# # #demo video 
# # DEMO_VIDEO = 'demo.mp4'



# # #mediapipe inbuilt solutions 
# # mp_face_detection = mp.solutions.face_detection
# # mp_drawing = mp.solutions.drawing_utils

# from webcam import webcam





# def main():

#     #title 
#     st.title('Face Detection App')

#     #sidebar title
#     st.sidebar.title('Face Detection App')

#     # st.sidebar.subheader('Parameters')
#     # #creating a button for webcam
#     # use_webcam = st.sidebar.button('Use Webcam')
#     # #creating a slider for detection confidence 
#     # detection_confidence = st.sidebar.slider('Min Detection Confidence', min_value =0.0,max_value = 1.0,value = 0.5)
    
#     # #model selection 
#     # model_selection = st.sidebar.selectbox('Model Selection',options=[0,1,2])
#     # st.markdown(' ## Output')
#     # stframe = st.empty()
    
#     # #file uploader
#     # video_file_buffer = st.sidebar.file_uploader("Upload a video", type=[ "mp4", "mov",'avi','asf', 'm4v' ])

    
#     # #temporary file name 
#     # tfflie = tempfile.NamedTemporaryFile(delete=False)

#     # if not video_file_buffer:

#     #     if use_webcam:
#     #         vid = cv2.VideoCapture(0)
#     #     else:
#     #         vid = cv2.VideoCapture(DEMO_VIDEO)
#     #         tfflie.name = DEMO_VIDEO
    
#     # else:
#     #     tfflie.write(video_file_buffer.read())
#     #     vid = cv2.VideoCapture(tfflie.name)

#     # #values 
#     # width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#     # height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     # fps = int(vid.get(cv2.CAP_PROP_FPS))
#     # #codec = cv2.VideoWriter_fourcc(*FLAGS.output_format)
#     # codec = cv2.VideoWriter_fourcc('V','P','0','9')
#     # out = cv2.VideoWriter('output1.webm', codec, fps, (width, height))


#     # st.sidebar.text('Input Video')
#     # st.sidebar.video(tfflie.name)

#     # # drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


#     # with mp_face_detection.FaceDetection(
#     # model_selection=model_selection, min_detection_confidence=detection_confidence) as face_detection:
        
#     #     while vid.isOpened():

#     #         ret, image = vid.read()

#     #         if not ret:
#     #             break
#     #         image.flags.writeable = False
#     #         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     #         results = face_detection.process(image)

#     #         if results.detections:
#     #             for detection in results.detections:
#     #                 mp_drawing.draw_detection(image, detection)
#     #         stframe.image(image,use_column_width=True)

#     #     vid.release()
#     #     out.release()
#     #     cv2.destroyAllWindows()


#     captured_image = webcam()
#     if captured_image is None:
#         st.write("Waiting for capture...")
#     else:
#         st.write("Got an image from the webcam:")
#         st.image(captured_image)

#     st.success('Video is Processed')
#     st.stop()

# if __name__ == '__main__':
#     main()

import tempfile
import streamlit as st
import mediapipe as mp

from webcam import webcam

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

st.title("Webcam capture component")

st.write("""
- Accesses the user's webcam and displays the video feed in the browser.
- Click the "Capture Frame" button to grab the current video frame and
return it to Streamlit.
""")
captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)

