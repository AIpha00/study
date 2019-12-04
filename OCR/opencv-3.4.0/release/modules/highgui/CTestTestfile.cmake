# CMake generated Testfile for 
# Source directory: /Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/highgui
# Build directory: /Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/modules/highgui
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_highgui "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/bin/opencv_test_highgui" "--gtest_output=xml:opencv_test_highgui.xml")
set_tests_properties(opencv_test_highgui PROPERTIES  LABELS "Main;opencv_highgui;Accuracy" WORKING_DIRECTORY "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/test-reports/accuracy" _BACKTRACE_TRIPLES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVUtils.cmake;1154;add_test;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;1168;ocv_add_test_from_target;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/highgui/CMakeLists.txt;161;ocv_add_accuracy_tests;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/highgui/CMakeLists.txt;0;")
