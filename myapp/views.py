from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
from twilio.rest import Client
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import base64
from geopy.geocoders import Nominatim
from rest_framework.decorators import api_view

import geocoder



CURR_ID = 0
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
sleep_frames = 20
first_frame = True
# initialize the frame counters and the total number of blinks
COUNTER = 0
TOTAL = 0
SETS = 0
CHECK = True
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
# print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("static/shape_predictor_68_face_landmarks0.dat")

#     # grab the indexes of the facial landmarks for the left and
#     # right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# 0 for all good; continue
# 1 for ring the alarm
# 2 for stop the alarm
# 3 for close the app after sending sms
STATUS = 0
profile = models.Profile.objects.filter(id=1)
no_trips = profile[0].no_of_trips
no_sleeps = profile[0].no_of_sleeps
no_trips = no_trips + 1
PROFILE = 0


def StartDrive(request):
    return render(request, "drive.html")


@api_view(['POST'])
def proc_frame(request):
    global PROFILE

    PROFILE = request.user  # get id of logged in user
    if request.user.is_authenticated:
        PROFILE = models.Profile.objects.filter(id=PROFILE.id)

    img_data = request.data['label']
    dummy(img_data)
    return HttpResponse("messages sent!", 201)


def dummy(base64img):
    filename = 'dummy.jpg'
    imgd = base64.b64decode(base64img)
    with open(filename, 'wb') as f:
        f.write(imgd)
    processing()



def processing():
    print("INSIDE PROCESSING ")
    global EYE_AR_THRESH
    global EYE_AR_CONSEC_FRAMES
    global sleep_frames

    # frame counters and total number of blinks
    global COUNTER
    global TOTAL
    global SETS
    global CHECK

    global detector
    global predictor

    global lStart
    global lEnd
    global rStart
    global rEnd

    global profile
    global no_trips
    global no_sleeps
    global first_frame

    if first_frame:
        no_trips = PROFILE[0].no_of_trips
        models.Profile.objects.filter(id=1).update(no_of_trips=no_trips)
        first_frame = False


    no_sleeps = PROFILE[0].no_of_sleeps
    no_trips = no_trips + 1




    global STATUS
    #     # loop over frames from the video stream
    #         # grab the frame from the threaded video file stream, resize
    #         # it, and convert it to grayscale
    #         # channels)
    frame = cv2.imread('dummy.jpg')
    #         # print(f"<br>frame is {len(frame)}<br>")
    frame = imutils.resize(frame, width=450)
    #         # print(f"<br>AFTER frame is {frame.shape}<br>")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print("gray: ", gray)
    #         # detect faces in the grayscale frame
    rects = detector(gray, 0)
    #
    #         # loop over the face detections
    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the left and right eye coordinates, then use the
        # coordinates to compute the eye aspect ratio for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # compute the convex hull for the left and right eye, then
        # visualize each of the eyes
        # leftEyeHull = cv2.convexHull(leftEye)
        # rightEyeHull = cv2.convexHull(rightEye)
        # cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        # cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        if ear < EYE_AR_THRESH:
            COUNTER += 1

            if COUNTER >= sleep_frames:

                if CHECK:
                    no_sleeps = no_sleeps + 1
                    models.Profile.objects.filter(id=1).update(no_of_sleeps=no_sleeps)
                    CHECK = False
                COUNTER = 0
                SETS += 1
                print("DON'T SLEEP")
                STATUS = 1
                # pygame.mixer.music.load("static/file.mp3")
                # pygame.mixer.music.play()
                if SETS >= 2:
                    # send_sms()
                    SETS = 0
                    STATUS = 10
                    return


        # otherwise, the eye aspect ratio is not below the blink
        # threshold
        else:

            # pygame.mixer.music.stop()
            STATUS = 0

            # if the eyes were closed for a sufficient number of
            # then increment the total number of blinks
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1

                # reset the eye frame counter
                COUNTER = 0
                SETS = 0

        # cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        # cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        # cv2.putText(frame, "Frames: {}".format(COUNTER), (30, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


@api_view(['GET'])
def status_view(request):
    global STATUS
    temp = STATUS
    if STATUS == 10:
        STATUS = 0
    return HttpResponse(temp)


def loc(lat, long):
    geolocator = Nominatim(user_agent="Drowsiness Detection")
    location = geolocator.reverse(f"{lat}, {long}")
    return location


@api_view(['POST'])
def send_sms(request):
    profile = request.user
    if request.user.is_authenticated:
        profile = models.Profile.objects.filter(id=profile.id)
    # profile = models.Profile.objects.filter(id=1)
    curr_loc = loc(request.data['latitude'], request.data['longitude'])
    message_to_broadcast = (
        f"{profile[0].Name} is in DANGER!!! His latitude and longitude are: ({request.data['latitude']}, {request.data['longitude']}) - {curr_loc}")

    TWILIO_ACCOUNT_SID = "AC484e144c28d7b6175deebb3811e8cc0c"
    TWILIO_AUTH_TOKEN = "f810baa628932b84bea885f76e60aceb"
    TWILIO_NUMBER = "+13073129312"
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    output = client.messages.create(to="+14086607308",
                                    from_=TWILIO_NUMBER,
                                    body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("myapp:addprofile")
    template_name = "signup.html"


def StartDrive(request):
    return render(request, 'drive.html')


def get_info(request):
    profile = request.user  # get id of logged in user
    if request.user.is_authenticated:
        profile = models.Profile.objects.filter(id=profile.id)
        sleeps = profile[0].no_of_sleeps
        trips = profile[0].no_of_trips
        name = profile[0].Name
        if trips == 0:
            accr = 0
        else:
            accr = (trips - sleeps) / trips * 100
        return render(request, 'myprofile.html', {'name': name, 'accr': accr, 'sleeps': sleeps, 'trips': trips})
    else:
        response = redirect('/myapp/login/')
        return response


def loc_1():
    g = geocoder.ip('me')
    geolocator = Nominatim(user_agent="Drowsiness Detection")
    loca = str(g.latlng[0]) + "," + str(g.latlng[1])
    location = geolocator.reverse(loca)
    return location



# def StartDrive(request):
# #     pygame.mixer.pre_init(22050, -16, 2, 64)
# #     pygame.mixer.init()
# #     pygame.mixer.quit()
# #     pygame.mixer.init(22050, -16, 2, 64)
# #
# #     profile = models.Profile.objects.filter(id=1)
# #     no_trips = profile[0].no_of_trips
# #     no_sleeps = profile[0].no_of_sleeps
# #     no_trips = no_trips + 1
# #     models.Profile.objects.filter(id=1).update(no_of_trips=no_trips)
# #
#     EYE_AR_THRESH = 0.3
#     EYE_AR_CONSEC_FRAMES = 3
#     sleep_frames = 100
#
#     # initialize the frame counters and the total number of blinks
#     COUNTER = 0
#     TOTAL = 0
#     SETS = 0
#     CHECK = True
#     # initialize dlib's face detector (HOG-based) and then create
#     # the facial landmark predictor
#     print("[INFO] loading facial landmark predictor...")
#     detector = dlib.get_frontal_face_detector()
#     predictor = dlib.shape_predictor("static/shape_predictor_68_face_landmarks0.dat")
#
# #     # grab the indexes of the facial landmarks for the left and
# #     # right eye, respectively
#     (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
#     (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
# #
# #     # start the video stream thread
# #     print("[INFO] starting video stream thread...")
# #     vs = FileVideoStream("").start()
# #     fileStream = True
# #     vs = VideoStream(src=0).start()
# #     # print(f"----- VS is {vs}")
# #     # vs = VideoStream(usePiCamera=True).start()
# #     fileStream = False
# #     time.sleep(1.0)
# #
# #     # loop over frames from the video stream
# #     while True:
# #         # if this is a file video stream, then we need to check if
# #         # there any more frames left in the buffer to process
# #         if fileStream and not vs.more():
# #             break
# #
# #         # grab the frame from the threaded video file stream, resize
# #         # it, and convert it to grayscale
# #         # channels)
#         frame = cv2.imread('dummy.jpg')
# #         # print(f"<br>frame is {len(frame)}<br>")
#         frame = imutils.resize(frame, width=450)
# #         # print(f"<br>AFTER frame is {frame.shape}<br>")
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         print(f"????? {gray.shape} ?????")
# #         # detect faces in the grayscale frame
#         rects = detector(gray, 0)
# #
# #         # loop over the face detections
#         for rect in rects:
# #             # determine the facial landmarks for the face region, then
# #             # convert the facial landmark (x, y)-coordinates to a NumPy
# #             # array
#             shape = predictor(gray, rect)
#             shape = face_utils.shape_to_np(shape)
# #
# #             # extract the left and right eye coordinates, then use the
# #             # coordinates to compute the eye aspect ratio for both eyes
#             leftEye = shape[lStart:lEnd]
#             rightEye = shape[rStart:rEnd]
#             leftEAR = eye_aspect_ratio(leftEye)
#             rightEAR = eye_aspect_ratio(rightEye)
# #
# #             # average the eye aspect ratio together for both eyes
#             ear = (leftEAR + rightEAR) / 2.0
# #
# #             # compute the convex hull for the left and right eye, then
# #             # visualize each of the eyes
#             leftEyeHull = cv2.convexHull(leftEye)
#             rightEyeHull = cv2.convexHull(rightEye)
# #             cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
# #             cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
# #
# #             # check to see if the eye aspect ratio is below the blink
# #             # threshold, and if so, increment the blink frame counter
#             if ear < EYE_AR_THRESH:
#                 COUNTER += 1
# #
#                 if COUNTER >= sleep_frames:
# #
#                     if CHECK:
#                         no_sleeps = no_sleeps + 1
#                         models.Profile.objects.filter(id=1).update(no_of_sleeps=no_sleeps)
#                         CHECK = False
#                     COUNTER = 0
#                     SETS += 1
#                     print("DON'T SLEEP")
#   ############ return get request flag to ring the alarm and
#
#                     # pygame.mixer.music.load("static/file.mp3")
# #                     pygame.mixer.music.play()
#                     if SETS >= 1:
#                         SendSMS()
#                         #### return get request with some flag to break from the loop
#                         # SETS = 0
# #
# #
# #             # otherwise, the eye aspect ratio is not below the blink
# #             # threshold
#             else:
# #
# #                 pygame.mixer.music.stop()
# #
# #                 # if the eyes were closed for a sufficient number of
# #                 # then increment the total number of blinks
#                 if COUNTER >= EYE_AR_CONSEC_FRAMES:
#                     TOTAL += 1
# #
# #                     # reset the eye frame counter
#                     COUNTER = 0
#                     SETS = 0
#
#             cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#             cv2.putText(frame, "Frames: {}".format(COUNTER), (30, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#
#         cv2.imshow("Frame", frame)
#         key = cv2.waitKey(1) & 0xFF
#
#         # if the `q` key was pressed, break from the loop
#         if key == ord("q"):
#             break
#
#     # do a bit of cleanup
#     cv2.destroyAllWindows()
#     vs.stop()
#     return render(request, 'index.html')


class add_profile(CreateView):
    form_class = forms.AddProfileForm
    success_url = reverse_lazy("myapp:login")
    template_name = "addprofile.html"
