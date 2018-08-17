# Facial-recognition-system
Simple Face Recognition algorithm using Python and OpenCV
Requirement

    Python 3.5
    OpenCV 3.1.0
    Numpy

Outline

This project consist of 3 parts, which are:

    Creating datasets (face_datasets.py)
    Train the model (training.py)
    Face Recognition (face_recognition.py)

How to run ?

    Make sure have executable permission. (chmod 777 .)
    Please make sure that you have folders called 'datasets' and 'trainer' in the same directory. (Optional, I have put the code so it will create if it's not exist.)
    Run in the command line the face_datasets.py for taking your face image as datasets. Don't forget to set each person's face to unique ID (You need to edit the code everytime, or maybe just change the id variable to raw_input[OPTIONAL])
    If you have more face to be include, change the ID and run the program again
    Train your datasets by running training.py
    Lastly, run face_recognition.py

Reading materials

    Object Detection using Haar-like features, link: http://www.cs.utexas.edu/~grauman/courses/spring2008/slides/Faces_demo.pdf
    Face Detection using Haar Cascades, link: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
    Haar-like Features, link: https://en.wikipedia.org/wiki/Haar-like_features
    Object Detection using Haar-cascades Classifier, link: http://ds.cs.ut.ee/Members/artjom85/2014dss-course-media/Object%20detection%20using%20Haar-final.pdf
    OpenCV Documentation, link: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
