from src.downyoutubepy import DownYoutubePy
import streamlit as st
import pandas as pd

import time


# App Title and Mode
st.title('Race Bib Number Detector')
st.sidebar.header("Mode")

mode = st.sidebar.radio(
    'Select Mode',
    options=['Image Files', 'Demo', 'Image', 'Video']
)

'''
if mode == 'Image Files':
    # Get Image from User
    user_file = st.file_uploader(label='Image for analysis:',
        type=['jpg', 'png'])

    button_loc = st.empty()
    
    # Display image and convert for predicting
    if user_file != None:
        text_loc = st.empty()
        text_loc.text('This is your image:')
        # Convert the file to an opencv image.
        # From: https://github.com/streamlit/streamlit/issues/888
        file_bytes = np.asarray(bytearray(user_file.read()), dtype=np.uint8)
        img = cv.imdecode(file_bytes, 1)
        img_loc = st.empty()
        img_loc.image(img, channels='BGR')

        # get bib prediction
        output = Detector.get_rbns(img)

        # annotate image
        if output != None:
            text_loc.text(f"Detected {len(output)} RBN(s)")
            for detection in output:
                img = Detector.annotate(img, detection, color)
        else:
            text_loc.text("No RBN's Detected")

        #display annotated image
        img_loc.image(img, channels='BGR')

elif mode == 'Image':
    # Get Image from User
    user_file = st.file_uploader(label='Image for analysis:', type=['jpg', 'png'])

    
    button_loc = st.empty()

    # Display image and convert for predicting
    if user_file != None:
        text_loc = st.empty()
        text_loc.text('This is your image: ')
        # Convert the file to an opencv image.
        # From: https://github.com/streamlit/streamlit/issues/888
        file_bytes = np.asarray(bytearray(user_file.read()), dtype=np.uint8)
        img = cv.imdecode(file_bytes, 1)
        #img_loc = st.empty()
        #img_loc.image(img, channels='BGR')

        if button_loc.button('Detect'):
            # get bib prediction
            output = Detector.get_rbns(img)

            # annotate image
            if output != None:
                text_loc.text(f"Detected {len(output)} RBN(s)")
                for detection in output:
                    img = Detector.annotate(img, detection, color)
            else:
                text_loc.text("No RBN's Detected")

            #display annotated image
            #img_loc.image(img, channels='BGR')
else:

    if mode == 'Demo':
        video_path = 'Data/bib_detector_demo.mp4'
        video_file = open(video_path, 'rb')
        video_bytes = video_file.read()

    elif mode == 'Video':
        video_bytes = st.file_uploader(label='Video for analysis:',
        type=['mp4'])
        # Use temp file for OpenCV with user uploaded video
        # from https://discuss.streamlit.io/t/how-to-access-uploaded-video-in-streamlit-by-open-cv/5831/4
        if video_bytes == None:
            st.stop()
        else:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_bytes.read())
            video_path = tfile.name

    button_loc = st.empty()
    text_loc = st.empty()
    video_loc = st.empty()

    video_loc.video(video_bytes)

    if button_loc.button('Detect'):
        # open video for detection
        cap = cv.VideoCapture(video_path)
        cap.set(cv.CAP_PROP_FPS, 25)
        # set ouput specifications
        fourcc = cv.VideoWriter_fourcc('m','p','4','v')
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        num_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
        vid_out = cv.VideoWriter('Data/output.mp4', fourcc, 25.0, (width,height))
        #outfile = tempfile.NamedTemporaryFile(delete=False)
        #vid_out = cv.VideoWriter(outfile.name, fourcc, 25.0, (width,height))

        frames_complete = 0
        rank = []
        prev_rbn = None
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # get bib prediction
            output = Detector.get_rbns(frame, single=True)

            # annotate image
            if output != None:
                frame = Detector.annotate(frame, output[0], color)

                if prev_rbn == None or prev_rbn != output[0][0]:
                    rbn_count = 0
                    prev_rbn = output[0][0]
                else:
                    rbn_count += 1
                
                if rbn_count >= 25 and prev_rbn not in rank:
                    rank.append(prev_rbn)

            #save annotated frame
            vid_out.write(frame)
            frames_complete += 1
            video_loc.progress(frames_complete / num_frames)

        cap.release()
        vid_out.release()

        button_loc.text("Complete.  Press play to see annotated video.")
        video_file = open('Data/output.mp4', 'rb')
        #video_file = open(outfile.name, 'rb')
        video_bytes = video_file.read()
        video_loc.video(video_bytes)

        st.header("Rank Order")
        for i, rbn in enumerate(rank):
            st.subheader(f'{i+1}.  {rbn}')
'''